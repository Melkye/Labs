print("Denys Adamov ІС-01")
e=0.0
t=1.0
n=0
N=int(input("Set N numbers after decimal point: "))

accuracy = 10**-N   # точність до N-го знаку
p=N+1               # виведенняя з наступним знаком для порівняння
check=bool(1)
while check:
    if (n==0):
        t=1         # перший елемент ряду 
    else:
        t/=n        # елемент ряду
    print("t", "{:<2}".format(n), " = ", "{:.{}f}".format(t, p), sep="")
    e+=t
    n+=1
    if (t/n<accuracy):
        check = 0
    
print("t00 =", "{:.{}f}".format(t/n, p))            # елемент, який менше за точність
print("aсс =", "{:.{}f}".format(accuracy, p))       # точність
print("e   =", "{:.{}f}".format(e, p))
