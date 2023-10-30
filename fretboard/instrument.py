
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
        self.fret_dots_x,self.fret_dots_y = self.get_fret_dots(inst, str_notes)

    def get_fret_dots(self, inst, str_notes):
        
        y_mid = (len(self.str_notes)-1)/2
        self.fret_dots_x = [2.5 ,4.5 ,6.5 ,8.5 ,11.5 ,11.5 ,14.5 ,16.5 ,18.5 ,20.5]
        self.fret_dots_y = [y_mid]*len(self.fret_dots_x)
        self.fret_dots_y[4] = self.fret_dots_y[4]-1
        self.fret_dots_y[5] = self.fret_dots_y[5]-1
        return self.fret_dots_x,self.fret_dots_y
    
    def get_string_notes(self, inst, str_notes):
        default_notes = {
            'Guitar': ['E2', 'A2', 'D3', 'G3', 'B3', 'E4'],
            'Mandolin': ['G3', 'D4', 'A5', 'E5'],
            'Banjo': ['G4', 'D3', 'G3', 'B3', 'D4'],
        }
        self.str_notes = str_notes if inst == 'Custom' else default_notes.get(inst, [])
        
        return self.str_notes

    def fretboard(self, key=False, plot_flag=True, plot_style='Notes', open_flag=True, dot_flag=True):
        key_dict = key.keydict() if key else self.get_default_key_dict()
        fretboard = self.generate_fretboard_data(open_flag)

        if plot_flag:
            self.plot_fretboard(fretboard, key_dict, plot_style, open_flag, dot_flag)

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
            
        # ax.scatter(self.fret_dots_x, self.fret_dots_y, s=200, c='k', zorder=2)

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

        
    def chord_charts(self, chord, pos=0, stretch=4, inversion=0, max_strings=None, accidentals='Sharp', plot_style='Notes', 
                     open_flag=False, dot_flag=True, full_board=False):
        
        chord_notes = chord.chord_notes()[accidentals][0]
        chord_reqs = chord.chord_notes()[accidentals][1]
        chordlist = chord_notes[inversion:] + chord_notes[:inversion]
        chorddegs = chord.chord_notes()['Degrees'][inversion:] + chord.chord_notes()['Degrees'][:inversion]
    
        if max_strings is None or max_strings == False:
            max_strings = len(self.str_notes)
        
        if full_board == True:
            p0 = 1
            p1 = self.num_frets-stretch+1
        else:
            p0 = pos
            p1 = pos+1
            
        for pos in range(p0,p1):
            AllCombos = []
            # if pos == 0:
            #     stretch += 1
            # elif pos == 1:
            #     stretch -= 1

            # Create a sub fretboard with the available frets
            if open_flag == True and pos > 0:
                SubBoard = [string[0:1]+string[pos:pos+stretch] for string in self.fretboard(key=False, plot_flag=False, open_flag=True)[accidentals]]
            else:
                SubBoard = [string[pos:pos+stretch] for string in self.fretboard(key=False, plot_flag=False, open_flag=True)[accidentals]]

            # Create all possible fingerings
            ChordBoard = [[note for note in chordlist if note in string] or ['X'] for string in SubBoard]
            ChordBoard_inds = [[string.index(note) for note in chordlist if note in string] for string in SubBoard]

            # Find all combinations
            def multi_lists_find_all_combination(lists):
                com = [[]]
                for l in lists:
                    com = [c + [x] for c in com for x in l]
                return com

            for combo in multi_lists_find_all_combination(ChordBoard):
                for ii in range(0, max_strings - 3, 1):
                    if combo[ii] == chordlist[0]:
                        AllCombos.append(['X'] * ii + combo[ii:])

            # Start new list of passing combinations by finding the first chord with required notes
            for ci,combo in enumerate(AllCombos):
                combo_check =  all(item in combo for item in chord_reqs)
                if combo_check:
                    NewCombos = [combo]
                    break
                
            # Assemble all chords with required notes and eliminate duplicates
            for combo in AllCombos[ci:]:
                combo_check =  all(item in combo for item in chord_reqs)
                if combo != NewCombos[-1] and combo_check:
                    NewCombos.append(combo)

            # Plot all chord combos
            stringLabels = [String[:-1] for String in self.str_notes]
            nStrings = len(self.str_notes)

            # Plot Chord charts in subplot groups
            num_panels = int(14/(stretch*0.8))
            num_subplots = int(len(NewCombos)/num_panels)
            
            for subplot_index in range(num_subplots):
                fig, axs = plt.subplots(1, num_panels, figsize=(16, 3))
                # fig, axs = plt.subplots(1, num_panels, figsize=(int(stretch * 1 * num_panels), 3))
                
                for panel_index in range(num_panels):
                    combo_index = subplot_index * num_panels + panel_index
                    try:
                        combo = NewCombos[combo_index] 
                    except: 
                        break

                    ax = axs[panel_index]
                    ax.set_yticks(range(nStrings))
                    ax.set_yticklabels(stringLabels,fontsize=12)
                    ax.set_ylim([-0.5, nStrings - 0.5])
                    ax.spines[['right', 'top', 'bottom', 'left']].set_visible(False)
                    ax.set_xlim([pos-2, pos+stretch-1])
                    ax.set_xticks(range(pos-1,pos+stretch))
                    ax.set_xticklabels(range(pos-1,pos+stretch),fontsize=12)

                    for ii in range(nStrings):
                        ax.plot([pos - 1, pos + stretch - 1], [ii, ii], 'k', linewidth=2)

                    for ii in range(pos - 1, pos + stretch):
                        ax.plot([ii, ii], [0, nStrings - 1], 'k', linewidth=2)

                    for si, note in enumerate(combo):
                        try:
                            if note != 'X':
                                loc = SubBoard[si].index(note)
                                degind = chordlist.index(note)

                                if open_flag == True and loc == 0:
                                    ax.scatter([pos + loc - 1.5], [si], s=700, c='k', zorder=2)
                                    ax.scatter([pos + loc - 1.5], [si], s=500, c='w', zorder=2)
                                    if plot_style == 'Degrees':
                                        ax.text(pos + loc - 1.5, si, chorddegs[degind], c='k', horizontalalignment='center',
                                                verticalalignment='center', fontsize='large', fontweight='bold', zorder=3)
                                    elif plot_style == 'Notes':
                                        ax.text(pos + loc - 1.5, si, note, c='k', horizontalalignment='center',
                                                verticalalignment='center', fontsize='large', fontweight='bold', zorder=3)
                                else:
                                    ax.scatter([pos + loc - 1.5], [si], s=700, c='k', zorder=2)
                                    if plot_style == 'Degrees':
                                        ax.text(pos + loc - 1.5, si, chorddegs[degind], c='w', horizontalalignment='center',
                                                verticalalignment='center', fontsize='large', fontweight='bold', zorder=3)
                                    elif plot_style == 'Notes':
                                        ax.text(pos + loc - 1.5, si, note, c='w', horizontalalignment='center',
                                                verticalalignment='center', fontsize='large', fontweight='bold', zorder=3)
                            else:
                                if plot_style == 'Degrees':
                                    ax.text(pos - 1.5, si, 'X', c='k', horizontalalignment='center', verticalalignment='center',
                                            fontsize='xx-large', fontweight='bold', zorder=3)
                                elif plot_style == 'Notes':
                                    ax.text(pos - 1.5, si, 'X', c='k', horizontalalignment='center', verticalalignment='center',
                                            fontsize='xx-large', fontweight='bold', zorder=3)
                        except:
                            continue

                plt.show()

    def scale_charts(self, key, pos=0, stretch=5, plot_style='Notes', dot_flag=True):
        
        scale_notes = key.keydict()['KeyNotes']
        scale_intervals = key.keydict()['KeyIntervals']
        scale_degrees = key.keydict()['KeyNoteNums']
        print(scale_notes)
        print(any('b' in note for note in scale_notes))
        if any('b' in note for note in scale_notes):
            accidental = 'Flat'
        else:
            accidental = 'Sharp'
        
        if pos == 0:
            # stretch += 1
            SubBoard = [string[pos:pos+stretch] for string in self.fretboard(key, plot_flag=False, open_flag=True)[accidental]]
        else:
            SubBoard = [string[pos:pos+stretch] for string in self.fretboard(key, plot_flag=False, open_flag=False)[accidental]]

        ScaleBoard = [[note for note in scale_notes if note in string] for string in SubBoard]
        ScaleBoard_inds = [[string.index(note) for note in scale_notes if note in string] for string in SubBoard]

        # # Test for duplicates
        # for si in range(len(ScaleBoard[:-1])):
        #     string_test = ScaleBoard[si+1]
        #     for ni,note in enumerate(ScaleBoard[si]):
        #         note_ind = ScaleBoard_inds[si][ni]
        #         if note in string_test and string_test.index(note) < note_ind:
        #             ScaleBoard[si].remove(note)
        #             ScaleBoard_inds[si].remove(note_ind)

        # Plot scale shape
        stringLabels = [String[:-1] for String in self.str_notes]
        nStrings = len(self.str_notes)

        fig, ax = plt.subplots(1, 1, figsize=(6, 4))
        if pos == 0:
            ax.set_xlim([pos-1, pos+stretch+1])
            ax.set_xticks(range(pos,pos+stretch+1))
            ax.set_xticklabels(range(pos,pos+stretch+1),fontsize=12)
            for ii in range(nStrings):
                ax.plot([pos, pos + stretch], [ii, ii], 'k', linewidth=2)
            for ii in range(pos, pos + stretch + 1):
                ax.plot([ii, ii], [0, nStrings - 1], 'k', linewidth=2)
        else:
            ax.set_xlim([pos-2, pos+stretch-1])
            ax.set_xticks(range(pos-1,pos+stretch))
            ax.set_xticklabels(range(pos-1,pos+stretch),fontsize=12)
            for ii in range(nStrings):
                ax.plot([pos - 1, pos + stretch - 1], [ii, ii], 'k', linewidth=2)
            for ii in range(pos - 1, pos + stretch):
                ax.plot([ii, ii], [0, nStrings - 1], 'k', linewidth=2)
            
        ax.set_yticks(range(nStrings))
        ax.set_yticklabels(stringLabels,fontsize=12)
        ax.set_ylim([-0.5, nStrings - 0.5])
        ax.spines[['right', 'top', 'bottom', 'left']].set_visible(False)


        for si,string in enumerate(ScaleBoard):
            try:
                for ni,note in enumerate(string):
                    loc = ScaleBoard_inds[si][ni]
                    degind = scale_notes.index(note)

                    if pos==0 and loc == 0:
                        
                        if note == scale_notes[0]:
                            ax.scatter([pos + loc - 0.5], [si], s=700, c='r', zorder=2)
                        else:
                            ax.scatter([pos + loc - 0.5], [si], s=700, c='k', zorder=2)
                        ax.scatter([pos + loc - 0.5], [si], s=500, c='w', zorder=2)
                        if plot_style == 'Degrees':
                            ax.text(pos + loc - 0.5, si, scale_degrees[degind], c='k', horizontalalignment='center',
                                    verticalalignment='center', fontsize='large', fontweight='bold', zorder=3)
                        elif plot_style == 'Notes':
                            ax.text(pos + loc - 0.5, si, note, c='k', horizontalalignment='center',
                                    verticalalignment='center', fontsize='large', fontweight='bold', zorder=3)
                            
                    else:
                        
                        if note == scale_notes[0]:
                            ax.scatter([pos + loc - 0.5], [si], s=700, c='r', zorder=2)
                        else:
                            ax.scatter([pos + loc - 0.5], [si], s=700, c='k', zorder=2)
                            
                        if plot_style == 'Degrees':
                            ax.text(pos + loc - 0.5, si, scale_degrees[degind], c='w', horizontalalignment='center',
                                    verticalalignment='center', fontsize='large', fontweight='bold', zorder=3)
                        elif plot_style == 'Notes':
                            ax.text(pos + loc - 0.5, si, note, c='w', horizontalalignment='center',
                                    verticalalignment='center', fontsize='large', fontweight='bold', zorder=3)
            except:
                continue

        plt.show()