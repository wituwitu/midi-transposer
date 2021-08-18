# midi-transposer

This project transposes notes from a MIDI file using a certain map. It's configured to transpose notes in channel 10
(percussion) but can be configured to other channels.

I felt the need to do this since is tedious to map the MIDI notes from Addictive Drums 2 (or other drum VSTs) to the
General MIDI map (in order to write sheet music using MIDI).

This project uses the [mido](https://github.com/mido/mido) Python library.