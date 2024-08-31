while True:
    x = int(input('매장에서 먹을지 포장할지 선택하세요. 1. 매장, 2. 포장  '))

    if x == 1 :
        print('매장을 선택하셨습니다.')
        break

    elif x == 2:
        print('포장을 선택하셨습니다.')
        break
    else:
        print('다시 선택하세요.')

while True:
        
    y = int(input('세트와 단품 중 선택하세요. 1. 세트, 2. 단품  '))

    if y == 1:
        print('세트를 선택하셨습니다.')
        break
        
    elif y == 2:
        print('단품을 선택했습니다.')
        break
    else:
        print('다시 선택하세요.')

dic_b = { '불고기버거' : 5000,
         '새우버거' : 6000,
         '빅맥' : 7000}

dic_be = { '콜라' : 1000,
          '사이다' : 500,
          '물' : 0 }
dic_s = { '감자튀김' : 0,
         '너겟' : 1000,
         '치즈스틱' : 500 }

p = 0

list = []

print(dic_b)
print(dic_be)
print(dic_s)
while True:
    b = int(input('버거를 선택하세요. 1. 불고기 버거, 2. 새우 버거, 3. 빅맥  '))
    if b == 1:
        p += dic_b['불고기버거']
        list.append('불고기버거')
        break

    elif b == 2:
        p += dic_b['새우버거']
        list.append('새우버거')
        break

    elif b == 3:
        p += dic_b['빅맥']
        list.append('빅맥')
        break
    else:
        print('다시 선택하세요.')


if y == 1:
    while True:
        be = int(input('음료를 선택하세요. 1. 콜라, 2. 사이다, 3. 물  '))
        if be == 1:
            p += dic_be['콜라']
            list.append('콜라')
            break

        elif be == 2:
            p += dic_be['사이다']
            list.append('사이다')
            break

        elif be == 3:
            p += dic_be['물']
            list.append('물')
            break
        else:
            print('다시 선택하세요.')

    while True:
        s = int(input('사이드를 선택하세요. 1. 감자튀김, 2. 너겟, 3. 치즈스틱  '))
        if s == 1:
            p += dic_s['감자튀김']
            list.append('감자튀김')
            break

        elif s == 2:
            p += dic_s['너겟']
            list.append('너겟')
            break

        elif s == 3:
            p += dic_s['치즈스틱']
            list.append('치즈스틱')
            break
        else:
            print('다시 선택하세요.')
print('주문내역')
print(*list)
print(f'{p}원')

while True:
    z = int(input('어떻게 계산 하시겠습니까? 1. 카드, 2. 현금  '))

    if z == 1:
        print('카드를 선택하셨습니다.')
        print('결제되었습니다.')
        break

    elif z == 2:
        print('현금을 선택하셨습니다.')

        
        c=''
        while True:
        
            c = input('결제할 금액을 입력하세요 : ')

            try:
                c = int(c)

                if c > 0:
                    if c > p:
                        print('결제되었습니다.')
                        print(f'잔돈 {c -p}원 입니다.')
                        break
                    elif c == p:
                        print('결제되었습니다.')
                        break
                    elif c < p:
                        print(f'{p -c}원 부족합니다.')

                else :
                    print('자연수만 입력하세요.')
            except:
                print('숫자만 입력하세요.')
        break

    else:
        print('다시 선택하세요.')
