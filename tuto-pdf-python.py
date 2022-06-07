# -*- coding: utf-8 -*-
"""
Created on Sun May 22 18:23:48 2022

@author: Samson Thibaut

pip install fpdf

"""

from fpdf import FPDF

pdf_w = 137
pdf_h=100
pdf = FPDF(orientation='P', unit='mm', format='A5')
pdf.add_page()
pdf.rect(5.0, 5.0, pdf_w, pdf_h)
pdf.set_font('Arial', 'B', 25)
pdf.cell(pdf_w, 10, txt='[PDF] Editic in Python', ln=1, align='C')
pdf.set_font("Arial", size=12)
pdf.cell(pdf_w, 10, txt='Written by Samson', ln=2, align='C')
pdf.cell(pdf_w, 10, txt="\nA place for a python's programmers "+
         "to generate a pdf document...", ln=3, align='L')
pdf.image('0.png', 10, 10, 10, 10)
pdf.cell(pdf_w, 55, txt="", ln=4, align='C')
pdf.cell(pdf_w, 10, txt="\xa9 Samson Thibaut.", ln=5, align='C')
pdf.output('data.pdf')



"""class PDF(FPDF):
    def lines(self):
        self.set_line_width(0.0)
        self.line(0,pdf_h/2,210,pdf_h/2)
        self.set_line_width(0.0)
        self.line(5.0,5.0,205.0,5.0) # top one
        self.line(5.0,292.0,205.0,292.0) # bottom one
        self.line(5.0,5.0,5.0,292.0) # left one
        self.line(205.0,5.0,205.0,292.0) # right one
        self.rect(5.0, 5.0, 200.0,287.0)

pdf = PDF()#pdf object
pdf=PDF(orientation='L') # landscape
pdf=PDF(unit='mm') #unit of measurement

pdf=PDF(format='A4') #page format. A4 is the default value of the format, you don't have to specify it.
# full syntax
PDF(orientation={'P'(def.) or 'L'}, measure{'mm'(def.),'cm','pt','in'}, format{'A4'(def.),'A3','A5','Letter','Legal')
#default
pdf = PDF(orientation='P', unit='mm', format='A4')

pdf.add_page()
pdf.output('test.pdf','F')

pdf_w=210
pdf_h=297"""