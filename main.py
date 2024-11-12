vosem = input("Введите число в восьмеричной системе состоящее из 5 цифр: ")
desyat = 0
desyat = (int(vosem[0]) * 8 ** 4 + int(vosem[1]) * 8 ** 3 + int(vosem[2]) * 8 ** 2 + int(vosem[3]) * 8 ** 1 + int(vosem[4]) * 8 ** 0)
print("Число в десятичной системе: ", desyat)
