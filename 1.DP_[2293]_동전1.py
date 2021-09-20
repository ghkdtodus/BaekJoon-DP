"""
***참고***
map : map(지정함수,요소) 리스트의 요소를 지정된 함수로 처리 
"""

n,k=map(int,input().split())
num=[int(input()) for i in range(n)]

dp = [0] * (k+1)
dp[0] = 1#dp[0] : 동전으로 0원을 만드는 법

for j in num:
    for i in range(j,k+1):
        dp[i]=dp[i-j]+dp[i]

print(dp[k])
