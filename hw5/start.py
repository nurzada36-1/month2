from casino import bet
from decouple import config

My_Money = int(config("My_Money"))
while True:
    print('Ваш баланс ' + str(My_Money))
    print('Запустить казино? (да или нет)')
    a = input('')
    if a == 'нет':
        print('вы вышли из казино!')
        break
    elif a == 'да':
        b = int(input('загадайте число от 1 до 30 - '))
        g = int(input('сколько хотите поставить? - '))
        My_Money -= g
        My_Money += bet(b, g)

    else:
        print('проверьте правильно ли вы написали')
