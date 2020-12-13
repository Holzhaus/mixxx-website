title: The Mixxx Class Diagram
authors: Albert Santoni
date: 2010-08-16 04:59:00
tags: 1.8, 1.8.0, development
comments: no

[![Mixxx class diagram]({static}/images/news/lolclassdiagram.png)]({static}/images/news/lolclassdiagram.png)

**Sorry, I just had to post this.**

I'm scraping together a press kit for the new 1.8.0 website and I came across this awesome class diagram in the "[The Mixxx Paper](http://haste.dk/tue/articles/nime03-mixxx.pdf)".
Tue Haste Andersen presented Mixxx and that paper at a conference back in 2003, and this diagram represents Mixxx's internals at the time.
You're looking at a snapshot inside one of the earliest versions of Mixxx, which has since grown to be the world's most popular free DJ software.

The diagram you're looking at is a standard tool software engineers use called a *UML class diagram* , and it lets developers effectively communicate their ideas about code layout.
If we had to make a new UML class diagram for Mixxx in 2010, it'd probably cover one of the walls of my apartment.
Although the MixxxApp, ControlObject, EngineObject, and SoundSource classes still exist (!) and might even be recognizable from their original incarnations, pretty much everything else has changed drastically.

The Mixxx architecture has expanded to accommodate an arbitrary number of sound devices, MIDI controllers, and soon, and arbitrary number of decks.
 Good things are in store.
