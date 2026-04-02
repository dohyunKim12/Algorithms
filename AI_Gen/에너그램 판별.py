# 두 문자열 s와 t가 주어질 때, t가 s의 애너그램이면 True, 아니면 False를 반환하세요.
#
# 애너그램 = 글자 구성이 같고 순서만 다른 것
#
# 입출력 예시
#
# ┌──────────┬──────────┬────────┐
# │    s     │    t     │ return │
# ├──────────┼──────────┼────────┤
# │ "listen" │ "silent" │ True   │
# ├──────────┼──────────┼────────┤
# │ "hello"  │ "world"  │ False  │
# ├──────────┼──────────┼────────┤
# │ "aab"    │ "baa"    │ True   │
# └──────────┴──────────┴────────┘

### my style

s = "listen"
t = "silent"

smap = {}
anagram = True                # 기본값 True로 시작

for i in s:
    if i in smap:
        smap[i] += 1
    else:
        smap[i] = 1

for i in t:
    if i in smap:             # smap에 있는지 확인 (s가 아니라 smap)
        smap[i] -= 1
    else:
        anagram = False

for i in smap:                # len(smap) → smap (dict 자체를 순회)
    if smap[i] != 0:
        anagram = False

print(anagram)

### best

s = "listen"
t = "silent"

smap = {}

for c in s:
    smap[c] = smap.get(c, 0) + 1 # getOrDefault
for c in t:
    smap[c] = smap.get(c, 0) - 1

print(all(v == 0 for v in smap.values()))