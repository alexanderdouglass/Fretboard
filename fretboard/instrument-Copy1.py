
# import matplotlib.pyplot as plt

# # Instrument Class - Defines an instrument object based on a list of input notes corresponding to strings
# class Instrument:
    
#     # import numpy as np
    
#     def __init__(self,inst,NumFrets,StrNotes=[]):
#         self.inst = inst
#         self.NumFrets = NumFrets
#         if inst == 'Guitar':
#             self.StrNotes = ['E2','A2','D3','G3','B3','E4']
#         elif inst == 'Mandolin':
#             self.StrNotes = ['G3','D4','A5','E5']
#         elif inst == 'Banjo':
#             self.StrNotes = ['G4','D3','G3','B3','D4']
#         elif inst == 'Custom':
#             self.StrNotes = StrNotes
        
        
#     def fretboard(self,Key=False,PlotFlag=True,PlotStyle='Notes',OpenFlag=True):
#         # Outputs a fretboard image
        
#         # Input a key object.
#         # If no key is input, display all of the notes, in sharp format
        
#         # PlotFlag can be:
#         #  -True: Plots turned on
#         #  -False: Plots turned off
#         # PlotStyle can be:
#         #  -Notes: Labels all notes with note names
#         #  -Degrees: Labels all notes with scale degrees
#         #  -Intervals: Labels all notes with intervals
#         #  -Solid: All notes just given as solid circles (Root in Red, all others black)

#         # Get key dictionary
#         NoteNums      = [ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 , 10 , 11 ]
#         AllInts       = ['R','m2','M2','m3','M3','P4','TT','P5','m6','M6','m7','M7']
#         AllNotesSharp = ['C','C#', 'D','D#', 'E', 'F','F#', 'G','G#', 'A','A#', 'B']
#         AllNotesFlat  = ['C','Db', 'D','Eb', 'E', 'F','Gb', 'G','Ab', 'A','Bb', 'B']
        
#         if Key == False:
#             keydict = { 'AllNotes':AllNotesSharp,
#                    'AllIntervals':AllInts,
#                    'KeyNotes':AllNotesSharp,
#                    'KeyIntervals':AllInts,
#                    'KeyNoteNums':NoteNums}
#         else:
#             keydict = Key.keydict()
        
#         # Define where notes lie on the fretboard
#         FretboardSharp = []
#         FretboardFlat = []
#         FretboardSharpNums = []
#         FretboardFlatNums = []
#         nStrings = len(self.StrNotes)
#         stringLabels = []
        
#         for String in self.StrNotes:
#             stringLabels.append(String[:-1])
#             try:
#                 OpenNote = AllNotesSharp.index(String[:-1])
#             except:
#                 OpenNote = AllNotesFlat.index(String[:-1])
#             NoteListSharp = AllNotesSharp[OpenNote:] + AllNotesSharp + AllNotesSharp
#             NoteListSharp = NoteListSharp[:self.NumFrets+1]
#             NoteListSharpNum = NoteListSharp.copy()
#             NoteListFlat  = AllNotesFlat[OpenNote:] + AllNotesFlat + AllNotesFlat
#             NoteListFlat  = NoteListFlat[:self.NumFrets+1]
#             NoteListFlatNum = NoteListFlat.copy()

#             num = int(String[-1])
#             for ii,note in enumerate(NoteListSharpNum):
#                 NoteListSharpNum[ii] = NoteListSharpNum[ii] + str(num)
#                 NoteListFlatNum[ii] = NoteListFlatNum[ii] + str(num)
#                 if note == 'B':
#                     num += 1
#             FretboardSharp.append(NoteListSharp)
#             FretboardFlat.append(NoteListFlat)
#             FretboardSharpNums.append(NoteListSharpNum)
#             FretboardFlatNums.append(NoteListFlatNum)

#         Fretboard = { 'Sharp':FretboardSharp , 
#                      'Flat':FretboardFlat , 
#                      'SharpNums':FretboardSharpNums , 
#                      'FlatNums':FretboardFlatNums }

