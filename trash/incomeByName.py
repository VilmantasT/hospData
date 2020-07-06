# -*- coding: utf-8 -*-
"""
Created on Tue May 19 09:17:34 2020

@author: Kompiuteris2
"""

import csv, pdb
from decimal import Decimal

file = 'detali_2019.csv'

dataByMonth = {}

with open(file) as csv_file:
        csv_reader = csv.reader(csv_file)
        
        for row in csv_reader:
            if csv_reader.line_num in [0,1,2]:
                continue
            elif csv_reader.line_num >= 7:
                data = ','.join(row).split(';')

                dataByMonth[data[11]] = dataByMonth.get(data[11], {})
                print(dataByMonth)
                if data[11] in dataByMonth:
                    dataByMonth[data[11]] = dataByMonth[data[11]].get(data[16], {})
                    
                    
                    
                