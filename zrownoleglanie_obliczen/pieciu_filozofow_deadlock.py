#!/usr/bin/env python3

import threading
import time


class Philosopher(threading.Thread):


    def __init__(self, name, lfork, rfork, event):

        threading.Thread.__init__(self)
        self.name = name
        self.left_fork = lfork
        self.right_fork = rfork
        self.stop_event = event


    def think(self):

        print(f'{self.name} mysli.')


    def dine(self):

        print(f'{self.name} jest glodny.')
        self.left_fork.acquire()
        self.right_fork.acquire()
        print(f'{self.name} rozpoczyna posilek.')
        print(f'{self.name} zakonczyl posilek.')
        self.left_fork.release()
        self.right_fork.release()


    def run(self):

        while not self.stop_event.is_set():
            self.think()
            self.dine()


def main():

        forks = [threading.Lock() for i in range(5)]
        event = threading.Event()
        philosophers = [Philosopher('Filozof nr %i' % (i+1), forks[i%5], forks[(i+1)%5], event) for i in range(5)]

        for p in philosophers:
            p.start()

        time.sleep(15)

        print('Rozpoczeto zatrzymywanie programu...')

        event.set()

        print('Oczekiwanie na zakonczenie posilkow przez filozofow...')

        for p in philosophers:
            p.join()

        print('Koniec programu.')


if __name__ == '__main__':

    main()

