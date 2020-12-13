#!/usr/bin/env python3

import numpy as np
import concurrent.futures


class Histogram():


    def __init__(self):

        self.results = np.zeros((10,), dtype=int)


    def parallel_sum(self, row):

        _sum = np.sum(row)
        
        for i in range(10):
            if _sum <= (i+1)*10:
                self.results[i] += 1
                break


    def print_results(self):

        print('Wyniki testu (laczna suma punktow):\n')
        print(f'0-10 punktow: {self.results[0]} osob')

        for i in range(1, 10):
            result = self.results[i]
            results_range = f'{10*i+1}-{10*i+10}'
            print(f'{results_range} punktow: {result} osob')


    def run(self):

        np.random.RandomState(100)
        arr = np.random.randint(0, 10, size = [50000, 10])
        data = arr.tolist()

        print('\nW internetowym tescie ze znajomosci jezyka Python wzielo udzial 50000 uzytkownikow.')
        print('Test skladal sie z 10 zadan. W kazdym z nich mozna bylo zdobyc 0-10 punktow.')
        print('Lacznie mozna bylo uzyskac 100 punktow.\n')

        number_of_threads = 2

        with concurrent.futures.ThreadPoolExecutor(number_of_threads) as thp:
            thp.map(self.parallel_sum, data)

        self.print_results()


def main():

    hist = Histogram()
    hist.run()


if __name__ == '__main__':
    
    main()

