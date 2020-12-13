#!/usr/bin/env python3

import sys
import csv


class CSVFileHandler:


    def show_start_screen(self):
        
        print('\n***********************************')
        print('********* LISTA STUDENTOW *********')
        print('***********************************\n')

        with open('students_list.csv', 'r') as csv_file:
   
            print('-----------------------------------')

            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    
            for row in csv_reader:

                try:
                    
                    print(f'ID: {row[0]}')
                    print(f'Imie: {row[1]}')
                    print(f'Nazwisko: {row[2]}')
                    print(f'Data urodzenia: {row[3]}')
                    print(f'Nr indeksu: {row[4]}')
                    print(f'Kierunek: {row[5]}')
                    print(f'Rok: {row[6]}')
                    print('-----------------------------------')

                except:

                    print(f'Plik .csv zawiera bledy!')

            print('\n***********************************\n')
            print('Wybierz akcje:')
            print('1. Dodaj nowego studenta')
            print('2. Usun studenta')
            print('3. Zakoncz program\n')


    def add_student(self):

        print('\n----------------------------------')
        print('---------- NOWY STUDENT ----------')
        print('----------------------------------\n\n')

        last_id = 0

        with open('students_list.csv', 'r') as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            for row in csv_reader:
                
                if int(row[0]) > last_id:
                    last_id = int(row[0])
        
        _id = last_id + 1

        parameters = { \
                'Imie' : '',
                'Nazwisko' : '',
                'Data urodzenia' : '',
                'Nr indeksu' : '',
                'Kierunek' : '',
                'Rok' : ''
                }

        for parameter in parameters:

            while True:
                print(f'{parameter}:')
                _input = input()

                if ',' not in _input:
                    parameters[parameter] = _input
                    break
                else:
                    print(f'{parameter} nie moze zawierac znaku przecinka! Ponow probe.')

        print('-----------------------------------')
        print(f'Imie: {parameters["Imie"]}')
        print(f'Nazwisko: {parameters["Nazwisko"]}')
        print(f'Data urodzenia: {parameters["Data urodzenia"]}')
        print(f'Nr indeksu: {parameters["Nr indeksu"]}')
        print(f'Kierunek: {parameters["Kierunek"]}')
        print(f'Rok: {parameters["Rok"]}')
        print('-----------------------------------')

        print('Czy potwierdzasz utworzenie nowego wpisu do listy? (y/n)')

        while True:

            _input = input()

            if _input == 'y':
                with open('students_list.csv', 'a') as csv_file:
                    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerow([_id, parameters['Imie'], parameters['Nazwisko'], parameters['Data urodzenia'], \
                                         parameters['Nr indeksu'], parameters['Kierunek'], parameters['Rok']])
                break
            elif _input == 'n':
                break
            else:
                print('Wprowadz poprawna litere: y -> tak, n -> nie')


    def remove_student(self):
        
        id_map = dict()
        data = list() 

        with open('students_list.csv', 'r') as csv_file:

            csv_reader = csv.reader(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

            number_of_students = sum(1 for row in csv_reader)

            if number_of_students == 0:
                print("Nie znaleziono zadnych studentow na liscie!")
                return
        
            csv_file.seek(0)

            for i, row in zip(range(number_of_students), csv_reader):
                data.append(row)
                id_map[i] = row[0]

        print('Podaj ID studenta, ktorego wpis zostanie usuniety.')

        while True:

            _input = input()

            if ( _input > '0' and _input in id_map.values() ):

                for i in range(len(data)):

                    if data[i][0] == _input:
                        del(data[i])
                        break

                with open('students_list.csv', 'w') as csv_file:

                    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
                    csv_writer.writerows(data)

                break

            else:
                print('Podano nieprawidlowe ID studenta! Prosze sprobowac ponownie.')
        

    def run(self):

        while True:
            
            self.show_start_screen()

            while True:

                try:
                    choice = input()
                except KeyboardInterrupt:
                    print('Dziekujemy za skorzystanie z programu!')
                    sys.exit()
                
                if choice not in ['1', '2', '3']:
                    print('Wybrano niepoprawna opcje. Wpisz liczbe 1-3.')
                
                elif choice == '1':
                    try:
                        self.add_student()
                        break
                    except KeyboardInterrupt:
                        break
                
                elif choice == '2':
                    try:
                        self.remove_student()
                        break
                    except KeyboardInterrupt:
                        break
                
                elif choice == '3':
                    print('\nDziekujemy za skorzystanie z programu!\n')
                    sys.exit()
                    break
                
                else:
                    raise


def main():

    csv_file_handler = CSVFileHandler()
    csv_file_handler.run()


if (__name__ == '__main__'):

    main()

