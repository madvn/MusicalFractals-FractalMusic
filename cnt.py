def cls():
    for i in range(1,40):
        print

cls()

tse1 = [1,1,2,4,5,2,5]
tse = tse1
cnt = []
i = 0
while len(tse) > 0:
	n0 = tse[0]
	cnt.append(1)
	del tse[tse.index(n0)]
	while n0 in tse:
		cnt[len(cnt)-1] += 1
		del tse[tse.index(n0)]
		print tse


print cnt
