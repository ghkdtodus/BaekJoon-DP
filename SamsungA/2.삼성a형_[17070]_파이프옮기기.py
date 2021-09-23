#input
N = int(input())
state = [list(map(int(input().split())) for _ in range(N)]
              
#initialize
state[0][:2] = [2,2]
cnt = 0 #count the numbers of way

