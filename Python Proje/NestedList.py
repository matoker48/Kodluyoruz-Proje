a = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
def flat(x):
    for i in x:
        if type(i) in [list]:
            for b in flat(i):
                yield(b)
        else:
            yield(i)
list(flat(a))

q = [[1, 2], [3, 4], [5, 6, 7]]
l= list()
for i in q:
    l.append(i[::-1])
rvd = l[::-1]
rvd