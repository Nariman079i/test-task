import sys
import logging
from time import sleep
from keyboard import *

def liter_limit(liter:float,a:float,b:float):
    try:
        if a < liter <= b:
            return 1

        elif liter < 0 :
            return 2

        elif liter==0:
            return 3
        else:
            return 0
    except ValueError:
        return 4

class Teapot:
    def __init__(self, liter:int=None,time_boiling=10):
        self.liter = liter 
        self.time_boiling = time_boiling / 2 #Время закипания
        

    def run(self):
        print()
        print("Сколько литров воды вы хотите налить в чайник")
        print("Если захотите остановить чайник удерживайте 'A' eng")
        self.liter = float(input("( 0 - 1.0 ) :"))

        action = liter_limit(self.liter, 0, 1.0)

        if action == 1 :
            time = int(self.liter * self.time_boiling)
            print("Чайник вкл")
            t = 0
            while True:
                try: 
                    
                    if is_pressed("a"):
                        sys.exit()
                    
                    print(f"{int(t)}°")
                    if t == 100.0:
                        
                        break
                    t += self.time_boiling * 2
                    
                    sleep((1.0 - (1.0-self.liter)))
                    

                except:
                    print("Чайник остановлен")   
                    quit() 
                    

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
        elif action == 4:
            print("Нужны литры, а не символы")
            print("Попробуйте ещё раз")
            return self.run()
        else:
            print("Чайник не вмещает в себя болше одного литра")
            print("Попробуйте ещё раз")
            return self.run()


teapot1 = Teapot()

if __name__ == '__main__':
    teapot1.run()