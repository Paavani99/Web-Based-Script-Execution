import xlrd
import json


def datasheet_xl():
    path= '.\\'

    wb1 = xlrd.open_workbook(path+'data1.xls')
    sheet1= wb1.sheets()[0]

    wb2 = xlrd.open_workbook(path+'data2.xls')
    sheet2= wb2.sheets()[0]

    wb3 = xlrd.open_workbook(path+ 'data3.xls')
    sheet3= wb3.sheets()[0]

    data= []

    for i in range(0,20):
        row=[]
        for j in {0,1,2}:
            temp = sheet1.cell_value(i,j)
            row.append(temp)
        for j in {1}:
            temp = sheet2.cell_value(i,j)
            row.append(temp)
        for j in {2,3}:
            temp = sheet3.cell_value(i,j)
            row.append(temp)
        data.append(row)

    
    return data


def pieChart_graph():
    data  = datasheet_xl()
    percentage = []
    for i in range(1,20):
       percentage.append(data[i][4]) 
   
    below30 =0 
    above70 = 0
    rest =0 

    for i in range(19):
        if percentage[i]<=30:
            below30 = below30+1
        elif percentage[i]>=70:
            above70= above70+1
        else:
            rest = rest+1
        
    # In data, add the titles of the columns in the 1st row, otherwise leave it empty []. 1st row
    # is reseved for titles, any data entered here would be left out of the graph.

    data= [['marks','number of students'], ["Below 30", below30], ["Above 70",above70], ["Between 30 and 70", rest]]
    
    pieChart = {
        "data" :data,
        "chartType": 'PieChart',
        "options" : {'title': 'Performance', 'width':500,
                       'height':400}
    }

    return pieChart

def pieChart2_graph():
    data  = datasheet_xl()
    percentage = []
    for i in range(1,20):
       percentage.append(data[i][4]) 
   
    below20 =0 
    above90 = 0
    rest =0 

    for i in range(19):
        if percentage[i]<=20:
            below20 = below20+1
        elif percentage[i]>=90:
            above90= above90+1
        else:
            rest = rest+1

    # In data, add the titles of the columns in the 1st row, otherwise leave it empty []. 1st row
    # is reseved for titles, any data entered here would be left out of the graph.
       
    data= [['marks','number of students'], ["Below 20", below20], ["Above 90",above90], ["Between 20 and 90", rest]]
    

    pieChart = {
        "data" :data,
        "chartType": 'PieChart',
        "options" : {'title': 'Performance', 'width':500,
                       'height':400}
    }

    return pieChart

def datasheet2_xl():
    path = '.\\'

    wb1 = xlrd.open_workbook(path+'data1.xls')
    sheet1= wb1.sheets()[0]

    wb2 = xlrd.open_workbook(path+'data2.xls')
    sheet2= wb2.sheets()[0]

    wb3 = xlrd.open_workbook(path+'data3.xls')
    sheet3= wb3.sheets()[0]

    data= []

    for i in range(0,20):
        row=[]
        for j in {0,1,3}:
            temp = sheet1.cell_value(i,j)
            row.append(temp)
        for j in {1}:
            temp = sheet2.cell_value(i,j)
            row.append(temp)
        for j in {1,3}:
            temp = sheet3.cell_value(i,j)
            row.append(temp)
        data.append(row)

    return data

