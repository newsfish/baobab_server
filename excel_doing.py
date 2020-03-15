# coding:utf-8
from win32com.client import Dispatch
import win32com.client
import time

import sys
reload(sys)
sys.setdefaultencoding('utf-8')

excel = win32com.client.DispatchEx('Excel.Application')

excel.Visible = False
excel.DisplayAlerts = False

def order_queego():
    pass

try:
    myBook = excel.Workbooks.Open('C:/Users/Administrator/Desktop/上海曾小姐11-2(1).xls'.decode('utf-8'))
    mySheet = myBook.Worksheets(1)
    myBook.SaveAs('d:\\a.xlsx', FileFormat=51)
    for i in range(1, 10):
        for j in range(1, 10):
            if mySheet.Cells(i, j).Value is not None and '昆鸽' in str(mySheet.Cells(i, j).Value):
                order_queego()
    myBook.Close()
except Exception as ex:
    print(ex)
finally:
    excel.Quit()
pass

