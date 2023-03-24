# 서로 다른 부분 문자열의 개수

word = input()
word_len = len(word)

word_list = []
for part_len in range(1, word_len + 1):
    for i in range(word_len - part_len + 1):
        word_list.append(word[i:i+part_len])

word_set = set(word_list)
print(len(word_set))