n = int(input("Enter the number: "))
sum_max = 0                        # найбільна сума дільників

for i in range (1, n+1):           # цикл для перевірки усіх чисел від 1 до n включно

    sum_i = 0                      # сума дільників числа і

    for j in range (1, n+1):       # цикл для пошуку дільників числа і від 1 до і включно
        if i % j == 0:      
            sum_i += j      

    if sum_i > sum_max:
        sum_max = sum_i
        n_max = i                  # число з найбільшою сумою дільників
    print(i, sum_i)

print("Number", n_max, "has the largest sum of divisors:", sum_max)



