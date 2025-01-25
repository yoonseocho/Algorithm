#이제 순서대로 K번째 사람을 제거한다. 
# 한 사람이 제거되면 남은 사람들로 이루어진 원을 따라 이 과정을 계속해 나간다. (이 과정은 N명의 사람이 모두 제거될 때까지 계속된다) 

N, K = map(int, input().split())

st1 = []
st2 = []
num = K-1

for i in range(N):
  st1.append(i+1)
  


for _ in range(N):
  if len(st1)>num:
    st2.append(st1.pop(num))
    num += K-1
  elif len(st1)<=num:
    num %= len(st1)
    st2.append(st1.pop(num))
    num += K-1


print('<'+ ', '.join(str(i) for i in st2)+ '>') # '+'는 공백포함x ','는 공백포함o

  

