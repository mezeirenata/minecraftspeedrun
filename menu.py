def fomenu():
    print('1 - Menj északra')
    print('2 - Menj délre')
    print('3 - Menj nyugatra')
    print('4 - Menj keletre')
    print('5 - Alvás')
    print('6 - Táplálkozás')
    valasz = int(input('Választás:'))
    match valasz:
        case 1:
            event() 
            
    