from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'NEURA STUDIO - Official Documentation', 0, 1, 'C')

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Chief Architect: JAVED", ln=True, align='C')
pdf.ln(20)
pdf.set_font("Arial", 'B', 16)
pdf.cell(200, 10, txt="Chapter 1: The Apex Engine", ln=True)
pdf.set_font("Arial", size=12)
pdf.multi_cell(0, 10, txt="Nova is a high-performance language. Designed for speed, it bypasses the OS kernel directly using the NeuraVM.")
pdf.output("Nova_Master_Guide_Fast.pdf")
print("✅ PDF generated instantly!")
