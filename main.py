Pers = 'Наруто'

def sravnenyie(a,b):
    if a == b:
        print("\033[92m" + ' '.join(a) + "\033[0m")
    else:
        Done = False
        for i in b:
            for j in a:
                if i == j:
                    print("\033[34m" + ' '.join(a) + "\033[0m")
                    Done = True
        if Done == False:
            print("\033[31m" + ' '.join(a) + "\033[0m")


def logica(Pers,GuessPers,Pvilage,Pjutsu,PkekeGenkay,Pstats,Patributes,Parka):
    f = open('NarutoList.txt', 'r', encoding='utf-8')
    for line in f:
        if GuessPers == line.split(sep=';')[0]:
            vilage = line.split(sep=';')[1]
            vilage = vilage.split()
            jutsu = line.split(sep=';')[2]
            jutsu = jutsu.split()
            kekeGenkay = line.split(sep=';')[3]
            kekeGenkay = kekeGenkay.split()
            stats = line.split(sep=';')[4]
            stats = stats.split()
            atributes = line.split(sep=';')[5]
            atributes = atributes.split()
            arka = line.split(sep=';')[6]
            arka = arka.split()
            f.close()
            print("Персонаж:",GuessPers)
            print('_____')
            print('Деревня:')
            sravnenyie(vilage, Pvilage)
            print('_____')
            print('Джутсу:')
            sravnenyie(jutsu, Pjutsu)
            print('_____')
            print('Кеке-Генкай:')
            sravnenyie(kekeGenkay, PkekeGenkay)
            print('_____')
            print('Стихии:')
            sravnenyie(stats,Pstats)
            print('_____')
            print('Атрибуты:')
            sravnenyie(atributes,Patributes )
            print('_____')
            print('Арка:')
            sravnenyie(arka, Parka)
            if Pers != GuessPers:
                logicaP(Pers)
            else:
                print('Поздравляем!')
    
def logicaP(Pers):
    f = open('NarutoList.txt', 'r', encoding='utf-8')
    for line in f:
        if Pers == line.split(sep=';')[0]:
            Pvilage = line.split(sep=';')[1]
            Pvilage = Pvilage.split()
            Pjutsu = line.split(sep=';')[2]
            Pjutsu = Pjutsu.split()
            PkekeGenkay = line.split(sep=';')[3]
            PkekeGenkay = PkekeGenkay.split()
            Pstats = line.split(sep=';')[4]
            Pstats = Pstats.split()
            Patributes = line.split(sep=';')[5]
            Patributes = Patributes.split()
            Parka = line.split(sep=';')[6]
            Parka = Parka.split()
            GuessPers = input('Введите персонажа')
            logica(Pers,GuessPers,Pvilage,Pjutsu,PkekeGenkay,Pstats,Patributes,Parka)
            f.close()



logicaP(Pers)
