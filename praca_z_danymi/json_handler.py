#!/usr/bin/env python3

import sys
import json


class JSONFileHandler:


    def show_start_screen(self):
        
        print('\n***********************************')
        print('** LISTA STUDENTOW I PRACOWNIKOW **')
        print('***********************************\n')

        with open('students_and_employees_list.json', 'r+') as json_file:
   
            data = json.load(json_file)

            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            print('^^^^^^^^^^^^ STUDENCI ^^^^^^^^^^^^^')
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n')

            students = data['students']

            for student in students:

                print('-----------------------------------')

                print(f'ID: {student["id"]}')
                print(f'Imie: {student["name"]}')
                print(f'Nazwisko: {student["surname"]}')
                print(f'Data urodzenia: {student["date_of_birth"]}')
                print(f'Nr indeksu: {student["student_no"]}')
                print(f'Kierunek: {student["field_of_study"]}')
                print(f'Rok: {student["year_of_study"]}')
                print('-----------------------------------')

            print('\n^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^')
            print('^^^^^^^^^^^ PRACOWNICY ^^^^^^^^^^^^')
            print('^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n')

            employees = data['employees']

            for employee in employees:

                print('-----------------------------------')

                print(f'ID: {employee["id"]}')
                print(f'Imie: {employee["name"]}')
                print(f'Nazwisko: {employee["surname"]}')
                print(f'Data urodzenia: {employee["date_of_birth"]}')
                print(f'Stanowisko: {employee["position"]}')
                print(f'Siedziba: {employee["room"]}')
                print(f'Nr telefonu: {employee["phone_number"]}')
                print(f'Adres e-mail: {employee["email_address"]}')
                print('-----------------------------------')

            print('\n***********************************\n')
            print('Wybierz akcje:')
            print('1. Dodaj nowego studenta')
            print('2. Dodaj nowego pracownika')
            print('3. Usun studenta')
            print('4. Usun pracownika')
            print('5. Zakoncz program\n')


    def add_student(self):

        print('\n----------------------------------')
        print('---------- NOWY STUDENT ----------')
        print('----------------------------------\n\n')

        last_id = 0

        with open('students_and_employees_list.json', 'r+') as json_file:

            data = json.load(json_file)

            students = data['students']

            for student in students:

                if student["id"] > last_id:
                    last_id = student["id"]

        _id = last_id + 1

        parameters = {
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
                with open('students_and_employees_list.json', 'w+') as json_file:
                    new_student = {
                        'id' : _id,
                        'name' : parameters['Imie'],
                        'surname' : parameters['Nazwisko'],
                        'date_of_birth' : parameters['Data urodzenia'],
                        'student_no' : parameters['Nr indeksu'],
                        'field_of_study' : parameters['Kierunek'],
                        'year_of_study' : parameters['Rok'],
                    }
                    students.append(new_student)
                    json.dump(data, json_file, indent=4)
                break
            elif _input == 'n':
                break
            else:
                print('Wprowadz poprawna litere: y -> tak, n -> nie')


    def add_employee(self):
        
        print('\n----------------------------------')
        print('--------- NOWY PRACOWNIK ---------')
        print('----------------------------------\n\n')

        last_id = 0

        with open('students_and_employees_list.json', 'r+') as json_file:

            data = json.load(json_file)

            employees = data['employees']

            for employee in employees:

                if employee["id"] > last_id:
                    last_id = employee["id"]

        _id = last_id + 1

        parameters = { 
                'Imie' : '',
                'Nazwisko' : '',
                'Data urodzenia' : '',
                'Stanowisko' : '',
                'Siedziba' : '',
                'Nr telefonu' : '',
                'Adres e-mail' : ''
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
        print(f'Stanowisko: {parameters["Stanowisko"]}')
        print(f'Siedziba: {parameters["Siedziba"]}')
        print(f'Nr telefonu: {parameters["Nr telefonu"]}')
        print(f'Adres e-mail: {parameters["Adres e-mail"]}')
        print('-----------------------------------')

        print('Czy potwierdzasz utworzenie nowego wpisu do listy? (y/n)')

        while True:

            _input = input()

            if _input == 'y':                
                with open('students_and_employees_list.json', 'w+') as json_file:
                    new_employee = {
                        'id' : _id,
                        'name' : parameters['Imie'],
                        'surname' : parameters['Nazwisko'],
                        'date_of_birth' : parameters['Data urodzenia'],
                        'position' : parameters['Stanowisko'],
                        'room' : parameters['Siedziba'],
                        'phone_number' : parameters['Nr telefonu'],
                        'email_address' : parameters['Adres e-mail']
                    }
                    employees.append(new_employee)
                    json.dump(data, json_file, indent=4)
                break
            elif _input == 'n':
                break
            else:
                print('Wprowadz poprawna litere: y -> tak, n -> nie')


    def remove_student(self):

        id_map = dict()

        with open('students_and_employees_list.json', 'r+') as json_file:

            data = json.load(json_file)
            students = data['students']

            number_of_students = len(students)

            if number_of_students == 0:
                print("Nie znaleziono zadnych studentow na liscie!")
                return

            for i in range(number_of_students):
                id_map[i] = students[i]['id']

        print('Podaj ID studenta, ktorego wpis zostanie usuniety.')

        while True:

            _input = (int)(input())

            if (_input > 0) and (_input in id_map.values()):

                for index, _id in id_map.items():
                    if _id == _input:
                        del(students[index])
                        break

                with open('students_and_employees_list.json', 'w+') as json_file:
                    json.dump(data, json_file, indent=4)
                break

            else:
                print('Podano nieprawidlowe ID studenta! Prosze sprobowac ponownie.')


    def remove_employee(self):

        id_map = dict()

        with open('students_and_employees_list.json', 'r+') as json_file:

            data = json.load(json_file)
            employees = data['employees']

            number_of_employees = len(employees)

            if number_of_employees == 0:
                print("Nie znaleziono zadnych pracownikow na liscie!")
                return

            for i in range(number_of_employees):
                id_map[i] = employees[i]['id']

        print('Podaj ID pracownika, ktorego wpis zostanie usuniety.')

        while True:

            _input = (int)(input())

            if (_input > 0) and (_input in id_map.values()):

                for index, _id in id_map.items():
                    if _id == _input:
                        del(employees[index])
                        break

                with open('students_and_employees_list.json', 'w+') as json_file:
                    json.dump(data, json_file, indent=4)
                break

            else:
                print('Podano nieprawidlowe ID pracownika! Prosze sprobowac ponownie.') 


    def run(self):

        while True:
            
            self.show_start_screen()

            while True:

                try:
                    choice = input()
                except KeyboardInterrupt:
                    print('Dziekujemy za skorzystanie z programu!')
                    sys.exit()
                
                if choice not in ['1', '2', '3', '4', '5']:
                    print('Wybrano niepoprawna opcje. Wpisz liczbe 1-5.')
                
                elif choice == '1':
                    try:
                        self.add_student()
                        break
                    except KeyboardInterrupt:
                        break

                elif choice == '2':
                    try:
                        self.add_employee()
                        break
                    except KeyboardInterrupt:
                        break
                
                elif choice == '3':
                    try:
                        self.remove_student()
                        break
                    except KeyboardInterrupt:
                        break

                elif choice == '4':
                    try:
                        self.remove_employee()
                        break
                    except KeyboardInterrupt:
                        break
                
                elif choice == '5':
                    print('Dziekujemy za skorzystanie z programu!')
                    sys.exit()
                    break
                
                else:
                    raise


def main():

    json_file_handler = JSONFileHandler()
    json_file_handler.run()


if (__name__ == '__main__'):
    
    main()