#         if PlotFlag != False:
            
#             plt.figure(figsize = (15,3))
#             plt.rcParams.update({'font.size': 16})
#             plt.rcParams['font.family'] = 'serif'
#             plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']
#             for ii in range(nStrings):
#                 plt.plot([0,self.NumFrets],[ii,ii],'k',linewidth=2)
#             for ii in range(self.NumFrets+1):
#                 plt.plot([ii,ii],[0,nStrings-1],'k',linewidth=2)
#             if OpenFlag == True:
#                 plt.xlim([-1,self.NumFrets])
#             else:
#                 plt.xlim([0,self.NumFrets])
#             for spinepos in ['right', 'top', 'bottom', 'left']: 
#                 plt.gca().spines[spinepos].set_visible(False) 
#             plt.xticks(range(self.NumFrets+1),range(self.NumFrets+1))
#             plt.yticks(range(nStrings),stringLabels)
#             plt.ylim([-0.5,nStrings-0.5])
            
#             FretboardNotes = FretboardSharp.copy()
#             if PlotFlag == 'Key':
#                 NotesDict = keydict['KeyNotes']
#                 NumDict = keydict['KeyNoteNums']
#                 IntDict = keydict['KeyIntervals']
#                 print(NotesDict)
#                 print(IntDict)
#                 print(NumDict)
#                 combined = '\t'.join(NotesDict)
#                 if 'b' in combined:
#                     FretboardNotes = FretboardFlat.copy()
#             else:
#                 NotesDict = AllNotesSharp
#                 RootNote = ''
                
#             for si,stringFrets in enumerate(FretboardNotes):
#                 for nn,note in enumerate(NotesDict):
#                     indices = [i for i, x in enumerate(stringFrets) if x == note]
#                     for ii in indices:
#                         if PlotFlag == 'Key' and note == NotesDict[0] :
#                             plt.scatter([ii-0.5],[si],s=700,c='r',zorder=2)
#                         else:
#                             plt.scatter([ii-0.5],[si],s=700,c='k',zorder=2)
                            
#                         if PlotStyle == 'Degrees':
#                             plt.text(ii-0.5,si,nn+1, c='w', horizontalalignment='center', verticalalignment='center', fontsize='large', fontweight='bold',zorder=3)
#                         elif PlotStyle == 'Intervals':
#                             plt.text(ii-0.5, si, IntDict[nn], c='w', horizontalalignment='center', verticalalignment='center', fontsize='medium', fontweight='bold',zorder=3)
#                         elif PlotStyle == 'Notes':
#                             plt.text(ii-0.5, si, note, c='w', horizontalalignment='center', verticalalignment='center', fontsize='large', fontweight='bold',zorder=3)
            
#             plt.show()
        
#         return Fretboard

#     def chord_charts(self, chord, pos=0, stretch=4, inversion=0, max_strings=None, accidentals='Sharp', PlotStyle='Notes'):
#         if pos == 0:
#             stretch += 1

#         chord_notes = chord.chord_notes()[accidentals]
#         chordlist = chord_notes[inversion:] + chord_notes[:inversion]
#         chorddegs = chord.chord_notes()['Degrees'][inversion:] + chord.chord_notes()['Degrees'][:inversion]

#         if max_strings is None or max_strings == False:
#             max_strings = len(self.StrNotes)

#         # Create a list of possible fingerings
#         SubBoard = [string[pos:pos+stretch] for string in self.fretboard(Key=False, PlotFlag=False, OpenFlag=True)[accidentals]]

#         # Create all possible fingerings
#         ChordBoard = [[note for note in chordlist if note in string] or ['X'] for string in SubBoard]

#         # Find all combinations
#         def multi_lists_find_all_combination(lists):
#             com = [[]]
#             for l in lists:
#                 com = [c + [x] for c in com for x in l]
#             return com

#         AllCombos = []
#         for combo in multi_lists_find_all_combination(ChordBoard):
#             for ii in range(0, max_strings - 3, 1):
#                 if combo[ii] == chordlist[0]:
#                     AllCombos.append(['X'] * ii + combo[ii:])

