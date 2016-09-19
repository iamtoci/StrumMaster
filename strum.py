<<<<<<< HEAD
=======
from time import perf_counter, sleep
>>>>>>> 89cd66123a94281ace3877eefc316052cc8f13ae
from random import choice
import numpy as np

class Song(object):
<<<<<<< HEAD
    '''Input is difficulty, output is a random strum pattern and random chord progression.'''
    def __init__(self, diff=1):

        self.key = choice(["A","C","D","E","G"])
=======

    def __init__(self, diff=1, mode_num=1):

        self.key = choice(["A","C","D","E","G"])
        self.mode_name, self.mode_intervals = self.modes(mode_num)
>>>>>>> 89cd66123a94281ace3877eefc316052cc8f13ae
        self.prog = self.progression(diff)
        self.timesig = None
        self.strum = self.strumpattern()
        self.notes = self.prog_notes()

    def strumpattern(self):
        timesignature = np.random.choice([3,4], size=1, p=[0.2, 0.8])[0]
        pattern3 = [("d","u","d"),("d","d","d"),("b_","du","du")]
        pattern4 = [("d","d","d","d"),("b","d","b","d"),("d_","du","_u","du"),
                    ("B_","DU","B_","DU"),("D_","DU","D_","DU")]
        if timesignature == 3:
            self.timesig = "3/4"
            return choice(pattern3)
        elif timesignature == 4:
            self.timesig = "4/4"
            return choice(pattern4)

    def progression(self, diff):
        progdict={
                1:[(1000,4000),(1000,5000),(1000,4000,5000),
                (1000,5000,4000),(1000,4000,1000,5000),
                (4000,1000,4000,5000),(1000,4000,5000,4000)],
                2:[(1000,6500,4000,5000),(1000,4000,5070),
                (1000,4000,1000,5070),(1000,5000,6500,4000),
                (1000,2500,4000,5000),(1000,2500,4000)],
                3:[(1000,6500,2500,4000,5070),(1000,6500,2500,5070,2500),
                (2570,5070,1000),(1000,4000,1000,5070,4000,1000),
                (1000,4000,7001,3500,6500,2500,5000,1000)]
                }
        return choice(progdict.get(diff))

<<<<<<< HEAD
    def prog_notes(self):
        '''returns notes in given chord progression'''
        major = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
        tonic = major.index(self.key)
        keyoftonic = [major[(tonic+i)%12] for i in range(7)]
=======
    def modes(self, mode_num):
        ionian = [2,2,1,2,2,2,1] #"TTSTTTS"
        intervals = [(ionian[i:]+ionian[:i])[:6] for i in range(len(ionian))]
        mode_name_lst = ["Ionian","Dorian","Phrygian","Lydian","Mixolydian",
                "Aeolian","Locrian"]
        return mode_name_lst[mode_num - 1], intervals[mode_num -1]

    def prog_notes(self):
        '''returns notes in given chord progression'''
        major = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"] #minor?
        tonic = major.index(self.key)
        keyoftonic = [major[(tonic+sum(self.mode_intervals[0:i]))%12] for i in range(7)]
>>>>>>> 89cd66123a94281ace3877eefc316052cc8f13ae
        #print(keyoftonic)
        notes = []
        for i in range(len(self.prog)):
            note = []
            for n in range(4):
                if n==0:
                    note.append(keyoftonic[(int(str(self.prog[i])[n])-1)%7])
                if n==1 and str(self.prog[i])[n]=="5":
                    note.append("m")
                if n==2 and str(self.prog[i])[n]!="0":
                    note.append(str(self.prog[i])[n])
                if n==3 and str(self.prog[i])[n]!="0":
                    if str(self.prog[i])[n]=="1":
                        note.append("dim")
                    if str(self.prog[i])[n]=="2":
                        note.append("sus")
            notes.append(''.join(note))
        return notes



if __name__=='__main__':
<<<<<<< HEAD
    diff = int(input("Choose Difficulty: 1, 2, or 3\n"))
    song1 = Song(diff=diff)
    print(song1.prog)
    print(song1.strum)
    print(song1.notes)
    print(song1.timesig)
=======

    song1 = Song(diff=1, mode_num=1)
    print(song1.mode_name)
    print(song1.prog)
    print(song1.strum)
    print(song1.notes)
>>>>>>> 89cd66123a94281ace3877eefc316052cc8f13ae
