# -*- coding: utf-8 -*-

import openpyxl

wb = openpyxl.load_workbook('export1.xlsx')

report = wb['Report']

patients = []
dubles = []
count = 0

for row in range(2, report.max_row + 1):
    pt = report['C'+str(row)].value
    room = report['F'+str(row)].value
    if room != '':
        count = count + 1
        #print(pt, 'Count:',count)
        if pt not in patients:
            patients.append(pt)
        else:
            dubles.append((pt, report['G'+str(row)].value))
print(len(patients))
print(dubles)