

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
            'm11': ['1', 'b3', '5', 'b7', '11'],
            'dom11': ['1', '3', '5', 'b7', '11']
        }
        
        chord_degrees = chord_types.get(self.chord_type, [])
        sharp_notes = [all_notes_sharp[degree_trans[deg]] for deg in chord_degrees]
        flat_notes = [all_notes_flat[degree_trans[deg]] for deg in chord_degrees]

        return {'Sharp': sharp_notes, 'Flat': flat_notes, 'Degrees': chord_degrees}





# class Chord:
    
#     def __init__(self,chord,custom_input=[]):
        
#         # Detect if only a note is input and assign as major chord
#         if chord == 'custom' or chord == 'Custom':
#             ChordType = 'Custom'
#             RootNote = custom_input[0]
#         if len(chord) == 1 or chord[-1] in ['#','b','A','B','C','D','E','F','G']:
#             ChordType = 'Major'
#             RootNote = chord[0:1]
#         elif chord[1] in ['#','b']:
#             ChordType = chord[2:]
#             RootNote = chord[0:2]
#         else:
#             ChordType = chord[1:]
#             RootNote = chord[0:1]
            
#         self.root = RootNote
#         self.type = ChordType
            

#     def chord_notes(self):
#     # def chord_notes(chord=False,key=False,custom=False,custom_input=[]):
        
#     # Defines all of the relevant chords for a given key and provides list of notes?
#     # Option to plot them in musical notation?
#     # Inversion options?
#     # Input option examples:
#         # Custom: 'Custom' or 'custom', custom_input = [G C E] 
#         # Major: 'G','Bb','GM','AMajor'
#         # Minor: 'Gm','Bbm','Aminor'
#         # Five chord: 'G5','Bb5'
#         # Seven chord: 'G7','Bb7'
#         # Major Seven chord: 'Bbmaj7'
#         # Minor Seven chord: 'Bbmin7','Bbm7'
#         # Diminished chord: 'Bbdim'
#         # Diminished seven chord: 'Bbdim7'
#         # Augmented chord: 'Bbaug'
#         # Sus2 chord: 'Bbsus2'
#         # Minor Sus2 chord: 'Bbmsus2'
#         # Sus4 chord: 'Bbsus4'
#         # Minor Sus4 chord: 'Bbmsus4'
#         # add9 chord: 'Bbadd9'
#         # add11 chord: 'Bbadd11'
#         # Six chord: 'Bb6'
#         # Minor Six chord: 'Bbm6'
#         # Nine chord: 'Bb9'
#         # Minor Nine chord: 'Bbm9'
#         # Major Nine chord: 'Bbmaj9'
#         # Eleven chord: 'Bb11'
#         # Minor Eleven chord: 'Bbm11'
#         # Thirteen chord: 'Bb13'
#         # Minor Thirteen chord: 'Bbm13'
#         # Major Thirteen chord: 'Bbmaj13'
        
#         AllNoteNums   = [ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 , 10 ,  11]
#         AllInts       = ['R','m2','M2','m3','M3','P4','TT','P5','m6','M6','m7','M7']
#         AllNotesSharp = ['C','C#', 'D','D#', 'E', 'F','F#', 'G','G#', 'A','A#', 'B']
#         AllNotesFlat  = ['C','Db', 'D','Eb', 'E', 'F','Gb', 'G','Ab', 'A','Bb', 'B']
        
#         DegreeTrans   = { '1': 0,
#                          '#1': 1,
#                          'b2': 1,
#                          '2': 2,
#                          '#2': 3,
#                          'b3': 3,
#                          '3': 4,
#                          '#3': 5,
#                          '4': 5,
#                          '#4': 6,
#                          'TT': 6,
#                          'b5': 6,
#                          '5': 7,
#                          '#5': 8,
#                          'b6': 8,
#                          '6': 9,
#                          '#6': 10,
#                          'b7': 10,
#                          '7': 11,
#                          'b9': 1,
#                          '9': 2,
#                          '#9': 3,
#                          'b11': 4,
#                          '11': 5,
#                          '#11': 6}
        
#         # Reorder so proper root note starts the lists
#         try:
#             keyShift = AllNotesSharp.index(self.root)
#         except:
#             keyShift = AllNotesFlat.index(self.root)
#         if keyShift > 0:
#             AllNotesSharp = AllNotesSharp[keyShift:] + AllNotesSharp[0:keyShift]
#             AllNotesFlat  = AllNotesFlat[keyShift:] + AllNotesFlat[0:keyShift]
            
