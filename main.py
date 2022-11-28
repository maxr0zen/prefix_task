words_count = int(input())
mass = []
res = ''
for i in range(0, words_count):
    mass.append(input(str()))
prefix = mass[0]
for string in mass[1:]:
    while string[:len(prefix)] != prefix and prefix:
        prefix = prefix[len(prefix) - 1]
    if not prefix:
        break
print(prefix)