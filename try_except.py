#esercizi

num = input('inserisci un numero intero: ')

try:
    num = int(num)

    if num >= 0 :
        if num == 0 :
            print('Zero è un numero Pari')
        else:
            print('hai inserito un numero positivo')
    else:
        print('hai inserito un numero negativo')

except ValueError :
    print('sono ammessi solo numeri')



    