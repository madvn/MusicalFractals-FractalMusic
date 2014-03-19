from music21 import *
us = environment.UserSettings()
#us.create() # run only the first time to create the file, then commented
s = us.getSettingsPath()
print s+'\n'
print sorted(us.keys())

bwv261 = corpus.parse('bach/bwv261')

notes = bwv261.flat.notes

diff = []
noteList = []
for index,items in enumerate(notes):
    print str(items.diatonicNoteNum)+'---'+str(items.frequency)+'---'+str(items.fullName)+'---'+str(items.duration.type)
    if index != len(notes)-1:
        diff.append(notes[index+1].frequency - items.frequency)
        noteList.append(items.diatonicNoteNum)

print \
      """

        Total number of notes --------->>> """ , len(notes),"\n"
