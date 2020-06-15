# -*- coding: utf-8 -*-
"""
Created on Wed Apr 15 14:35:32 2020

@author: Kompiuteris2
"""

import csv, pdb
from decimal import Decimal
  

# allServices = {}

# def getEndocrino(row):
#     endo
        

# with open("detali.csv") as csv_file:
#     # csv_reader = csv.reader(csv_file, delimiter=",")
#     csv_dict_reader = csv.DictReader(csv_file, ['time', 'code', 'specialist', 'patients', 'consultations', 'money'], delimiter=';')
    
#     for row in csv_dict_reader:
#         time = "".join([i for i in row['time'] if i.isalpha()])
#         money = Decimal(row['money'].replace(",", "."))
#         code = row['code']
#         allServices[time] = allServices.get(time, dict())
        
#         if code in allServices[time]:
#             allServices[time]B[code] += money
#         else:
#             allServices[time][code] = money
#         # allServices[time][code] = allServices[time].get(code, money) + money
        
#     print(allServices)
years = 2015
files = ['israsyti_2015.csv', 'israsyti_2016.csv','israsyti_2017.csv','israsyti_2018.csv','israsyti_2019.csv']

def statistica(file):
    global years
    patients =[]

    with open(file) as csv_file:
        csv_reader = csv.DictReader(csv_file)

        for row in csv_reader:
            data =  row['Skyrius;Etapo_pabaigos_data;Ligos_istorijos_Nr;Korteles_Nr;Etapo_Nr;Pavarde_vardas;Asmens_kodas_gimimo_data;Israsymo_budas'].split(";")
            if data[6] not in patients:
                patients.append(data[6])
    
        old = []
        invalid = []
    
        
        for i in patients:
            # print(int(i[1:3]), int(i[1:3]) <=45, int(i[1:3]) >= 31)
            if int(i[1:3]) <= years - 60 - 1900:
                old.append(i)
            if int(i[1:3]) >= years - 60 - 1900:
               invalid.append(i)
               
        
        result = displayData(years, [len(patients), len(old), len(invalid)])
        
        csv_file.close()   
     
    years += 1

    return result
    
  
def displayData(years, data):
    
    print("***************{} m. ************".format(years))
    print("Visi slaugos: {}".format(data[0]))
    print("Senyvi: {}".format(data[1]))
    print("Su negalia: {}".format(data[2]))
    
for file in files:
    statistica(file)


