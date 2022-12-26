import xlrd, json


def python1_xl():
    wb1 = xlrd.open_workbook('data1.xls')
    sheet1= wb1.sheets()[0]

    wb2 = xlrd.open_workbook('data2.xls')
    sheet2= wb2.sheets()[0]

    wb3 = xlrd.open_workbook('data3.xls')
    sheet3= wb3.sheets()[0]

    data= []

    for i in range(0,20):
        row=[]
        for j in {0,1}:
            temp = sheet1.cell_value(i,j)
            row.append(temp)
        for j in {1}:
            temp = sheet2.cell_value(i,j)
            row.append(temp)
        for j in {1,2}:
            temp = sheet3.cell_value(i,j)
            row.append(temp)
        data.append(row)

    return data

def grades_graph():
    sheet = python1_xl()
    data =[]
    for row in range(0,19):
        temp =[]
        for col in {1,3,4}:
            temp.append(sheet[row][col])
        data.append(temp)

    lineChart = {
        "data" :data,
        "chartType": 'LineChart',
        "options" : {
          'title': 'Performance in 10th and 12th',
          'curveType': 'function',
          'legend': "{ position: 'bottom' }"
        }

    }

    return lineChart


