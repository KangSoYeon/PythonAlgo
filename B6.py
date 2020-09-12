from fractions import Fraction

N = int(input())

#0~N
initialSet = set()
for i in range(N+1): #분자
    for j in range(1, N+1): #분모
        if i <= j:
            initialSet.add(Fraction(i,j))

list = list(initialSet)

list.sort()

for i in list:
    print(str(i.numerator)+"/"+ str(i.denominator))
