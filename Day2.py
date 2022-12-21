def solution():
    with open('Day2input.txt', 'r') as f: #open input file
        inpt = [("ABC".index(i[0]), "XYZ".index(i[2])) for i in f.read().split("\n")]

        score = 0

        for i in inpt:
            score += i[1] + 1

            if i[0] == i[1]:
                score += 3
            elif (i[0] + 1) % 3 == i[1]:
                score += 6

        print(score)

        score = 0
        for i in inpt:
            score += 3 * i[1]
            score += (i[0] + i[1] + 2) % 3 + 1

        print(score)






solution()