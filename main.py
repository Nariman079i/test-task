import sys
import logging
import configs
from time import sleep
from keyboard import *


# "Валидация" для чайника
def liter_limit(liter:float, a: float, b=configs.VOLUME):
    try:
        liter = float(liter)
        if a < liter <= b:
            """
            
            b - объем
            """
            return 1

        elif liter < 0:
            """
            литры не могут быть отрицательными
            """
            return 2

        elif liter == 0:
            """
            чайник включенный без воды, ни к чему хорошему не приведет
            """
            return 3
        else:#
            return 0
    except:#
        """
        тут срабатывает исключение если человек введет символ
        """
        return 4


class Teapot:
    def __init__(self, liter: int = None, time_boiling=configs.TIME_BOILING):
        self.liter = liter
        self.time_boiling = time_boiling / 2  # Время закипания

    def run(self):
        """
        Главная функция для работы с чайником
        """
        logging.basicConfig(level=logging.DEBUG, filename="log.log", format='%(asctime)s %(levelname)s:%(message)s')#
        print()
        print("Сколько литров воды вы хотите налить в чайник")
        print("Если захотите остановить чайник удерживайте 'A' eng")
        self.liter = input("( 0 - 1.0 ) :")#

        action = liter_limit(self.liter, 0)# Проверка налитой воды -- "Валидация" :)

        if action == 1:

            print("Чайник вкл")
            logging.debug('Start Teapot')
            t = 0
            while True:# Цикл для отображения температуры
                try:
                    if is_pressed("a"):#
                        sys.exit()

                    print(f"{int(t)}°")
                    if t == configs.TEMP:#Температура кипения
                        break
                    t += self.time_boiling  #

                    sleep(abs(1.0 - (1.0 - float(self.liter))))
                    """
                    Скорость кипения зависит от налитой воды в чайник
                    чем меньше воды, тем быстрее он вскипит 
                    """
                except:
                    """
                    исключение если нужно будет остановить кипение чайника
                    """
                    logging.error('Stop Teapot')
                    print("Чайник остановлен")
                    quit()

            logging.debug('End Teapot')
            print("Чайник вскипел")
            logging.debug('Off Teapot')
            print("Чайник выкл")
        elif action == 2:
            logging.error('Error code  2')
            print("В чайнике не может быть отрицательное значение литров")
            print("Попробуйте ещё раз")
            return self.run()
        elif action == 3:
            logging.error('Error code  3')
            print("Упс, чайник пустой")
            print("Попробуйте ещё раз")
            return self.run()
        elif action == 4:
            logging.error('Error code  4')
            print("Нужны литры, а не символы")
            print("Попробуйте ещё раз")

            return self.run()
        else:
            logging.error('Error code  0')
            print("Чайник не вмещает в себя больше одного литра")
            print("Попробуйте ещё раз")
            return self.run()


teapot1 = Teapot() #Класс A

teapot1.run() #Экземпляр класса А
