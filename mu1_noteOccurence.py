#####################################################
#                                                   #
# Music21 - File3 - Madhavun Candadai               #
# Count number of occurences of note                #
#                                                   #
#####################################################
def cls():
    for i in range(1,40):
        print

cls()


from music21 import *
us = environment.UserSettings()
#us.create() # run only the first time to create the file, then commented
s = us.getSettingsPath()
#print s
#bwv261 = corpus.parse('mozart/k155')
bwv261 = corpus.parse('bach/bwv250')
#notes = bwv261.parts[0].flat.notes
notes = bwv261.flat.notes
diff = []
for k in range(0,len(notes)-1):
    #print len(notes)
    # t = bwv261.plot('histogram', 'pitch')
    checked = []
    notedist = []
    i = 0
    for index,items in enumerate(notes):
        if index != len(notes)-1:
            if items.isNote:
                notedist.append(items.diatonicNoteNum)

    if notedist[k] != 0:
        recurr = []
        n0 = notedist[k]

        notedist[k] = 0

        while n0 in notedist:
            indexis = notedist.index(n0) 
            recurr.append(indexis)
            notedist[indexis] = 0

        for i in range(1,len(recurr)):
            diff.append(recurr[i]-recurr[i-1])


diff.sort()
diff.reverse() 
