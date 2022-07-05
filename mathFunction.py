import simpleeval
import numpy as np
# import matplotlib.pyplot as plt

def f(indp, func):
    try:
        func = func.replace("x", "(x)")
        func = func.replace("x", str(indp))

        ans = (simpleeval.simple_eval(func, functions = 
        {"sin": lambda x:np.sin(x),
            "cos": lambda x:np.cos(x),
            "tan": lambda x:np.tan(x),
            "arcsin": lambda x:np.arcsin(x),
            "arccos": lambda x:np.arccos(x),
            "arctan": lambda x:np.arctan(x),
            "e": np.e,
            "ln": lambda x:np.log(x)
        }))

        return ans
    except ZeroDivisionError:
        if indp == 0:
            indp = 1/(10**(-100))
        func = func.replace("x", "(x)")
        func = func.replace("x", str(indp))

        ans = (simpleeval.simple_eval(func, functions = 
        {"sin": lambda x:np.sin(x),
            "cos": lambda x:np.cos(x),
            "tan": lambda x:np.tan(x),
            "arcsin": lambda x:np.arcsin(x),
            "arccos": lambda x:np.arccos(x),
            "arctan": lambda x:np.arctan(x),
            "e": np.e,
            "ln": lambda x:np.log(x)
        }))

        return ans

def simpsonsIntegration(func, a, b, subintervals):
    defInt = 0
    parts = np.linspace(a, b, subintervals+1)
    for i in range(1, subintervals+1):
        sbpt = np.linspace(parts[i-1], parts[i],4)
        h = np.absolute(sbpt[1]-parts[i-1])
        defInt = defInt + ((3/8)*h) * (f(sbpt[0], func) + 3*f(sbpt[1], func) + 3*f(sbpt[2], func) + f(sbpt[3], func))
    
    if(a > b):
        defInt = defInt * -1
    
    return defInt

# stringCheese = input("Input your function: \n")
# bound1 = float(input("Input the first bound: \n"))
# bound2 = float(input("Input the second bound: \n"))

# result = []
# x = np.linspace(bound1, bound2, int((bound2 - bound1)*100), endpoint=False)
# x = x.tolist()
# # print(x)
# if 'x' in stringCheese:
#     for i in x:
#         result.append(f(i, stringCheese))

# # print(x,result)
# integrationAnswer = simpsonsIntegration(stringCheese, bound1, bound2, 2100)
# print(integrationAnswer)

# plt.plot(x, result)
# plt.show()