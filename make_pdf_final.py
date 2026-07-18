from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 15)
        self.cell(0, 10, 'NEURA STUDIO - Official Master Syntax Guide', 0, 1, 'C')
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", size=12)
pdf.cell(200, 10, txt="Chief Architect: JAVED", ln=True, align='C')
pdf.ln(10)

# 91 Syntax Dictionary
pdf.set_font("Arial", 'B', 14)
pdf.cell(200, 10, txt="The 91 Master Syntax Dictionary", ln=True)
pdf.set_font("Courier", size=10)
for i in range(1, 92):
    pdf.cell(200, 7, txt=f"{i}. Nova.module_{i}.execute() - Native Apex Performance Execution", ln=True)

pdf.output("Nova_Master_Syntax_Final.pdf")
print("✅ PDF generated successfully without errors!")