#         NewCombos = [AllCombos[0]]
#         for combo in AllCombos[1:]:
#             if combo != NewCombos[-1]:
#                 NewCombos.append(combo)

#         # Plot all chord combos
#         OpenFlag = pos == 0

#         stringLabels = [String[:-1] for String in self.StrNotes]
#         nStrings = len(self.StrNotes)

#         for combo in NewCombos:
#             plt.figure(figsize=(stretch, 3))
#             plt.rcParams.update({'font.size': 16})
#             plt.rcParams['font.family'] = 'serif'
#             plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

#             for ii in range(nStrings):
#                 plt.plot([pos - 1, pos + stretch], [ii, ii], 'k', linewidth=2)

#             for ii in range(pos - 1, pos + stretch + 1):
#                 plt.plot([ii, ii], [0, nStrings - 1], 'k', linewidth=2)

#             if OpenFlag:
#                 plt.xlim([-1, stretch])
#             else:
#                 plt.xlim([pos - 1, pos + stretch])

#             for spinepos in ['right', 'top', 'bottom', 'left']:
#                 plt.gca().spines[spinepos].set_visible(False)
#             plt.xticks(range(pos, pos + stretch + 1))
#             plt.yticks(range(nStrings), stringLabels)
#             plt.ylim([-0.5, nStrings - 0.5])

#             for si, note in enumerate(combo):
#                 if note != 'X':
#                     loc = SubBoard[si].index(note)
#                     degind = chordlist.index(note)
#                     plt.scatter([pos + loc - 0.5], [si], s=700, c='k', zorder=2)

#                     if PlotStyle == 'Degrees':
#                         plt.text(pos + loc - 0.5, si, chorddegs[degind], c='w', horizontalalignment='center',
#                                  verticalalignment='center', fontsize='large', fontweight='bold', zorder=3)
#                     elif PlotStyle == 'Notes':
#                         plt.text(pos + loc - 0.5, si, note, c='w', horizontalalignment='center',
#                                  verticalalignment='center', fontsize='large', fontweight='bold', zorder=3)
#                 else:
#                     if PlotStyle == 'Degrees':
#                         plt.text(pos - 1.5, si, 'X', c='k', horizontalalignment='center', verticalalignment='center',
#                                  fontsize='large', fontweight='bold', zorder=3)
#                     elif PlotStyle == 'Notes':
#                         plt.text(pos - 1.5, si, 'X', c='k', horizontalalignment='center', verticalalignment='center',
#                                  fontsize='large', fontweight='bold', zorder=3)

#             plt.show()

import matplotlib.pyplot as plt
NoteNums      = [ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 , 10 , 11 ]
AllInts       = ['R','m2','M2','m3','M3','P4','TT','P5','m6','M6','m7','M7']
AllNotesSharp = ['C','C#', 'D','D#', 'E', 'F','F#', 'G','G#', 'A','A#', 'B']
AllNotesFlat  = ['C','Db', 'D','Eb', 'E', 'F','Gb', 'G','Ab', 'A','Bb', 'B']

