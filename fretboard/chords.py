

# Key class takes an input key and outputs an object with all of that key's information.

class Chord:
    def __init__(self, chord, custom_input=[]):
        if chord.lower() == 'custom':
            self.chord_type = 'Custom'
            self.root_note = custom_input[0]
        else:
            chord_info = self.parse_chord(chord)
            self.chord_type, self.root_note = chord_info

    def parse_chord(self, chord):
        # A helper function to parse the chord and return the chord type and root note.
        valid_chord_types = [
            'major', 'Major', 'M', 'Minor', 'm', 'minor', '5', '7', 'dom7', 'Dom7', 'maj7', 'major7', 'Major7', 'minor7', 'Minor7',               'm7', 'dim', 'Dim', 'dim7', 'Dim7','aug', 'Aug', 'sus2', 'msus2', 'sus4', 'msus4', 'add9', 'add11', '6', 'm6', '9',                   'dom9', 'm9', 'maj9', '11', 'dom11', 'm11'
        ]

        if len(chord) > 1:
            if chord[1] == '#' or chord[1] == 'b':
                chord_type = chord[2:]
                root_note = chord[0:2]
            else:
                chord_type = chord[1:]
                root_note = chord[0:1]
        else:
            chord_type = 'M'
            root_note = chord
            
        return chord_type, root_note

        return 'Major', chord  # Default to major chord

    def chord_notes(self):
        all_note_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        all_notes_sharp = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        all_notes_flat = ['C', 'Db', 'D', 'Eb', 'E', 'F', 'Gb', 'G', 'Ab', 'A', 'Bb', 'B']
        degree_trans = {
            '1': 0, 'b2': 1, '2': 2, 'b3': 3, '3': 4, '4': 5, 'b5': 6, '5': 7,
            'b6': 8, '6': 9, 'b7': 10, '7': 11, 'b9': 1, '9': 2, 'b11': 4, '11': 5
        }
        
        key_shift = all_notes_sharp.index(self.root_note) if self.root_note in all_notes_sharp else all_notes_flat.index(self.root_note)

        all_notes_sharp = all_notes_sharp[key_shift:] + all_notes_sharp[:key_shift]
        all_notes_flat = all_notes_flat[key_shift:] + all_notes_flat[:key_shift]

        chord_types = {
            'Major': ['1', '3', '5'],
            'major': ['1', '3', '5'],
            'M': ['1', '3', '5'],
            'Minor': ['1', 'b3', '5'],
            'minor': ['1', 'b3', '5'],
            'm': ['1', 'b3', '5'],
            '5': ['1', '5'],
            '7': ['1', '3', '5', 'b7'],
            'Dom7': ['1', '3', '5', 'b7'],
            'dom7': ['1', '3', '5', 'b7'],
            'major7': ['1', '3', '5', '7'],
            'Major7': ['1', '3', '5', '7'],
            'maj7': ['1', '3', '5', '7'],
            'Minor7': ['1', 'b3', '5', 'b7'],
            'minor7': ['1', 'b3', '5', 'b7'],
            'm7': ['1', 'b3', '5', 'b7'],
            'dim': ['1', 'b3', 'b5'],
            'Dim': ['1', 'b3', 'b5'],
            'dim7': ['1', 'b3', 'b5', '6'],
            'Dim7': ['1', 'b3', 'b5', '6'],
            'sus2': ['1', '2', '3', '5'],
            'msus2': ['1', '2', 'b3', '5'],
            'sus4': ['1', '3', '4', '5'],
            'msus4': ['1', 'b3', '4', '5'],
            'add9': ['1', '3', '5', '9'],
            'add11': ['1', '3', '5', '11'],
            'aug': ['1', '3', 'TT'],
            'Aug': ['1', '3', 'TT'],
            '6': ['1', '3', '5', '6'],
            'm6': ['1', 'b3', '5', '6'],
            '9': ['1', '3', '5', 'b7', '9'],
            'dom9': ['1', '3', '5', 'b7', '9'],
            'm9': ['1', 'b3', '5', 'b7', '9'],
            'maj9': ['1', '3', '5', '7', '9'],
            '11': ['1', '3', '5', '7', '9', '11'],
            'm11': ['1', 'b3', '5', 'b7', '9', '11'],
            'dom11': ['1', '3', '5', 'b7', '9', '11']
        }
        
        chord_reqs = {
            'Major': ['1', '3'],
            'major': ['1', '3'],
            'M': ['1', '3'],
            'Minor': ['1', 'b3'],
            'minor': ['1', 'b3'],
            'm': ['1', 'b3'],
            '5': ['1', '5'],
            '7': ['1', '3', 'b7'],
            'Dom7': ['1', '3', 'b7'],
            'dom7': ['1', '3', 'b7'],
            'major7': ['1', '3', '7'],
            'Major7': ['1', '3', '7'],
            'maj7': ['1', '3', '7'],
            'Minor7': ['1', 'b3', 'b7'],
            'minor7': ['1', 'b3', 'b7'],
            'm7': ['1', 'b3', 'b7'],
            'dim': ['1', 'b3', 'b5'],
            'Dim': ['1', 'b3', 'b5'],
            'dim7': ['1', 'b3', 'b5', '6'],
            'Dim7': ['1', 'b3', 'b5', '6'],
            'sus2': ['1', '2', '3', '5'],
            'msus2': ['1', '2', 'b3', '5'],
            'sus4': ['1', '3', '4', '5'],
            'msus4': ['1', 'b3', '4', '5'],
            'add9': ['1', '3', '5', '9'],
            'add11': ['1', '3', '5', '11'],
            'aug': ['1', '3', 'TT'],
            'Aug': ['1', '3', 'TT'],
            '6': ['1', '3', '6'],
            'm6': ['1', 'b3', '6'],
            '9': ['1', '3', 'b7', '9'],
            'dom9': ['1', '3', 'b7', '9'],
            'm9': ['1', 'b3', 'b7', '9'],
            'maj9': ['1', '3', '7', '9'],
            '11': ['1', '7', '9', '11'],
            'm11': ['1', 'b7', '9', '11'],
            'dom11': ['1', 'b7', '9', '11']
        }
        
        chord_degrees = chord_types.get(self.chord_type, [])
        chord_requirements = chord_reqs.get(self.chord_type, [])
        sharp_notes = [all_notes_sharp[degree_trans[deg]] for deg in chord_degrees]
        flat_notes = [all_notes_flat[degree_trans[deg]] for deg in chord_degrees]
        sharp_reqs = [all_notes_sharp[degree_trans[deg]] for deg in chord_requirements]
        flat_reqs = [all_notes_flat[degree_trans[deg]] for deg in chord_requirements]
        
        sharps = [sharp_notes,sharp_reqs]
        flats = [flat_notes,flat_reqs]

        return {'Sharp': sharps, 'Flat': flats, 'Degrees': chord_degrees}



