print("Denys Adamov ІС-01")
n = int(input("Enter natural number n: "))
S = 0
for k in range (1, n+1):
    S = S + 1/(k*(2*k+1)*(2*k+1))
print("Sum equals ", "{:.{}f}".format(S, 10))