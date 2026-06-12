# -*- coding: utf-8 -*-
"""从完整版MD生成PDF"""
from fpdf import FPDF
from fpdf.enums import XPos, YPos

FONT = r'C:\Windows\Fonts\msyh.ttc'

with open(r'd:\英语四级备战\备考资料\考前速查_完整版.md', 'r', encoding='utf-8') as f:
    content = f.read()

pdf = FPDF()
pdf.add_font('CJK', '', FONT)
pdf.set_auto_page_break(True, 12)
pdf.add_page()

for block in content.split('\n\n'):
    block = block.strip()
    if not block: continue
    lines = block.split('\n')
    
    if block.startswith('# ') and not block.startswith('## '):
        pdf.set_font('CJK', '', 16)
        pdf.set_text_color(180,130,0)
        pdf.cell(0,10,block[2:].strip(),new_x=XPos.LMARGIN,new_y=YPos.NEXT)
        pdf.set_text_color(0,0,0)
        pdf.ln(3); continue
    
    if block.startswith('## '):
        pdf.set_font('CJK','',12)
        pdf.set_text_color(140,80,0)
        pdf.cell(0,8,block[3:].strip(),new_x=XPos.LMARGIN,new_y=YPos.NEXT)
        pdf.set_text_color(0,0,0)
        pdf.ln(2); continue
    
    if block.startswith('### '):
        pdf.set_font('CJK','',10)
        pdf.set_text_color(100,100,100)
        pdf.cell(0,7,block[4:].strip(),new_x=XPos.LMARGIN,new_y=YPos.NEXT)
        pdf.set_text_color(0,0,0)
        pdf.ln(1); continue
    
    if all(l.startswith('- ') for l in lines):
        pdf.set_font('CJK','',7.5)
        for l in lines:
            pdf.cell(0,4.5,'  '+l[2:].strip(),new_x=XPos.LMARGIN,new_y=YPos.NEXT)
        pdf.ln(2); continue
    
    pdf.set_font('CJK','',9)
    for l in lines:
        clean = l.strip()
        if clean: pdf.cell(0,5,clean,new_x=XPos.LMARGIN,new_y=YPos.NEXT)
    pdf.ln(2)

pdf.output(r'd:\英语四级备战\备考资料\考前速查_完整版.pdf')
print('PDF done')
