a,b,c,d = input().split()
 
clock_num = min([int(a+b+c+d),int(b+c+d+a),int(c+d+a+b),int(d+a+b+c)])
sol = 0
for x in range(1111,clock_num+1):
    a, b, c, d = str(x)
    clock_num = min([int(a+b+c+d),int(b+c+d+a),int(c+d+a+b),int(d+a+b+c)])
    if clock_num == x: sol+=1
 
print(sol)