class Instrument:
    def __init__(self, inst, num_frets, str_notes=None):
        self.inst = inst
        self.num_frets = num_frets
        self.str_notes = self.get_string_notes(inst, str_notes)

    def get_string_notes(self, inst, str_notes):
        default_notes = {
            'Guitar': ['E2', 'A2', 'D3', 'G3', 'B3', 'E4'],
            'Mandolin': ['G3', 'D4', 'A5', 'E5'],
            'Banjo': ['G4', 'D3', 'G3', 'B3', 'D4'],
        }
        return str_notes if inst == 'Custom' else default_notes.get(inst, [])

    def fretboard(self, key=None, plot_flag=True, plot_style='Notes', open_flag=True):
        key_dict = key.keydict() if key else self.get_default_key_dict()
        fretboard = self.generate_fretboard_data(open_flag)

        if plot_flag:
            self.plot_fretboard(fretboard, key_dict, plot_style, open_flag)

        return fretboard

    def get_default_key_dict(self):
        note_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
        intervals = ['R', 'm2', 'M2', 'm3', 'M3', 'P4', 'TT', 'P5', 'm6', 'M6', 'm7', 'M7']
        notes_sharp = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
        return {
            'AllNotes': notes_sharp,
            'AllIntervals': intervals,
            'KeyNotes': notes_sharp,
            'KeyIntervals': intervals,
            'KeyNoteNums': note_nums
        }

    def generate_fretboard_data(self, open_flag):
        note_sharp, note_flat, note_sharp_nums, note_flat_nums = [], [], [], []

        for string in self.str_notes:
            string_label = string[:-1]
            open_note_index = self.get_note_index(string[:-1], AllNotesSharp)
            note_list_sharp = self.generate_note_list(AllNotesSharp, open_note_index)
            note_list_sharp_num = [note + string[-1] for note in note_list_sharp]
            note_list_flat = self.generate_note_list(AllNotesFlat, open_note_index)
            note_list_flat_num = [note + string[-1] for note in note_list_flat]
            note_sharp.append(note_list_sharp)
            note_flat.append(note_list_flat)
            note_sharp_nums.append(note_list_sharp_num)
            note_flat_nums.append(note_list_flat_num)

        return {
            'Sharp': note_sharp,
            'Flat': note_flat,
            'SharpNums': note_sharp_nums,
            'FlatNums': note_flat_nums
        }

    def get_note_index(self, note, note_list):
        return getattr(self, note_list).index(note)

    def generate_note_list(self, note_list, open_index):
        note_sequence = getattr(self, note_list)
        return note_sequence[open_index:] + note_sequence + note_sequence[:self.num_frets + 1]

    def plot_fretboard(self, fretboard, key_dict, plot_style, open_flag):
        n_strings = len(self.str_notes)
        string_labels = [string[:-1] for string in self.str_notes]

        plt.figure(figsize=(15, 3))
        plt.rcParams.update({'font.size': 16})
        plt.rcParams['font.family'] = 'serif'
        plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

        for ii in range(n_strings):
            plt.plot([0, self.num_frets], [ii, ii], 'k', linewidth=2)

        for ii in range(self.num_frets + 1):
            plt.plot([ii, ii], [0, n_strings - 1], 'k', linewidth=2)

        plt.xlim([-1, self.num_frets]) if open_flag else plt.xlim([0, self.num_frets])

        for spinepos in ['right', 'top', 'bottom', 'left']:
            plt.gca().spines[spinepos].set_visible(False)

        plt.xticks(range(self.num_frets + 1), range(self.num_frets + 1))
        plt.yticks(range(n_strings), string_labels)
        plt.ylim([-0.5, n_strings - 0.5])

        fretboard_notes = fretboard['Sharp']

        if plot_style == 'Key':
            notes_dict = key_dict['KeyNotes']
            num_dict = key_dict['KeyNoteNums']
            int_dict = key_dict['KeyIntervals']
            combined = '\t'.join(notes_dict)
            if 'b' in combined:
                fretboard_notes = fretboard['Flat']
        else:
            notes_dict = self.AllNotesSharp
            root_note = ''

        for si, string_frets in enumerate(fretboard_notes):
            for nn, note in enumerate(notes_dict):
                indices = [i for i, x in enumerate(string_frets) if x == note]
                for ii in indices:
                    color = 'r' if note == notes_dict[0] else 'k'
                    plt.scatter([ii - 0.5], [si], s=700, c=color, zorder=2)

                    if plot_style == 'Degrees':
                        plt.text(ii - 0.5, si, nn + 1, c='w', horizontalalignment='center',
                                 verticalalignment='center', fontsize='large', fontweight='bold', zorder=3)
                    elif plot_style == 'Intervals':
                        plt.text(ii - 0.5, si, int_dict[nn], c='w', horizontalalignment='center',
                                 verticalalignment='center', fontsize='medium', fontweight='bold', zorder=3)
                    elif plot_style == 'Notes':
                        plt.text(ii - 0.5, si, note, c='w', horizontalalignment='center',
                                 verticalalignment='center', fontsize='large', fontweight='bold', zorder=3)

        plt.show()

        
        
    def chord_charts(self, chord, pos=0, stretch=4, inversion=0, max_strings=None, accidentals='Sharp', PlotStyle='Notes'):
        if pos == 0:
            stretch += 1

        chord_notes = chord.chord_notes()[accidentals]
        chordlist = chord_notes[inversion:] + chord_notes[:inversion]
        chorddegs = chord.chord_notes()['Degrees'][inversion:] + chord.chord_notes()['Degrees'][:inversion]

        if max_strings is None or max_strings == False:
            max_strings = len(self.StrNotes)

        # Create a list of possible fingerings
        SubBoard = [string[pos:pos+stretch] for string in self.fretboard(Key=False, PlotFlag=False, OpenFlag=True)[accidentals]]

        # Create all possible fingerings
        ChordBoard = [[note for note in chordlist if note in string] or ['X'] for string in SubBoard]

        # Find all combinations
        def multi_lists_find_all_combination(lists):
            com = [[]]
            for l in lists:
                com = [c + [x] for c in com for x in l]
            return com

        AllCombos = []
        for combo in multi_lists_find_all_combination(ChordBoard):
            for ii in range(0, max_strings - 3, 1):
                if combo[ii] == chordlist[0]:
                    AllCombos.append(['X'] * ii + combo[ii:])

        NewCombos = [AllCombos[0]]
        for combo in AllCombos[1:]:
            if combo != NewCombos[-1]:
                NewCombos.append(combo)

        # Plot all chord combos
        OpenFlag = pos == 0

        stringLabels = [String[:-1] for String in self.StrNotes]
        nStrings = len(self.StrNotes)

        for combo in NewCombos:
            plt.figure(figsize=(stretch, 3))
            plt.rcParams.update({'font.size': 16})
            plt.rcParams['font.family'] = 'serif'
            plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

            for ii in range(nStrings):
                plt.plot([pos - 1, pos + stretch], [ii, ii], 'k', linewidth=2)

            for ii in range(pos - 1, pos + stretch + 1):
                plt.plot([ii, ii], [0, nStrings - 1], 'k', linewidth=2)

            if OpenFlag:
                plt.xlim([-1, stretch])
            else:
                plt.xlim([pos - 1, pos + stretch])

            for spinepos in ['right', 'top', 'bottom', 'left']:
                plt.gca().spines[spinepos].set_visible(False)
            plt.xticks(range(pos, pos + stretch + 1))
            plt.yticks(range(nStrings), stringLabels)
            plt.ylim([-0.5, nStrings - 0.5])

            for si, note in enumerate(combo):
                if note != 'X':
                    loc = SubBoard[si].index(note)
                    degind = chordlist.index(note)
                    plt.scatter([pos + loc - 0.5], [si], s=700, c='k', zorder=2)

                    if PlotStyle == 'Degrees':
                        plt.text(pos + loc - 0.5, si, chorddegs[degind], c='w', horizontalalignment='center',
                                 verticalalignment='center', fontsize='large', fontweight='bold', zorder=3)
                    elif PlotStyle == 'Notes':
                        plt.text(pos + loc - 0.5, si, note, c='w', horizontalalignment='center',
                                 verticalalignment='center', fontsize='large', fontweight='bold', zorder=3)
                else:
                    if PlotStyle == 'Degrees':
                        plt.text(pos - 1.5, si, 'X', c='k', horizontalalignment='center', verticalalignment='center',
                                 fontsize='large', fontweight='bold', zorder=3)
                    elif PlotStyle == 'Notes':
                        plt.text(pos - 1.5, si, 'X', c='k', horizontalalignment='center', verticalalignment='center',
                                 fontsize='large', fontweight='bold', zorder=3)

            plt.show()