from pyresparser import ResumeParser
import os
from docx import Document
##file format should be in .txt , .docx or .pdf only
filed=input()
try:
    doc = Document()
    with open(filed, 'r') as file:
        doc.add_paragraph(file.read())
    doc.save("resume.docx")
    data = ResumeParser('resume.docx').get_extracted_data()
    print(data['skills'])
except:
    data = ResumeParser(filed).get_extracted_data()
    print(data['skills'])