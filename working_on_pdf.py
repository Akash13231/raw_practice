# from fpdf import *
# from fpdf import FPDF
#
# pdf = FPDF(orientation='P', unit='pt', format='A4')
# pdf.add_page()
#
# #pdf.image('tiger.jpeg', w=80, h=50)
#
# pdf.set_font(family='Times', style='B', size=24)
# pdf.cell(w=0, h=50, txt="Malayan Tiger", align='C', ln=1)
#
# pdf.set_font(family='Times', style='B', size=14)
# pdf.cell(w=0, h=15, txt='Description', ln=1)
#
# pdf.set_font(family='Times', size=12)
# txt1 = """The Malayan tiger is a tiger from a specific population of the Panthera tigris tigris subspecies that is native to Peninsular Malaysia.[5] This population inhabits the southern and central parts of the Malay Peninsula and has been classified as critically endangered on the IUCN Red List since 2015. As of April 2014, the population was estimated at 80 to 120 mature individuals with a continuous declining trend"""
# pdf.multi_cell(w=0, h=15, txt=txt1)
#
# pdf.set_font(family='Times', style='B', size=14)
# pdf.cell(w=100, h=25, txt='Kingdom:')
#
# pdf.set_font(family='Times', size=14)
# pdf.cell(w=100, h=25, txt='Animalia', ln=1)
#
# pdf.set_font(family='Times', style='B', size=14)
# pdf.cell(w=100, h=25, txt='Phylum:')
#
# pdf.set_font(family='Times', size=14)
# pdf.cell(w=100, h=25, txt='Chordata', ln=1)
#
#
# pdf.output('output.pdf')
#
# ###################### GENERATING PDF FROM EXCEL SHEET ################
#
# import pandas
# from fpdf import FPDF
#
# df = pandas.read_excel('data.xlsx')
# # print(df)
#
# for index, row in df.iterrows():
#   pdf = FPDF(orientation='P', unit='pt', format='A4')
#   pdf.add_page()
#
#   pdf.set_font(family='Times', style='B', size=24)
#   pdf.cell(w=0, h=50, txt=row['name'], align='C', ln=1)
#
#   for column in df.columns[1:]:
#     pdf.set_font(family='Times', style='B', size=14)
#     pdf.cell(w=100, h=25, txt=f"{column.title()}:")
#
#     pdf.set_font(family='Times', size=14)
#     pdf.cell(w=100, h=25, txt=row[column], ln=1)
#
#
#   pdf.output(f"{row['name']}.pdf")
#
#
# ########### EXTRACT DATA FRM PDF #########
#
# import fitz
#
# with fitz.open("students.pdf") as pdf:
#   text = ''
#   for page in pdf:
#     text = text + page.get_text()
#     print(text)from PyPDF2 import PdfReader
#
# Path to your PDF file
from PyPDF2 import PdfReader
pdf_path = "students.pdf"

# Create a PdfReader object
reader = PdfReader(pdf_path)

# Extract and print text from each page
for page_num, page in enumerate(reader.pages, start=1):
    print(f"--- Page {page_num} ---")
    print(page.extract_text())

#
#
#
#
# ############ EXTRACT TABLE FRM PDF #######
#
# import tabula
#
# table = tabula.read_pdf('weather.pdf', pages=1)
#
# print(type(table[0]))
#
# table[0].to_csv('output.csv', index=None)