#####################################################
#                                                   #
# Music21 - File1 - Madhavun Candadai               #
# Creating and configuring user settings object     #
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
print s+'\n'
print sorted(us.keys())

#tinyNotation.TinyNotationStream("e4 e4 d4 c4 c4 d4 d4", "3/4").show()

#print (serial.rowToMatrix([2,1,9,10,5,3,4,0,8,7,6,11]) )

##
##streamObject = converter.parse(humdrum.testFiles.mazurka6)
##stream2 = streamObject.stripTies()
##correlated = graph.Plot3DBarsPitchSpaceQuarterLength(stream2.flat)
##correlated.process()
#print correlated.data

##bwv261 = corpus.parse('mozart/k155')
bwv261 = corpus.parse('bach/bwv261')
#bwv295.show()
##bwv295.plot
notes = bwv261.parts[0].flat.notes
diff = []
noteList = []
for index,items in enumerate(notes):
    print str(items.diatonicNoteNum)+'---'+str(items.frequency)+'---'+str(items.fullName)
    if index != len(notes)-1:
        diff.append(notes[index+1].frequency - items.frequency)
        noteList.append(items.diatonicNoteNum)

print \
      """

        Total number of notes --------->>> """ , len(notes),"\n"
##print diff
diff.sort()
diff.reverse()
##n0 = notes[0]
##del notes[0]
##
##print \
##      """
##        after deleting notes[0]
##        Total number of notes --------->>> """ , len(notes),"\n"
##notes.append(n0)
##
##print \
##      """
##        after appending n0
##        Total number of notes --------->>> """ , len(notes),"\n"

##for index in range(1,len(notes)):
    
diffCnt = []
while len(diff) > 0:
	n0 = diff[0]
	diffCnt.append(1)
	del diff[diff.index(n0)]
	while n0 in diff:
		diffCnt[len(diffCnt)-1] += 1
		del diff[diff.index(n0)]
##		print diff

diffCnt.sort()
diffCnt.reverse()
##print diffCnt

print noteList
notesCnt = []
while len(noteList) > 0:
	n0 = noteList[0]
	notesCnt.append(1)
	del noteList[noteList.index(n0)]
	while n0 in noteList:
		notesCnt[len(notesCnt)-1] += 1
		del noteList[noteList.index(n0)]
##		print diff

notesCnt.sort()
notesCnt.reverse()
print notesCnt
