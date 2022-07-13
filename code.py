f = lambda x: eval(input("F"))
#f_derivative = lambda x: eval(input("F_Dev"))
x = int(input("Enter x:"))
step = 0
while step < 10:
    y = f(x)
    #y1 = f_derivative(x)
    x = x -1/2
    print(step, x)
    step += 1
print("End")#