#         # Define all chord types of interest
#         if self.type == 'Major' or self.type == 'M' or self.type == 'major':
#             ChordDegs = ['1','3','5']
#             ChordPriority = ['1','3','5']
            
#         if self.type == 'Minor' or self.type == 'm' or self.type == 'minor':
#             ChordDegs = ['1','b3','5']
#             ChordPriority = ['1','b3','5']
            
#         if self.type == '5':
#             ChordDegs = ['1','5']
#             ChordPriority = ['1','5']
        
#         if self.type == '7' or self.type == 'dom7' or self.type == 'Dom7':
#             ChordDegs = ['1','3','5','b7']
#             ChordPriority = ['1','b7','3','5']
            
#         if self.type == 'maj7' or self.type == 'Major7' or self.type == 'major7':
#             ChordDegs = ['1','3','5','7']
#             ChordPriority = ['1','7','3','5']
            
#         if self.type == 'm7' or self.type == 'Minor7' or self.type == 'minor7':
#             ChordDegs = ['1','b3','5','b7']
#             ChordPriority = ['1','b7','b3','5']
            
#         if self.type == 'dim' or self.type == 'Dim':
#             ChordDegs = ['1','b3','b5']
#             ChordPriority = ['1','b3','b5']
            
#         if self.type == 'dim7' or self.type == 'Dim7':
#             ChordDegs = ['1','b3','b5','6']
#             ChordPriority = ['1','6','b3','b5']
            
#         if self.type == 'sus2':
#             ChordDegs = ['1','2','3','5']
#             ChordPriority = ['1','2','3','5']
            
#         if self.type == 'msus2':
#             ChordDegs = ['1','2','b3','5']
#             ChordPriority = ['1','2','b3','5']
            
#         if self.type == 'sus4':
#             ChordDegs = ['1','3','4','5']
#             ChordPriority = ['1','3','4','5']
            
#         if self.type == 'msus4':
#             ChordDegs = ['1','b3','4','5']
#             ChordPriority = ['1','b3','4','5']
            
#         if self.type == 'add9':
#             ChordDegs = ['1','3','5','9']
#             ChordPriority = ['1','9','3','5']
            
#         if self.type == 'add11':
#             ChordDegs = ['1','3','5','11']
#             ChordPriority = ['1','11','3','5']
            
#         if self.type == 'aug' or self.type == 'Aug':
#             ChordDegs = ['1','3','TT']
#             ChordPriority = ['1','TT','3']
            
#         if self.type == '6':
#             ChordDegs = ['1','3','5','6']
#             ChordPriority = ['1','6','3','5']
            
#         if self.type == 'm6':
#             ChordDegs = ['1','b3','5','b6']
#             ChordPriority = ['1','b6','b3','5']
            
#         if self.type == '9' or self.type == 'dom9':
#             ChordDegs = ['1','3','5','b7','9']
#             ChordPriority = ['1','9','b7','3','5']
            
#         if self.type == 'm9':
#             ChordDegs = ['1','b3','5','b7','9']
#             ChordPriority = ['1','9','b7','b3','5']
        
#         if self.type == 'maj9':
#             ChordDegs = ['1','3','5','7','9']
#             ChordPriority = ['1','9','7','3','5']
        
# #         if self.type == '11':
# #             ChordDegs = ['1','3','5']
# #             ChordPriority = ['1','3','5']
            
#         if self.type == 'm11':
#             ChordDegs = ['1','b3','5','b7','9','11']
#             ChordPriority = ['1','11','9','b7','b3','5']
            
#         if self.type == '11' or self.type == 'maj11':
#             ChordDegs = ['1','3','5','7','9','11']
#             ChordPriority = ['1','11','9','7','3','5']
            
        
#         SharpNotes = [AllNotesSharp[ DegreeTrans[deg] ] for deg in ChordDegs]
#         FlatNotes = [AllNotesFlat[ DegreeTrans[deg] ] for deg in ChordDegs]
#         ChordNotes = { 'Sharp':SharpNotes, 'Flat':FlatNotes, 'Degrees':ChordDegs, 'Priority': ChordPriority }
        
#         return ChordNotes