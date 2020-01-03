import openpyxl
import os
print(os.getcwd())

wb = openpyxl.load_workbook("example.xlsx")
wb.get_active_sheet()
ws = wb.get_active_sheet()
ws.iter_cols()
openpyxl.utils.cell.get_column_interval(start=2, end=5)
