def cuenta_atras(_num):
    _num-=1
    if _num>0:
        print(_num)
        cuenta_atras(_num)

def factorial(n):
    if(n>1): n=n*factorial(n-1)
    return n

print(factorial(900))