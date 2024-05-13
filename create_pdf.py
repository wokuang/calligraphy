from reportlab.lib.pagesizes import letter
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.pdfbase import pdfmetrics

font_path = "edukai-5.0.ttf"
pdfmetrics.registerFont(TTFont("TW-MOE-Std-Kai", font_path))
font_fmaily = "TW-MOE-Std-Kai"

def create_pdf(first_line, lines, filename):
    print(f'start to create_pdf: {filename}')
    c = canvas.Canvas(filename, pagesize=letter)
    
    c.setFont(font_fmaily, 12)
    print_title = True
    
    # lines = text.split('\n')
    y = 750
    for line in lines:
        if y < 100:
            c.showPage()
            c.setFont(font_fmaily, 12)
            y = 750
        c.drawString(100, y, line)
        y -= 15

    c.save()
    print(f'create_pdf: {filename} done')

