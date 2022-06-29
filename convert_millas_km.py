def run():
    millas =  1.609344
    kiometro = 0.621371
    print('selecciones una opción ')
    print('1 ==> de kilímetros a millas')
    print('2 ==> de milla a kilómeotrs ')
    opciones = int(input(''))
    if opciones == 1:
        kilometros = int(input('text millas to cenverter '))
        total = millas * kilometros
        total = str(total)
        print('you have '+ total+' km')
    if opciones == 2:
        milla = int(input('text millas to cenverter '))
        total = milla * kiometro
        total = str(total)
        print('you have '+ total+' millas')

    

if __name__ == '__main__':
    run()