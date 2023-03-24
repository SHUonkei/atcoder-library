N = int(input())
S = list(input())

"後ろから考える"

"パズル系統、貪欲 or dp？？？"

for i in range(N-2):
    if S[i] == S[i+1] == S[i+2]:
        print("Yes")
        exit()
print("No")