print("Enter four numbers and the program will form combinations of multiples the first three numbers to find numbers less than or equal to the fourth number you input.")
x = int(input())
y = int(input())
z = int(input())
p = int(input())
if x>p:
    print("The first number is above the last number.")
    exit()
if y>p:
    print("The second number is above the last number.")
    exit()
if z>p:
    print("The third number is above the last numbere+.")
    exit()
maxnum1 = min(x, y, z)
maxnum2 = round(p/maxnum1)
res = ""
allnum = []
for a in range(1, p+1):
    for k in range(0, maxnum2+1):
        for l in range(0, maxnum2+1):
            for m in range(0, maxnum2+1):
                if a == k*x + l*y + m*z:
                    res = res + (str(a) +" = " + str(k) + "*" + str(x) + " + " + str(l) + "*" + str(y) + " + " + str(m) + "*" + str(z) + "  \n")
                    allnum.append(a)
print("A list of all the possible solutions is: \n" + res)
set_allnum = set(allnum)
list_res = (list(set_allnum))
print("All possible numbers that can be made using the inputted numbers are: ")
print(*list_res , sep = ", ")

