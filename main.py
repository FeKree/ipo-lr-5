vosem = input("Введите число в восьмеричной системе состоящее из 5 цифр: ")
desyat = 0
if len(vosem) == 5:
    for i in range(5): #range(5)-кол-во символов 
        num = int(vosem[i])
        desyat += num * (8 ** (4 - i)) #вывод (8 ** (4 - i)) перевод с 8 в 10 систему
    print("Число в десятичной системе:", desyat)
elif len(vosem)<5:
     print("Вы ввели менее 5 символов")
else:
    print("Вы ввели более 5 символов")