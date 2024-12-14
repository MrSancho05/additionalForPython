# 1 TASK  a va b musbat sonlar berilgan(a>b). a uzunlikdagi kesmaga b uzunlikdagi kesmani mumkin 
# qadar eng ko‘p miqdorda joylashtirilganda, a kesmaning bo‘sh (ortib) qolgan bo‘lagi topilsin. 
# Ko‘paytirish va bo‘lish operatsiyalaridan foydalanilmasin
# a = 6
# b = 4
# while a >= b:
#     a -= b
# print(a)
# print(a % b)

# 2 TASK a va b musbat son berilgan(a>b). a uzunlikdagi kesmaga b uzunlikdagi kesma mumkin qadar 
# eng ko‘p miqdorda joylashtirilgan bo`lsa, (Ko‘paytirish va bo‘lish operatsiyalaridan foydalanmay) 
# a kesmaga joylashtirilgan b kesmalar soni aniqlansin. 
# count = 0
# while a >= b:
#     count += 1
#     a -= b
# print(count)

# 3 TASK n va k musbat butun sonlari berilgan. Faqat qo‘shish va ayirish operatsiyasidan foydalanib n ni 
# k ga bo‘lganda bo‘linmaning butun hamda qoldiq qismi topilsin. 
# n = 6
# k = 4
# count = 0
# while n >= k:
#     count += 1
#     n -= k
# print(f"Butun qism: {count}")
# print(f"Qoldiq qism: {n}")

# 4 TASK n(n>0) butun son berilgan. Agar u 3 sonining darajasidan iborat bo‘lsa true, aks holda false 
# chiqarilsin. 
# n = 243
# while n % 3 == 0:
#     n //= 3
# print(n == 1)

# 5 TASK n(n>0) butun son berilgan. U 2 ning biror bir darajasidan iborat bo‘lsa  n=2k, shu darajaning 
# ko‘rsatkichi k butun soni topilsin.
# n = 512
# daraja = 0
# while n % 2 == 0:
#     n //= 2
#     daraja += 1
# print(daraja)

# 6 TASK n(n>0) butun son berilgan. n ikki factorial hisoblansin. Bu yerda n!!=n(n-2)(n-4)… (oxirgi 
# ko‘paytuvchi agar n-juft bo‘lsa 2 ga, toq bo‘lsa 1 ga teng.) Butun tip diapozonidan oshib 
# ketishining oldini olish uchun bu ko‘paytma natija haqiqiy tipli o‘zgaruvchiga qiymatlanadi. 
# n = 4
# twoFactorialeven = 1
# twoFactorialodd = 1
# if n % 2 == 0:
#     while n > 0:
#         if n % 2 == 0:
#             twoFactorialeven *= n
#         n -= 1
#     print(twoFactorialeven)
# else :
#     while n > 0:
#         if n % 2 == 1:
#             twoFactorialodd *= n
#         n -= 1
#     print(twoFactorialodd)


# 7 TASK n(n>0) butun son berilgan. Kvadratdan ildiz chiqarish formulasidan foydalanmay kvadrati n 
# dan katta eng kichik k soni topilsin. (k2>n) 
# n = 5
# l = 1
# kVn = 0
# while l <= n:
#     # print(l)
#     kVn = l * l
#     # print(kVn)
#     if kVn > n:
#         # print(kVn)
#         break
#     l += 1
# import math
# print(round(math.sqrt(kVn)))

# 8 TASK n butun son berilgan. Kvadratdan ildiz chiqarish formulasidan foydalanmay kvadrati n dan katta 
# bo‘lmagan eng katta butun k soni topilsin. (k2≤n) 
n = 5
i = 1
k = 0
while i <= n:
    print(i * i)
    if i * i <= i:
        # k = n
        print(i)
    i += 1
# print(k)
