import json

from mido import MidiFile


def read_messages(filename):
    mid = MidiFile(filename)

    for i, track in enumerate(mid.tracks):
        print('Track {}: {}'.format(i, track.name))
        for msg in track:
            print(msg)


def ad2_to_gm(note):
    with open("maps/ad2_parsed.json") as f:
        ad2_parsed = json.load(f)
    return ad2_parsed[str(note)]
