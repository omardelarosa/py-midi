import numpy as np
from pypianoroll import Multitrack, Track, metrics
from matplotlib import pyplot as plt
from img import load_array_from_image

MIDI_FILE_PATH = 'midi/bach/inventions/invent1.midi'
IMAGE_FILE_PATH = 'images/t_10.png'
IMAGE_MIDI_OUT_FILE_PATH = './midi/outfile.mid'


def plot_multitrack(mt):
    fig, axs = mt.plot()
    plt.show()


def write_multitrack_to_midi_file(mt, filename):
    mt.write(filename)


def midi_from_image(image_filename, midi_outfilename):
    arr = load_array_from_image(image_filename)
    THRESHOLD = 0.25  # threshold amount to register note

    # Example pianoroll loading
    # pianoroll = np.zeros((96, 128))
    # C_maj = [60, 64, 67, 72, 76, 79, 84]
    # pianoroll[0:95, C_maj] = 100
    mask = arr > THRESHOLD
    arr[mask] = 0
    pianoroll = np.uint8(arr * 100)
    # print(arr)

    track = Track(pianoroll=pianoroll, program=0, is_drum=False,
                  name='t_10')

    multitrack = Multitrack(tracks=[track],
                            tempo=120.0,
                            # downbeat=[0, 96, 192, 288],  #
                            beat_resolution=4)
    # plot_multitrack(multitrack)
    write_multitrack_to_midi_file(multitrack, midi_outfilename)


def determine_key_of_midi(midi_filename):
    # Parse a MIDI file to a `pypianoroll.Multitrack` instance
    multitrack = Multitrack(midi_filename)
    for t in multitrack.tracks:
        pianoroll = t.pianoroll
        pitch_classes = set()
        # Ignore key of drum pattern
        if not t.is_drum:
            # print("track: ", t.pianoroll)
            p = metrics.n_pitche_classes_used(pianoroll)
            pitch_classes.add(p)
        # print("pitch classes: ", pitch_classes)
        if len(pitch_classes) == 1:
            # Return first pitch in class
            for pitch in pitch_classes:
                return pitch
        else:
            print("Warning: multiple pitch classes detected in file: ", pitch_classes)
            return None


pitch = determine_key_of_midi(MIDI_FILE_PATH)
print("Pitch: ", pitch)
# midi_from_image(IMAGE_FILE_PATH, IMAGE_MIDI_OUT_FILE_PATH) # turn image into midi
