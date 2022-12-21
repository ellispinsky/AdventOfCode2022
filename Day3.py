def solution():
    with open('Day3input.txt', 'r') as f:
        inpt = f.read().split("\n")
    vals = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    a = 0
    for i in inpt:
        second = i[len(i) // 2:] #first half of string
        first = i[:len(i) // 2] #second half of string
        intersection = set(first).intersection(set(second)) #find the intersection of the two sets
        for j in intersection:
            a += vals.index(j) + 1 #add the index of the intersection to a
    print(a)
solution()

ok = "a,b,c,d,e"
for a in ok:
    print(a.index("a"))

