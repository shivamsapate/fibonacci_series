import sys
def fib(n):
    a ,b =0,1
    while a<n:
        print(a,end=' ')
        a,b=b,a+b
    return ["my val"]

if __name__=="__main__":
    fib(10)
    
