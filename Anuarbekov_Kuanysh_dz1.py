import time

class TrafficLight:
     __color = 'Black'


     def running(self):
          while True:
               self.__color = 'Red'
               print(f'{self.__color}')
               time.sleep(7)
               self.__color = 'Yellow'
               print(f'{self.__color}')
               time.sleep(2)
               self.__color = 'Green'
               print(f'{self.__color}')
               time.sleep(5)


traffic = TrafficLight()
traffic.running()