#!/usr/bin/env python3

import xml.dom.minidom

from random import seed
from random import randint


class XMLDOMParser:


    def print_employee_info(self, collection):

        employees = collection.getElementsByTagName('Employee')
        
        for employee in employees:
            
            print("\n--------------------------------")
            print("---------- Pracownik -----------")
            print("--------------------------------\n")

            if employee.hasAttribute('id'):
                print(f'ID pracownika: {employee.getAttribute("id")}')
            
            if len(employee.getElementsByTagName('Name')) != 0:
                name = employee.getElementsByTagName('Name')[0]
                print(f'Imie: {name.childNodes[0].data}')

            if len(employee.getElementsByTagName('Surname')) != 0:
                surname = employee.getElementsByTagName('Surname')[0]
                print(f'Nazwisko: {surname.childNodes[0].data}')

            if len(employee.getElementsByTagName('Position')) != 0:
                position = employee.getElementsByTagName('Position')[0]
                print(f'Stanowisko: {position.childNodes[0].data}')

            if len(employee.getElementsByTagName('Salary')) != 0:
                salary = employee.getElementsByTagName('Salary')[0]
                print(f'Zarobki: {salary.childNodes[0].data} PLN miesiecznie')

            if len(employee.getElementsByTagName('Age')) != 0:
                age = employee.getElementsByTagName('Age')[0]
                print(f'Wiek: {age.childNodes[0].data}')


    def print_office_info(self, collection):

        offices = collection.getElementsByTagName('Office')

        for office in offices:

            print("\n--------------------------------")
            print("------------ Biuro -------------")
            print("--------------------------------\n")

            if office.hasAttribute('id'):
                print(f'ID biura: {office.getAttribute("id")}')

            if len(office.getElementsByTagName('Address')) != 0:
                address = office.getElementsByTagName('Address')[0]
                print(f'Adres: {address.childNodes[0].data}')

            if len(office.getElementsByTagName('Area')) != 0:
                area = office.getElementsByTagName('Area')[0]
                print(f'Powierzchnia: {area.childNodes[0].data}')

            if len(office.getElementsByTagName('RentCost')) != 0:
                rent_cost = office.getElementsByTagName('RentCost')[0]
                print(f'Koszt wynajmu: {rent_cost.childNodes[0].data} PLN miesiecznie')


    def run(self):

        seed(1)

        DOMTree = xml.dom.minidom.parse('sample_xml_file.xml')
        collection = DOMTree.documentElement

        if collection.hasAttribute("name"):
            print("\n********************************")
            print(f'\nFirma (korzen drzewa DOM): {collection.getAttribute("name")}')

        print("\n********************************")
        self.print_employee_info(collection)
        print("\n********************************")
        self.print_office_info(collection)
        print("\n********************************\n")


        # modyfikacja elementu RentCost dla biura o ID rownym 1
                
        print("\n\n\n------------------------------------------------")
        print('WZROST KOSZTU WYNAJMU BIURA NA UL. NIEISTNIEJACEJ DO 3500 PLN')
        print("------------------------------------------------------")

        offices = collection.getElementsByTagName('Office')

        for office in offices:
            
            if office.hasAttribute('id'):
                if office.getAttribute('id') == '1':
                    office.getElementsByTagName('RentCost')[0].childNodes[0].nodeValue = 3500
 
        print("\n********************************")
        self.print_office_info(collection)
        print("\n********************************\n")


        # dodanie pustego elementu 'Age' dla kazdego z pracownikow

        print("\n\n\n------------------------------------------------")
        print('DODANIE POLA "WIEK" DLA KAZDEGO Z PRACOWNIKOW')
        print("------------------------------------------------------")

        employees = collection.getElementsByTagName('Employee')

        for employee in employees:

            age_element =  DOMTree.createElement('Age')
            age_element_text = DOMTree.createTextNode(' ')

            age_element.appendChild(age_element_text)
            employee.appendChild(age_element)

        print("\n********************************")
        self.print_employee_info(collection)
        print("\n********************************\n")


        # uzupelnienie elementu 'Age' losowymi wartosciami z przedzialu 20-50

        print("\n\n\n------------------------------------------------")
        print('UZUPELNIENIE WIEKU POSZCZEGOLNYCH PRACOWNIKOW')
        print("------------------------------------------------------")

        employees = collection.getElementsByTagName('Employee')

        for employee in employees:

            if len(employee.getElementsByTagName('Age')) != 0:
                age = randint(20, 50)
                employee.getElementsByTagName('Age')[0].childNodes[0].nodeValue = age

        print("\n********************************")
        self.print_employee_info(collection)
        print("\n********************************\n")


        # usuniecie elementu pracownika o ID rownym 101 wraz ze wszystkimi elementami podrzednymi
        
        print("\n\n\n------------------------------------------------")
        print('ZWOLNIENIE PRACOWNIKA: RYSZARD NOWAK')
        print("------------------------------------------------------")

        employees = collection.getElementsByTagName('Employee')

        for employee in employees:

            if employee.hasAttribute('id'):
                if employee.getAttribute('id') == '101':
                    employee.parentNode.removeChild(employee)

        print("\n********************************")
        self.print_employee_info(collection)
        print("\n********************************\n")

            
        # stworzenie nowego elementu pracownika wraz ze wszystkimi elementami podrzednymi (niewypelnionymi)

        print("\n\n\n------------------------------------------------")
        print('ZATRUDNIENIE PRACOWNIKA')
        print("------------------------------------------------------")
        
        employees = collection.getElementsByTagName('Employee')[0].parentNode

        new_employee = DOMTree.createElement('Employee')
        new_employee.setAttribute('id', '202')

        new_employee_name = DOMTree.createElement('Name')
        new_employee_name.appendChild(DOMTree.createTextNode(' '))
        new_employee.appendChild(new_employee_name)

        new_employee_surname = DOMTree.createElement('Surname')
        new_employee_surname.appendChild(DOMTree.createTextNode(' '))
        new_employee.appendChild(new_employee_surname)

        new_employee_position = DOMTree.createElement('Position')
        new_employee_position.appendChild(DOMTree.createTextNode(' '))
        new_employee.appendChild(new_employee_position)

        new_employee_salary = DOMTree.createElement('Salary')
        new_employee_salary.appendChild(DOMTree.createTextNode(' '))
        new_employee.appendChild(new_employee_salary)

        new_employee_age = DOMTree.createElement('Age')
        new_employee_age.appendChild(DOMTree.createTextNode(' '))
        new_employee.appendChild(new_employee_age)

        employees.appendChild(new_employee)

        print("\n********************************")
        self.print_employee_info(collection)
        print("\n********************************\n")


        # uzupelnienie wartosci elementow podrzednych nowego elementu pracownika
        
        print("\n\n\n--------------------------------")
        print('UZUPELNIENIE INFORMACJI O NOWYM PRACOWNIKU')
        print("--------------------------------")

        employees = collection.getElementsByTagName('Employee')

        for employee in employees:
            if employee.hasAttribute('id'):
                if employee.getAttribute('id') == '202':
                   
                   employee.getElementsByTagName('Name')[0].childNodes[0].nodeValue = 'Piotr'
                   employee.getElementsByTagName('Surname')[0].childNodes[0].nodeValue = 'Zagloba'
                   employee.getElementsByTagName('Position')[0].childNodes[0].nodeValue = 'Junior Python Developer'
                   employee.getElementsByTagName('Salary')[0].childNodes[0].nodeValue = 5500
                   employee.getElementsByTagName('Age')[0].childNodes[0].nodeValue = 25
        
        print("\n********************************")
        self.print_employee_info(collection)
        print("\n********************************\n")

        with open('sample_xml_file.xml', 'w') as f:
            DOMTree.writexml(f)


def main():
    
    parser = XMLDOMParser()
    parser.run()


if (__name__ == "__main__"):
    
    main()

