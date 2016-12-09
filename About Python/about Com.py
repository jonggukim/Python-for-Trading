

class CpStockCode:
    def __init__(self):
        self.stocks = {'유한양행':'A000100'}
    def GetCount(self):
        return len(self.stocks)
    def NameToCode(self, name):
        return self.stocks[name]


# internet explorer 사용하기
import win32com.client

explore = win32com.client.Dispatch("InternetExplorer.Application")
explore.Visible = True

# word 사용하기
import win32com.client

word = win32com.client.Dispatch("Word.Application")
word.Visible = True

# excel 사용하기.
import win32com.client
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True

# 생성된 엑셀에 쉬트 추가 하기 :sheet1
wb = excel.Workbooks.Add()
ws = wb.Worksheets("Sheet1")

# 특정한이름으로 쉬트 생성하기 : hello
wb = excel.Workbooks.Add()
ws = wb.Worksheets.add()
ws.Name = "hello"


# worksheet ( "sheet1")에 데이터 추가하기
ws.Cells(1, 1).Value = "hello world"


# 저장된 내용을 text.xlsx 파일로 저장하고 엑셀 닫기.
wb.SaveAs('c:\\Users\\Jason\\Desktop\\test.xlsx')
excel.Quit()

'''
# 기존 엑셀 파일을 열고 1.1에 있는 데이터를 읽기.
excel = win32com.client.Dispatch("Excel.Application")
excel.Visible = True
wb = excel.Workbooks.Open('C:\\Users\\Jason\\Desktop\\input.xlsx')
ws = wb.ActiveSheet
ws.Cells(1,2).Value = "is"                             # 1행 2열 (=B1)에 is 추가
ws.Range("C1").Value = "good"                          # C행 1열에 good 추가
ws.Range("C1").Interior.ColorIndex = 10                # C행 1열의 생상 변경
ws.Range("A2:C2").Interior.ColorIndex = 27             # A2 부터 C2까지의 범위의 색상 변경경print(ws.Cells(1,1).Value)
excel.Quit()

'''




