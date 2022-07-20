n = int(input())
cnt = 0

for i in range(n):
    c = 0
    word = input()
    a = len(word)
    for j in range(a-1):
        if word[j] != word[j+1]:
            new_word = word[j+1:]
            if new_word.count(word[j]) > 0:
                c = 1    
    if c == 0:
        cnt += 1

print(cnt)
            