## PDF to Excel DEMO

[PDFConverter](https://github.com/houking-can/PDFConverter)
PDFConverter对Acrobat的调用封装为exe，可以用下面命令调用
```shell
PDFConvert.exe -i .\pdfs\A45RMB-4600017085-创源A厂.pdf -o .\output -f xlsx
```

- call_acrobat.py `使用pywin32, 完成对acrobat的调用`
- pdf_to_image.py `把PDF转换为图片`
- paddleocr_demo.py `使用paddleORC，对图片OCR`
- paddleocr_demo1.ipynb  `paddleORC jupyter`
- pdf2excel.ipynb  `pdfplumber 读取PDF内容，获取表格，文本等等`

[tr一个简单好用的离线ORC工具](https://github.com/myhub/tr)