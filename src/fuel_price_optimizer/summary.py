from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import textwrap

def save_summary(text, path):
    c = canvas.Canvas(str(path), pagesize=A4)
    width, height = A4
    text_obj = c.beginText(40, height - 50)
    text_obj.setFont("Helvetica", 10)

    for line in text.split("\n"):
        for wrapped in textwrap.wrap(line, 100):
            text_obj.textLine(wrapped)
        text_obj.textLine("")

        if text_obj.getY() < 50:
            c.drawText(text_obj)
            c.showPage()
            text_obj = c.beginText(40, height - 50)
            text_obj.setFont("Helvetica", 10)

    c.drawText(text_obj)
    c.save()
