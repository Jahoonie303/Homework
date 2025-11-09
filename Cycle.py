# mehmonlar = ['Jahongir', 'Kamron', 'Komil', 'Temur', "O'ktam"]
# # for mehmon in mehmonlar:
# #     print(mehmon)
# for mehmon in mehmonlar:
#         print(f"Hurmatli {mehmon}, sizni 20-mart kuni oshga taklif qilamiz")
#         print("Hurmat bilan Ravshanovlar oilasi")

# sonlar = list(range(11))
# for son in sonlar:
#     print(f"{son}ning kavdrati {son**2}ga teng")
#
# sonlar_kvadrati = []
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
#
# print(sonlar)
# print(sonlar_kvadrati)

dostlar =  []
print("5 ta eng yaqin do'stlaringiz kim?")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingizning ismini kiriting: "))
print(dostlar)