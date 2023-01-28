N = int(input())

words = []
for n in range(N):
    wd = input()
    if wd not in words:
        words.append(wd)

words_ascending = sorted(words)

words_by_length = sorted(words_ascending, key=lambda word: len(word))

print(*words_by_length, sep='\n')