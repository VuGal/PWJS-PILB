#!/usr/bin/env python3

import threading
import time


class Semaphore():


    def __init__(self, init_value):
        self.lock = threading.Condition(threading.Lock())
        self.value = init_value


    def up(self):
        with self.lock:
            self.value += 1
            self.lock.notify()


    def down(self):
        with self.lock:
            while self.value == 0:
                self.lock.wait()
            self.value -= 1


class Fork():


    def __init__(self, num):
        
        self.number = num
        self.user_name = ''
        self.lock = threading.Condition(threading.Lock())
        self.taken = False


    def take(self, user_name):
        
        with self.lock:
            while self.taken == True:
                self.lock.wait()
            self.user_name = user_name
            self.taken = True
            print(f'{user_name} podniosl widelec nr {self.number+1}.')
            self.lock.notifyAll()


    def drop(self, user_name):
        
        with self.lock:
            while self.taken == False:
                self.lock.wait()
            self.user_name = -1
            self.taken = False
            print(f'{user_name} opuscil widelec nr {self.number+1}.')
            self.lock.notifyAll()


class Philosopher(threading.Thread):


    def __init__(self, name, lfork, rfork, butler):

        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = lfork
        self.right_fork = rfork
        self.butler = butler


    def run(self):

        print(f'{self.name} zaczyna rozmyslac.')

        for i in range (30):
            
            print(f'{self.name} jest glodny.')
            
            self.butler.down()
            
            print(f'{self.name} rozpoczyna posilek.')
            
            time.sleep(0.1)
            self.left_fork.take(self.name)
            time.sleep(0.1)
            self.right_fork.take(self.name)
            time.sleep(0.1)
            self.right_fork.drop(self.name)
            self.left_fork.drop(self.name)
            print(f'{self.name} zakonczyl posilek i wraca do rozmyslania.')
            self.butler.up()
            
        print(f'{self.name} zakonczyl jedzenie i rozmyslanie')


def main():

        butler = Semaphore(4)

        f = [Fork(i) for i in range(5)]

        p = [Philosopher(f'Filozof nr {i+1}', f[i], f[(i+1)%5], butler) for i in range(5)]

        for i in range(5):
            p[i].start()

        print('Koniec programu.')


if __name__ == '__main__':

    main()

