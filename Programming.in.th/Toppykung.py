n = int(input())
words = []
for i in range(n):
    word = input()
    if word not in words:
        words.append(word)

words.sort()

for word in words:
    print(word)