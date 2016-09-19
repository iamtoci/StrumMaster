from random import choice
import numpy as np

class Song(object):
    '''Input is difficulty, output is a random strum pattern and random chord progression.'''

    def __init__(self, diff=1):

        self.key = choice(["A","C","D","E","G"])
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

    def prog_notes(self):
        '''returns notes in given chord progression'''
        major = ["A","A#","B","C","C#","D","D#","E","F","F#","G","G#"]
        tonic = major.index(self.key)
        keyoftonic = [major[(tonic+i)%12] for i in range(7)]
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
    diff = int(input("Choose Difficulty: 1, 2, or 3\n"))
    song1 = Song(diff=diff)
    print(song1.prog)
    print(song1.strum)
    print(song1.notes)
    print(song1.timesig)
