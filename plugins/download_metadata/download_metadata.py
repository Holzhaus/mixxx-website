import json
import logging
import datetime
import urllib.request
from pelican import signals


def format_size(num, suffix="B"):
    for unit in ("", "Ki", "Mi", "Gi", "Ti", "Pi", "Ei", "Zi"):
        if abs(num) < 1024.0:
            return "%3.1f%s%s" % (num, unit, suffix)
        num /= 1024.0
    return "%.1f%s%s" % (num, "Yi", suffix)


def page_generator_context(page_generator, metadata):
    """
    Iterate through author objects in metadata and add some additional
    properties.
    """
    logger = logging.getLogger(__name__)

    try:
        date_format = tuple(
            page_generator.context["generated_content"].values()
        )[0].date_format
    except IndexError:
        date_format = "%Y-%m-%d"
    datetime_format = f"{date_format} %H:%M"

    for version_name, version_data in metadata.get("versions", {}).items():
        manifest_url = version_data.get("download_manifest")
        if not manifest_url:
            continue

        req = urllib.request.Request(
            manifest_url,
            headers={
                "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:86.0) Gecko/20100101 Firefox/86.0",
            },
        )
        try:
            resp = urllib.request.urlopen(req, timeout=10)
            manifest_data = resp.read().decode()
        except IOError:
            logger.warning(
                "Failed to retrieve manifest URL: %s",
                manifest_url,
                exc_info=True,
            )
            continue

        manifest = json.loads(manifest_data)
        for download in version_data.get("downloads", []):
            for package in download.get("packages", []):
                slug = f"{download['slug']}-{package['slug']}"
                metadata = manifest.get(slug)
                if not metadata:
                    continue

                logger.debug("Updating download: %s", slug)
                package["url"] = metadata["file_url"]
                package["size"] = format_size(int(metadata["file_size"]))
                package["date"] = datetime.datetime.fromisoformat(
                    metadata["file_date"]
                )
                package["locale_date"] = package["date"].strftime(
                    datetime_format
                )
                package["commit_id"] = metadata["commit_id"]
                package["commit_url"] = metadata["commit_url"]
                package["build_log_url"] = metadata["build_log_url"]


def register():
    """ Subscribe to Pelican's signals. """
    signals.page_generator_context.connect(page_generator_context)