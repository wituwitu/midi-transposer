import sys

from mido import MidiFile, MidiTrack, Message

from utils import ad2_to_gm

if len(sys.argv) < 1:
    print("Usage: py transposer.py filename")

filename = sys.argv[1]
mid = MidiFile(filename)

outfile = MidiFile()
meta_track = MidiTrack()
out_track = MidiTrack()
outfile.tracks.append(meta_track)
outfile.tracks.append(out_track)

for i, track in enumerate(mid.tracks):
    print(f'Track {i}: {track.name}')
    for msg in track:
        if i == 0:
            print(msg)
            meta_track.append(msg)
        else:
            if msg.is_meta:
                out_track.append(msg)
                print(msg)
            else:
                out_track.append(Message(type=msg.type,
                                         channel=9,
                                         note=ad2_to_gm(msg.note),
                                         velocity=msg.velocity,
                                         time=msg.time*20))     # Why 20 XD

outfile.save('result.mid')
