# yosh = int(input("Yoshingiz nechada?: "))
# if yosh <=4:
#     price = 0
# elif yosh<=12:
#     price = 5000
# elif yosh<65:
#     price = 10000
# elif yosh >=65:
#     price = 8000
# print(f"Sizga kirish {price} so'm")
from operator import truediv

#
# kun = input("Bugun nima kun?")
# harorat = float(input("Bugun havo harorati qanday?"))
# if(kun.lower()=="shanba" or kun.lower()=="yakshanba") and harorat>=30:
#     print("Davay cho'milamiz!!!")
# elif(kun.lower()=="shanba" or kun.lower()=="yakshanba") and harorat<30:
#     print("Uyda qolgan ma'qul")
# else:
#     print("Bugun ish kuni, dam olish kunini kutaylik!")

# narx = 15000
# choy = True
# salat = False
# non = True
# kompot = True
# assorti = False
# if choy:
#     print("Mijoz choy oldi.")
#     narx = narx+3000
# if salat:
#     print("Mijoz salat oldi.")
#     narx = narx+5000
# if non:
#     print("Mijoz non oldi.")
#     narx = narx+2000
# if kompot:
#     print("Mijoz kompot oldi.")
#     narx = narx+5000
# if assorti:
#     print("Mijoz assorti oldi.")
#     narx = narx+15000
# print(f"Jami narx: {narx}")

menu = ['osh', 'qozonkabob', 'shashlik', 'norin', 'somsa' ]
buyurtma = ['osh', 'somsa', 'manti', 'shashlik']
if buyurtma:
    for taom in buyurtma:
        if taom in menu:
            print(f'menuda {taom} bor')
        else:
            print(f'Kechirasiz, {taom} menuda yoq')
else:
    print("Iltimos, ovqat kiriting!")