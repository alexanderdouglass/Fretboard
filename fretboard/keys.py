        
class Key:
    def __init__(self, note, mode):
        self.note = note
        self.mode = mode

    def keydict(self):
        all_note_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        all_ints = ['R', 'm2', 'M2', 'm3', 'M3', 'P4', 'TT', 'P5', 'm6', 'M6', 'm7', 'M7']
        all_notes_sharp = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        all_notes_flat = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']

        key_shift = all_notes_sharp.index(self.note) if self.note in all_notes_sharp else all_notes_flat.index(self.note)

        all_notes_sharp = all_notes_sharp[key_shift:] + all_notes_sharp[:key_shift]
        all_notes_flat = all_notes_flat[key_shift:] + all_notes_flat[:key_shift]

        mode_definitions = {
            'Ionian': [0, 2, 4, 5, 7, 9, 11],
            'Major': [0, 2, 4, 5, 7, 9, 11],
            'Dorian': [0, 2, 3, 5, 7, 9, 10],
            'Phrygian': [0, 1, 3, 5, 7, 8, 10],
            'Lydian': [0, 2, 4, 6, 7, 9, 11],
            'Mixolydian': [0, 2, 4, 5, 7, 9, 10],
            'Aeolian': [0, 2, 3, 5, 7, 8, 10],
            'Minor': [0, 2, 3, 5, 7, 8, 10],
            'Locrian': [0, 1, 3, 5, 6, 8, 10],
            'Harmonic Minor': [0, 2, 3, 5, 8, 8, 11]
        }

        note_nums = mode_definitions.get(self.mode, [])
        sharp_notes = [all_notes_sharp[i][0:1] for i in note_nums]
        if len(sharp_notes) == len(set(sharp_notes)):
            key_notes = [all_notes_sharp[i] for i in note_nums]
        else:
            key_notes = [all_notes_flat[i] for i in note_nums]
        
        all_notes = all_notes_sharp if key_notes[0][-1] != 'b' else all_notes_flat
        key_ints = [all_ints[i] for i in note_nums]

        keydict = {
            'AllNotes': all_notes,
            'AllIntervals': all_ints,
            'KeyNotes': key_notes,
            'KeyIntervals': key_ints,
            'KeyNoteNums': note_nums
        }

        return keydict
