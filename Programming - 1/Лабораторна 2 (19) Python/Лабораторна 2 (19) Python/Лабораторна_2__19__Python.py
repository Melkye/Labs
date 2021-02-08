print("Denys Adamov IC-01")
x = float(input("Enter X coordinate: "))
y = float(input("Enter Y coordinate: "))
if (abs(x + y) + abs(x - y) <= 6):  # чи належить точка квадрату
    if (x * x + y * y >= 9):        # чи не належить точка кругу
        if (abs(x + y) + x - y >= 0): # чи не належить другій чверті
            print("The point belongs to the area")
        else:
            print("The point doesn't belong to the area")
    else:
        print("The point doesn't belong to the area")
else:
    print("The point doesn't belong to the area")