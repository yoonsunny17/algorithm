alphabets = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()

for alpha in alphabets:
    word = word.replace(alpha, '0')

print(len(word))