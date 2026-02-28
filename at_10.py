import math


cat_1 = int(input("Qual o valor do primeiro cateto: "))
cat_2 = int(input("Qual o valor do segundo cateto: "))

hip_quad = (cat_1*cat_1) + (cat_2*cat_2)

hip = math.sqrt(hip_quad)

print(hip)
