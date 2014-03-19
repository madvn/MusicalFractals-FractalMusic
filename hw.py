# my first python program - Madhavun

###########################################################

def cls():
    for i in range(1,40):
        print

############################################################


import random

print \
      """hello########
                    ########world"""
a = 'Pie\n'
b = a *10
print b

print "2 + 24 / 5 % 2 = ",
print 2 + 24 / 5 % 2

name = raw_input ("enter your name - ")
print 'Hi,' + name.title() + ','
print 'or shd i say.. ' + name.replace("ad","BC")

#print '\nyour name\'s number equivalent is - ',
#print float(name)

num = raw_input('enter number - ')
#print 'your encoded number is ' + str(int(num)+10)
print 'your encoded number is ' , int(num)+10 , 'which is to be kept secret'

soln = random.randrange(100)
#print soln
cnt  = 1
guess = int(raw_input("guess the random number between 0 to 100 generated "))
while cnt < 5:
    if abs (guess-soln) < 25:
        print "You are close but not correct"
        cnt = cnt +1
        guess = int(raw_input("guess the random number between 0 to 100 generated "))
    if guess-soln > 25:
        print "You are far from soln"
        cnt = cnt + 1
        guess = int(raw_input("guess the random number between 0 to 100 generated "))
    if guess == soln:
        print "WOW!! you got it in", cnt , "attempts"
        cnt = 45

print 'the soln was ' , soln

for letter in name:
    print letter

high = len(name)
low = -len(name)
for i in range(10):
        position = random.randrange(low,high)
        print "word[",position,"]\t",name[position]



#########################################################
raw_input("\t\n Press enter to exit")

