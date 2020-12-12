import math
print ("Denys Adamov IC-01")
Square1_Area = float(input ("Enter 1st square's area: "))       # введення площі першого квадрата

Square2_Diagonal = round(math.sqrt(Square1_Area), 2)            # знаходження діагоналі вписаного квадрата через посередництво кола
Square2_Area = round(Square2_Diagonal * Square2_Diagonal / 2)   # знаходження площі вписаного квадрата
N = round(Square1_Area / Square2_Area)                          # у скільки раз другий менший, ніж перший

print ( "2nd square's area: ", Square2_Area)                    # виведення площі другого квадрата
print ("2nd is ", N, " times smaller than 1st")                 # та отриманого N