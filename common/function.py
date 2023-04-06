from datetime import date, timedelta

import xlrd


def read_excel(filename):
    xlsx=xlrd.open_workbook(filename)
    sheet=xlsx.sheet_by_index(0)
    data=[]
    for i in range(sheet.nrows):
        if(i==0):
            continue
        data.append(sheet.row_values(i))
    return data

def date_n(n):
    return str(date.today() + timedelta(days=int(n))) #导入偏移量，如后天就传2加今天时间

if __name__ == '__main__':
    print(read_excel("../data/data.xlsx"))