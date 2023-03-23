# 듣보잡

n, m = map(int, input().split())

not_heard = []
not_seen = []
for i in range(n):
    not_heard.append(input())
for i in range(m):
    not_seen.append(input())

not_heard_set = set(not_heard)
not_seen_set = set(not_seen)
not_heard_seen = not_heard_set & not_seen_set

print(len(not_heard_seen))
for name in sorted(list(not_heard_seen)):
    print(name)
