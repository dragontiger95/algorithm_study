# 나는야 포켓몬 마스터 이다솜

n, m = map(int, input().split())

pokemon_book = set()
pokemon = {}
for i in range(n):
    pokemon[input()] = i+1

# key, value 변경
pokemon_reverse = {v:k for k,v in pokemon.items()}

ans = []
for i in range(m):
    quiz = input()
    if quiz in pokemon:
        ans.append(pokemon[quiz])
    elif int(quiz) in pokemon_reverse:
        ans.append(pokemon_reverse[int(quiz)])
for pok in ans:
    print(pok)