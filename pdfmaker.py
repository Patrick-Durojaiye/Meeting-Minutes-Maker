from fpdf import FPDF

def save_minutes(text):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=10)
    pdf.write(h=6, txt=text)
    pdf.output("minutes.pdf")
