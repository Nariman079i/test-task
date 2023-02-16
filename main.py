from time import sleep


def liter_limit(liter:float,a:float,b:float):

    if a < liter <= b:
        return 1

    elif liter<0 :
        return 2

    elif liter==0:
        return 3

    else:
        return 0

class Teapot:
    
    def __init__(self, liter:int=None,time_boiling=10):
        self.liter = liter 
        self.time_boiling = time_boiling / 2 #Время закипания
        self.run()

    def run(self):
        print()
        print("Сколько литров воды воды вы хотите налить в чайник")

        self.liter = float(input("( 0 - 1.0 ) :"))

        action = liter_limit(self.liter, 0, 1.0)

        if action == 1 :
            time = int(self.liter * 5)
            print("Чайник вкл")
            sleep(time)
            print("Чайник начал кипеть")
            sleep(time)
            print("Чайник вскипел")
            print("Чайник выкл")
        elif action == 2:
            print("В чайнкие не может быть отрицательное значение литров")
            print("Попробуйте ещё раз")
            return self.run()
        elif action == 3:
            print("Упс, чайник пустой")
            print("Попробуйте ещё раз")
            return self.run()
        else:
            print("Чайник не вмещает в себя болше одного литра")
            print("Попробуйте ещё раз")
            return self.run()


teapot1 = Teapot()
