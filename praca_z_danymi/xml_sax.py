#!/usr/bin/env python3

import xml.sax


class EmployeeHandler(xml.sax.ContentHandler):


    def __init__(self):
        self.CurrentData = ""
        self.name = ""
        self.surname = ""
        self.position = ""
        self.salary = ""


    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "Employee":
            print("\n--------------------------------")
            print("---------- Pracownik -----------")
            print("--------------------------------\n")
            _id = attributes['id']
            print(f"ID pracownika: {_id}")


    def endElement(self, tag):
        if self.CurrentData == "Name":
            print(f"Imie: {self.name}")
        elif self.CurrentData == "Surname":
            print(f"Nazwisko: {self.surname}")
        elif self.CurrentData == "Position":
            print(f"Stanowisko: {self.position}")
        elif self.CurrentData == "Salary":
            print(f"Zarobki: {self.salary} PLN miesiecznie")
        self.CurrentData = ""


    def characters(self, content):
        if self.CurrentData == "Name":
            self.name = content
        elif self.CurrentData == "Surname":
            self.surname = content
        elif self.CurrentData == "Position":
            self.position = content
        elif self.CurrentData == "Salary":
            self.salary = content


class OfficeHandler(xml.sax.ContentHandler):


    def __init__(self):
        self.CurrentData = ""
        self.address = ""
        self.area = ""
        self.rent_cost = ""
    

    def startElement(self, tag, attributes):
        self.CurrentData = tag
        if tag == "Office":
            print("\n--------------------------------")
            print("------------ Biuro -------------")
            print("--------------------------------\n")
            _id = attributes['id']
            print(f"ID biura: {_id}")


    def endElement(self, tag):
        if self.CurrentData == "Address":
            print(f"Adres: {self.address}")
        elif self.CurrentData == "Area":
            print(f"Powierzchnia: {self.area}")
        elif self.CurrentData == "RentCost":
            print(f"Koszt wynajmu: {self.rent_cost} PLN miesiecznie")
        self.CurrentData = ""


    def characters(self, content):
        if self.CurrentData == "Address":
            self.address = content
        elif self.CurrentData == "Area":
            self.area = content
        elif self.CurrentData == "RentCost":
            self.rent_cost = content


def main():

    parser = xml.sax.make_parser()
    parser.setFeature(xml.sax.handler.feature_namespaces, 0)
    print("\n********************************")

    parser.setContentHandler( EmployeeHandler() )
    parser.parse("sample_xml_file.xml")
    print("\n********************************")

    parser.setContentHandler( OfficeHandler() )
    parser.parse("sample_xml_file.xml")
    print("\n********************************\n")

    
    # Parser SAX nie pozwala na modyfikacje plikow .xml, w zwiazku z czym
    # zaprezentowany zostal tylko odczyt.


if (__name__ == "__main__"):

    main()

