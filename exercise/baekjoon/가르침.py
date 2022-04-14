from itertools import combinations
import sys
sys.stdin = open("input.txt", "r")

n,k = map(int, sys.stdin.readline().split()) #3 6
word_list = []
for _ in range(n):
    word_list.append(sys.stdin.readline())

#필수못배우면의미없
if k<5:
    print(0)
    exit(0)

pre = 'anta'
post = 'tica'
must_alph = ['a','n','t','i','c']
alph = [ 'b', 'd', 'e', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'o', 'p', 
        'q', 'r', 's', 'u', 'v', 'w', 'x', 'y', 'z']

#읽을 수 있는지
def readable(word, must_alph):
    flag = True
    word = word[len(pre):-len(post)]
    for w in word:
        if w not in must_alph:
            flag = False
            break
    return flag

#k-5내에서 모든 조합 구하기 -> alph에서 k-5개 고르기
cnt = 0
for c in combinations(alph,k-5):
    cnt_new = 0
    for word in word_list:
        if readable(word,must_alph+list(c)):
            cnt_new += 1
    cnt = max(cnt,cnt_new)
print(cnt)