title: New in 2.3: Importing tracks and cues from Rekordbox removable devices
authors: Evan
tags: 2.3, rekordbox
date: 2020-07-20 12:00:00

Do you rock your gigs armed only with your cans and a Rekordbox prepared USB flash drive? Ever been tempted to play your carefully curated tracks on something other than a CDJ or Rekordbox, on something that is free and open-source? We have news for you!

Mixxx 2.3 will support reading the following from Rekordbox prepared removable devices on all of Mixxx's supported platforms:

* Folders
* Playlists
* Beatgrids
* Hotcues
* Memory cues
* Loops

You can use this new feature now in [Mixxx 2.3 beta](/download/#unstable). This includes importing the key and BPM analyzed by Rekordbox, and comments and colors for tracks, cues and loops. **We have to be clear however:** this feature *only* reads Rekordbox prepared removable devices, such as USB flash drives or external hard drives. It *will not* read your locally stored Rekordbox collection if you also have Rekordbox installed. The main Rekordbox database (both for Rekordbox 5 and Rekordbox 6) use completely different formats from the USB drives, so reading those databases would be a whole other project.

## Importing from Rekordbox to Mixxx

After you have exported music to a USB drive in Rekordbox, simply plug it in while Mixxx is running. Click on Rekordbox in the library, and all USB drives prepared with Rekordbox will be visible (attach as many as you like!). Then click on the desired removable device, and all your folders and playlists that you have so tirelessly prepared will be revealed for you to play from.

![Mixxx showing a Rekordbox USB library]({static}/images/news/mixxx-rekordbox-usb.png)

Some notes to keep in mind on how Rekordbox hotcues, memory cues, and loops are imported: Mixxx currently has one main cue point, one loop, and 38 hotcues. As such, all Rekordbox hotcues are mapped to Mixxx hotcues as expected, the first chronological Rekordbox memory cue is mapped to the Mixxx main cue, and the first chronological Rekordbox loop mapped to the Mixxx loop. All loops (including the first loop), and all subsequent Rekordbox memory cues are appended as Mixxx hotcues following the previously imported Rekordbox hotcues. A little confusing? Perhaps, but hopefully it will all make sense when you give it a whirl. Rest assured the hotcue and memory cue colors you assigned in Rekordbox are also imported, assisting in distinguishing between them. Also note that whilst the additional imported Rekordbox loops only appear in Mixxx 2.3 as hotcues, their loop details are preserved, ready for the multiple loop feature proposed for Mixxx 2.4!

![Rekordbox USB library]({static}/images/news/rekordbox-6-usb.png)![Mixxx showing a Rekordbox USB library]({static}/images/news/mixxx-rekordbox-usb.png)

Also note that as with the Serato library feature{# TODO: Add link to serato blogpost #}, we have tried our best to mitigate against certain edge cases of audio files encoded in lossy formats (MP3 and AAC/MP4), where different software's decoders can interpret conflicting timing information, leading to shifted cue points and beatgrids. We hope these are all correct, but some cases may be milliseconds off, and if you find any of these, please let us know on [Zulip](https://mixxx.zulipchat.com).

We probably didn't get every case perfect, so we have added some buttons by the beatgrid editing buttons to shift all cue points in a track by 10 ms (left click) or 1 ms (right click) so you can correct the timing yourself. This only shifts cue points, not the beatgrid (because the same problem happens with Serato and Mixxx does not yet import the beatgrid from Serato). If you want to shift the beatgrid too, you can shift the cue points, then go to a cue point and press the beatgrid shift button.

![Mixxx showing a Rekordbox USB library and beatgrid adjustment buttons]({static}/images/news/mixxx-rekordbox-usb-beatgrid.png)

## Can I prepare a Rekordbox removable device from Mixxx to use in a CDJ?

Sadly no, however this would be super cool! If you are so inclined to look at how to implement this and contribute back to Mixxx, it would be most welcome. A great to place to start would be looking into [Kaitai Struct serialization](https://doc.kaitai.io/faq.html#writing) which is a prerequisite for writing the [PDB file format](https://github.com/Deep-Symmetry/crate-digger/blob/master/src/main/kaitai/rekordbox_pdb.ksy).

## Shoutouts

As is often the case in open-source, the development of this new functionality was not possible without input from others. The new Mixxx Rekordbox removable device library feature builds upon the hard work already completed by [Deep Symmetry](https://github.com/Deep-Symmetry) for the [Crate Digger](https://github.com/Deep-Symmetry/crate-digger) library and [Pedro Estrela's](https://github.com/pestrela) [research about MP3 timing shifts](https://github.com/digital-dj-tools/dj-data-converter/issues/3) for [DJ Data Converter](https://github.com/digital-dj-tools/dj-data-converter). Kudos and keep up the great work!

## Future work: CDJs as Mixxx controllers

On a related note, we have [started reverse engineering the HID protocol for the Pioneer CDJ 2000 NXS2](https://mixxx.zulipchat.com/#narrow/stream/113295-controller-mapping/topic/Pioneer.20CDJ-2000NXS2). In future versions of Mixxx this would allow you to plug your laptop using Mixxx into CDJs via a USB cable and use your Mixxx library with the CDJs without needing Rekordbox at all. With the release of Rekordbox 6.0, this feature is now restricted in Rekordbox to customers paying a subscription fee, but [Mixxx is free](/news/2020-05-22-you-dont-need-to-pay-for-mixxx) and unlike Rekordbox, Mixxx runs on Linux. You could even add another controller to a CDJ setup to control other Mixxx features such as an [Allen & Heath Xone K2](https://github.com/mixxxdj/mixxx/wiki/Allen-&-Heath-Xone-K2-K1) for full control of Mixxx's effects while using CDJs!

![Pioneer CDJ 2000 NXS2 proof of concept]({static}/images/news/IMG_4627.JPG)

We have [documented what we have learned about the protocol so far](https://mixb.me/CDJHidProtocol/hid-analysis/startup.html) but there is still more to reverse engineer. After that, it will be more work to write a Mixxx HID controller mapping. If you have a CDJ 2000 NXS 2 or other CDJ model and want to get involved in this reverse engineering effort, [introduce yourself on our Zulip chat](https://mixxx.zulipchat.com/#narrow/stream/109123-introduce-yourself) and let us know how you can help.
