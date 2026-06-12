# -*- coding: utf-8 -*-
"""生成四级考前速查PDF — 翻译词汇 + 逻辑关系词"""
from fpdf import FPDF
from fpdf.enums import XPos, YPos

FONT = r'C:\Windows\Fonts\msyh.ttc'

def make_pdf(md_path, title, subtitle, pdf_path):
    with open(md_path, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    pdf = FPDF()
    pdf.add_font('CJK', '', FONT)
    pdf.set_auto_page_break(True, 15)
    pdf.add_page()
    
    # Title
    pdf.set_font('CJK', '', 18)
    pdf.cell(0, 12, title, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_font('CJK', '', 10)
    pdf.set_text_color(100,100,100)
    pdf.cell(0, 8, subtitle, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    pdf.set_text_color(0,0,0)
    pdf.ln(4)
    
    in_table = False
    for line in lines:
        line = line.rstrip()
        
        # Skip HTML-style comments
        if '<!-' in line or '```' in line:
            continue
        
        # Section header
        if line.startswith('## '):
            pdf.ln(4)
            pdf.set_font('CJK', '', 13)
            pdf.set_text_color(200, 130, 0)
            pdf.cell(0, 8, line[3:], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.set_text_color(0,0,0)
            pdf.set_font('CJK', '', 10)
            continue
        
        if line.startswith('### '):
            pdf.ln(2)
            pdf.set_font('CJK', '', 11)
            pdf.cell(0, 7, '  ' + line[4:], new_x=XPos.LMARGIN, new_y=YPos.NEXT)
            pdf.set_font('CJK', '', 10)
            continue
        
        # Table
        if line.startswith('|') and '|' in line[1:]:
            cells = [c.strip() for c in line.split('|')[1:-1]]
            if all(c.startswith('-') for c in cells):
                in_table = True
                continue
            if all(c == '' for c in cells):
                continue
            if in_table or len(cells) >= 2:
                in_table = True
                # Calculate column widths
                n = len(cells)
                w = 180 // n
                for i, cell in enumerate(cells):
                    clean = cell.replace('★','').replace('**','').strip()
                    pdf.set_font('CJK', '', 9)
                    if i == n-1:
                        pdf.cell(w, 7, clean, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                    else:
                        pdf.cell(w, 7, clean)
            continue
        else:
            in_table = False
        
        # Regular text
        if line.strip() and not line.startswith('>') and not line.startswith('-'):
            # Clean bold markers
            clean = line.strip()
            if clean.startswith('- ') and '→' in clean:
                pdf.set_font('CJK', '', 9)
                pdf.set_x(15)
                pdf.cell(170, 6, clean, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
                pdf.set_font('CJK', '', 10)
            elif clean and not clean.startswith('#'):
                pdf.set_font('CJK', '', 10)
                pdf.cell(0, 6, clean, new_x=XPos.LMARGIN, new_y=YPos.NEXT)
    
    pdf.output(pdf_path)
    print(f'✅ {pdf_path}')

if __name__ == '__main__':
    base = r'd:\英语四级备战\备考资料'
    
    make_pdf(
        base + r'\考前速查_翻译词汇.md',
        '🌐 四级翻译 · 核心词汇',
        '来源: GitHub KyleBing/english-vocabulary + China Daily | 2026.06.12',
        base + r'\考前速查_翻译词汇.pdf'
    )
    
    make_pdf(
        base + r'\考前速查_逻辑关系词.md',
        '🔗 四级作文 · 逻辑关系词',
        '来源: 简书·奇速教育 (2026.06.03) + GitHub CET-Prompt-Hub',
        base + r'\考前速查_逻辑关系词.pdf'
    )
