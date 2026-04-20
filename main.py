Animal = 'Корова'

def sravnenyie(a,b):
    if a == b:
        print("\033[92m" + ' '.join(b) + "\033[0m")
    else:
        Done = False
        for i in b:
            for j in a:
                if i == j:
                    print("\033[34m" + ' '.join(b) + "\033[0m")
                    Done = True
        if Done == False:
            print("\033[31m" + ' '.join(b) + "\033[0m")


def logica(Class,Habitat,Leg,Cover,Reproduction,Size,Animal,GuessAnimal):
    f = open('AnimalList.txt', 'r', encoding='utf-8')
    for line in f:
        if GuessAnimal == line.split(sep=';')[0]:
            GClass = line.split(sep=';')[1]
            GClass = GClass.split()
            GHabitat = line.split(sep=';')[2]
            GHabitat = GHabitat.split()
            GLeg = line.split(sep=';')[3]
            GLeg = GLeg.split()
            GCover = line.split(sep=';')[4]
            GCover = GCover.split()
            GReproduction = line.split(sep=';')[5]
            GReproduction = GReproduction.split()
            GSize = line.split(sep=';')[6]
            GSize = GSize.split()
            f.close()
            print("Животное:",GuessAnimal)
            print('_____')
            print('Класс:')
            sravnenyie(Class, GClass)
            print('_____')
            print('Среда:')
            sravnenyie(Habitat, GHabitat)
            print('_____')
            print('Количество ног:')
            sravnenyie(Leg, GLeg)
            print('_____')
            print('Покров тела:')
            sravnenyie(Cover,GCover)
            print('_____')
            print('Размножение:')
            sravnenyie(Reproduction,GReproduction )
            print('_____')
            print('Размер:')
            sravnenyie(Size, GSize)
            if Animal != GuessAnimal:
                logicaP(Animal)
            else:
                print('Поздравляем!')
    
def logicaP(Animal):
    f = open('AnimalList.txt', 'r', encoding='utf-8')
    for line in f:
        if Animal == line.split(sep=';')[0]:
            Class = line.split(sep=';')[1]
            Class = Class.split()
            Habitat = line.split(sep=';')[2]
            Habitat = Habitat.split()
            Leg = line.split(sep=';')[3]
            Leg = Leg.split()
            Cover = line.split(sep=';')[4]
            Cover = Cover.split()
            Reproduction = line.split(sep=';')[5]
            Reproduction = Reproduction.split()
            Size = line.split(sep=';')[6]
            Size = Size.split()
            GuessAnimal = input('Введите животное')
            logica(Class,Habitat,Leg,Cover,Reproduction,Size,Animal,GuessAnimal)
            f.close()



logicaP(Animal)
