mode1 = int(input('請輸入轉換單位 攝氏-->華氏(1)/華氏-->攝氏(2):'))

if mode1 == 1 :
    fahrenheit = float(input('請輸入華氏溫度:'))
    celsius = (fahrenheit-32.)*5 / 9
    print('攝氏溫度 = ',celsius)

if mode1 == 2:
    celsius = float(input('請輸入華氏溫度:'))
    fahrenheit = celsius * 9 / 5 + 32.
    print('華氏溫度 = ',fahrenheit)
elif (mode1 != 1 and mode1 != 2):
    print('輸入錯誤')
    