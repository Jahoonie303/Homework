# car_0 = {'model':'ferrari','rang':'qizil'}
# print(car_0)
#
# car_0 = {'model':'ferrari','rang':'qizil'}
# print(car_0['model'])
# print(car_0['rang'])
#
#
# talaba_0 = {'ism':'murod olimov','yosh':20,'t_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#  {talaba_0['t_yil']}-yilda tu'gilgan,\
#  {talaba_0['yosh']} yoshda")
#
# talaba_0['kurs'] = 4 # yangi, 'kurs' nomli kalit so'zga 4 qiymatini yuklaymiz
# talaba_0['fakultet'] = 'informatika' # 'fakultet' ga esa 'informatika’
# print(talaba_0)
#
# talaba_1 = {}
# talaba_1['ism'] = 'qobil rasulov'
# talaba_1['kurs'] = 3
# talaba_1['yosh'] = 20
# print(talaba_1)
# print(f"Talaba {talaba_1['ism'].title()} {talaba_1['kurs']}-kurs")

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310'
    }
phone = telefonlar['ali']
print(f"Alining telefoni {phone}")
phone = telefonlar.get('hasan','Bunday ism mavjud emas')
print(f"Hasanning telefoni {phone}")
