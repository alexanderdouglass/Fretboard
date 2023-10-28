
import matplotlib.pyplot as plt


class Instrument:
    def __init__(self, inst, num_frets, str_notes=[]):
        self.inst = inst
        self.num_frets       = num_frets
        self.str_notes       = self.get_string_notes(inst, str_notes)
        self.note_nums       = [ 0 ,  1 ,  2 ,  3 ,  4 ,  5 ,  6 ,  7 ,  8 ,  9 , 10 , 11 ]
        self.all_ints        = ['R','m2','M2','m3','M3','P4','TT','P5','m6','M6','m7','M7']
        self.all_notes_sharp = ['C','C#', 'D','D#', 'E', 'F','F#', 'G','G#', 'A','A#', 'B']
        self.all_notes_flat  = ['C','Db', 'D','Eb', 'E', 'F','Gb', 'G','Ab', 'A','Bb', 'B']

    def get_string_notes(self, inst, str_notes):
        default_notes = {
            'Guitar': ['E2', 'A2', 'D3', 'G3', 'B3', 'E4'],
            'Mandolin': ['G3', 'D4', 'A5', 'E5'],
            'Banjo': ['G4', 'D3', 'G3', 'B3', 'D4'],
        }
        self.str_notes = str_notes if inst == 'Custom' else default_notes.get(inst, [])
        
        return self.str_notes

    def fretboard(self, key=False, plot_flag=True, plot_style='Notes', open_flag=True):
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
        
        FretboardSharp = []
        FretboardFlat = []
        FretboardSharpNums = []
        FretboardFlatNums = []
        nStrings = len(self.str_notes)
        stringLabels = []
        
        for String in self.str_notes:
            stringLabels.append(String[:-1])
            try:
                OpenNote = self.all_notes_sharp.index(String[:-1])
            except:
                OpenNote = self.all_notes_flat.index(String[:-1])
            NoteListSharp = self.all_notes_sharp[OpenNote:] + self.all_notes_sharp + self.all_notes_sharp
            NoteListSharp = NoteListSharp[:self.num_frets+1]
            NoteListSharpNum = NoteListSharp.copy()
            NoteListFlat  = self.all_notes_flat[OpenNote:] + self.all_notes_flat + self.all_notes_flat
            NoteListFlat  = NoteListFlat[:self.num_frets+1]
            NoteListFlatNum = NoteListFlat.copy()

            num = int(String[-1])
            for ii,note in enumerate(NoteListSharpNum):
                NoteListSharpNum[ii] = NoteListSharpNum[ii] + str(num)
                NoteListFlatNum[ii] = NoteListFlatNum[ii] + str(num)
                if note == 'B':
                    num += 1
            FretboardSharp.append(NoteListSharp)
            FretboardFlat.append(NoteListFlat)
            FretboardSharpNums.append(NoteListSharpNum)
            FretboardFlatNums.append(NoteListFlatNum)

        return { 
            'Sharp':FretboardSharp , 
                     'Flat':FretboardFlat , 
                     'SharpNums':FretboardSharpNums , 
                     'FlatNums':FretboardFlatNums 
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

        if open_flag:
            plt.xlim([-1, self.num_frets])
        else:
            plt.xlim([0, self.num_frets])

        for spinepos in ['right', 'top', 'bottom', 'left']:
            plt.gca().spines[spinepos].set_visible(False)

        plt.xticks(range(self.num_frets + 1), range(self.num_frets + 1))
        plt.yticks(range(n_strings), string_labels)
        plt.ylim([-0.5, n_strings - 0.5])

        fretboard_notes = fretboard['Sharp']

        # if plot_style == 'Key':
        notes_dict = key_dict['KeyNotes']
        num_dict = key_dict['KeyNoteNums']
        int_dict = key_dict['KeyIntervals']
        combined = '\t'.join(notes_dict)
        if 'b' in combined:
            fretboard_notes = fretboard['Flat']
        # else:
        #     notes_dict = self.all_notes_sharp
        #     root_note = ''

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

        
    def chord_charts(self, chord, pos=0, stretch=4, inversion=0, max_strings=None, accidentals='Sharp', plot_style='Notes', open_flag = False):
        
        if pos == 0:
            stretch += 1

        chord_notes = chord.chord_notes()[accidentals]
        chordlist = chord_notes[inversion:] + chord_notes[:inversion]
        chorddegs = chord.chord_notes()['Degrees'][inversion:] + chord.chord_notes()['Degrees'][:inversion]

        if max_strings is None or max_strings == False:
            max_strings = len(self.str_notes)

        # Create a list of possible fingerings
        SubBoard = [string[pos:pos+stretch] for string in self.fretboard(key=False, plot_flag=False, open_flag=True)[accidentals]]

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
        stringLabels = [String[:-1] for String in self.str_notes]
        nStrings = len(self.str_notes)

        for combo in NewCombos:
            plt.figure(figsize=(stretch, 3))
            plt.rcParams.update({'font.size': 16})
            plt.rcParams['font.family'] = 'serif'
            plt.rcParams['font.serif'] = ['Times New Roman'] + plt.rcParams['font.serif']

            for ii in range(nStrings):
                plt.plot([pos - 1, pos + stretch], [ii, ii], 'k', linewidth=2)

            for ii in range(pos - 1, pos + stretch + 1):
                plt.plot([ii, ii], [0, nStrings - 1], 'k', linewidth=2)

            if open_flag:
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

                    if plot_style == 'Degrees':
                        plt.text(pos + loc - 0.5, si, chorddegs[degind], c='w', horizontalalignment='center',
                                 verticalalignment='center', fontsize='large', fontweight='bold', zorder=3)
                    elif plot_style == 'Notes':
                        plt.text(pos + loc - 0.5, si, note, c='w', horizontalalignment='center',
                                 verticalalignment='center', fontsize='large', fontweight='bold', zorder=3)
                else:
                    if plot_style == 'Degrees':
                        plt.text(pos - 1.5, si, 'X', c='k', horizontalalignment='center', verticalalignment='center',
                                 fontsize='large', fontweight='bold', zorder=3)
                    elif plot_style == 'Notes':
                        plt.text(pos - 1.5, si, 'X', c='k', horizontalalignment='center', verticalalignment='center',
                                 fontsize='large', fontweight='bold', zorder=3)

            plt.show()

