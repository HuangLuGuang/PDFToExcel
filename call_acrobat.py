from win32com.client import Dispatch, DispatchEx
from win32com.client.dynamic import ERRORS_BAD_CONTEXT
import winerror

global ERRORS_BAD_CONTEXT
ERRORS_BAD_CONTEXT.append(winerror.E_NOTIMPL)

import os
pdf_path = r"E:\code\PDFToExcel\pdfs\C29USD-4000059506     创源(1).pdf"
out_path = r"E:\code\PDFToExcel\pdfs"
# avDoc = Dispatch("AcroExch.AVDoc")  # Connect to Adobe Acrobat
avDoc = DispatchEx("AcroExch.AVDoc")  # Connect to Adobe Acrobat
ret = avDoc.Open(os.path.abspath(pdf_path), "") # 需要绝对路径，否则找不到文件
assert ret

pdDoc = avDoc.GetPDDoc()
jsObject = pdDoc.GetJSObject()

# out_path, out_type
jsObject.SaveAs(os.path.abspath(os.path.join(out_path, '2201210024.xlsx')), "com.adobe.acrobat.xlsx")

pdDoc.Close()
avDoc.Close(True)