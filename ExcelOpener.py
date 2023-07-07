import xlsxwriter

def open_workbook():
    workbook = xlsxwriter.Workbook("..\DataCollection.xlsx")
    return workbook