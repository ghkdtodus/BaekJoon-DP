"""
***참고***
1. eval : "3+4*2-7" 인 문자열을 연산해준다
2. 사용된 알고리즘: dfs
"""

def cal(i,j):
    global answer
    #N만큼 계산을 완료하면 max 값 찾음
    #N==1도 여기서 걸러짐
    if i == len(op):
        answer = max(answer, int(j))
        ##print("answer:",answer)
        return 
        

    #(3+8)*7-9*2 앞에서부터 쭉 연산
    temp1 = eval(j+op[i]+num[i+1])
    ##print("temp1:",temp1)
    cal(i+1, str(temp1))

    #3+(8*7)-(9*2),3+(8*7)-9*2, 3+8*(7-9)*2, 3+8*7-(9*2)
    #괄호 이외 부분은 순서대로 연산
    if i+1 < len(op): #i까지 연산하는게 아니라 i+1까지 연산하기 때문에
        temp2 = eval(num[i+1]+op[i+1]+num[i+2])
        temp2 = eval(j+op[i]+str(temp2))
        ##print("temp2:",temp2)
        cal(i+2, str(temp2))


#***입력***
N = int(input())
exp = input()

#***최솟값***
answer = -2 ** 31

#***숫자와 연산자 분리***
num=[]
op=[]
for e in exp:
    if e.isdigit():
        num.append(e)
    else:
        op.append(e)

#***연산***
cal(0,num[0])
print(answer)


