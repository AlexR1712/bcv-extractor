import xlrd
import csv
from glob import glob
from datetime import datetime

data = []
def get_files():
    files = glob('files/*.xls')
    return files

def extract(file):
    wb = xlrd.open_workbook(file)
    print("Archivo: {1}: El número de hojas es {0}".format(wb.nsheets, file))
    for i in range(wb.nsheets):
        sheet = wb.sheet_by_index(i)
        sheetname = sheet.name
        currency = sheet.cell_value(14, 1)
        buy = sheet.cell_value(14, 5)
        sell = sheet.cell_value(14, 6)
        date_time_obj = datetime.strptime(sheetname, '%d%m%Y')
        data.append([date_time_obj.strftime('%d/%m/%Y') , sheetname, currency, buy, sell])


def writeCsv(data):
    with open('dataset.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(data)

def main():
    files = get_files()
    for file in files:
        extract(file)
    writeCsv(data)
    



if __name__ == "__main__":
    main()