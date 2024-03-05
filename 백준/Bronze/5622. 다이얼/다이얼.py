dials = input()

dialList = ['ABC', 'DEF', 'GHI', 'JKL', 'MNO', 'PQRS', 'TUV', 'WXYZ']
time = 0

for dial in dials:
    for i, el in enumerate(dialList):
        if dial in el:
            time += (i + 3)

print(time)