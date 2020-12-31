title: New in 2.3: KeyFinder support and license change to GPL v3
authors: Jan Holthuis
tags: license, key detection, 2.3, beta
status: draft

Starting with the 2.3, Mixxx will be licensed under the terms of the [GNU General Public License (GNU GPL) version 3](https://www.gnu.org/licenses/rms-why-gplv3.html).
This step is necessary because it allows us to integrate support for the excellent [KeyFinder library](https://github.com/mixxxdj/libKeyFinder) by Ibrahim Sha'ath.

[KeyFinder](http://www.ibrahimshaath.co.uk/keyfinder/) is a pretty accurate open-source key detection tool.
It's been in the top 3 of the [2020 key detection comparison on Reddit](https://www.reddit.com/r/DJs/comments/hwlzyt/key_detection_comparison_2020/) and performs considerably better than the key analyzer from the [QM-DSP library](https://code.soundsoftware.ac.uk/projects/qm-dsp) that current stable version of Mixxx is using.

Unfortunately, it's also a lot slower than the QM-DSP algorithm (because the latter divides the sample rate by 8 and only analyzes every 8th window, resulting in a speedup factor of 64).
We hope to improve performance in the future.
Until then, the Queen Mary key Analyzer will be selected by default and you'll have to enable KeyFinder in the Key Detection settings.

KeyFinder is licensed under the terms of the GPL v3 (or later), which means that any code using it also needs to be GPL v3.
Therefore, Mixxx is switching from GPL v2 (or later) to GPL v3 (or later).

Don't worry:
Mixxx is still [free]({filename}/news/2020-05-22-you-dont-need-to-pay-for-mixxx.md) and always will be.

The most notable change with GPLv3 is that it prevents [tivoization](http://gplv3.fsf.org/rms-why.html):

> Tivoization means computers (called “appliances”) contain GPL-covered software that you can't change, because the appliance shuts down if it detects modified software.
> The usual motive for tivoization is that the software has features the manufacturer thinks lots of people won't like.
> The manufacturers of these computers take advantage of the freedom that free software provides, but they don't let you do likewise.

In other words: If you're a hardware manufacturer and want to embed Mixxx or parts of Mixxx into your product (e.g. a standalone controller running Mixxx), you still can, but you mustn't implement measures designed to prevent users from flashing a custom, modified version of Mixxx on that device.

Check the [quick guide on the GNU website](https://www.gnu.org/licenses/quick-guide-gplv3) and the [FAQ](https://www.gnu.org/licenses/gpl-faq) for more details.
