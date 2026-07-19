from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 24)
        self.set_text_color(0, 207, 255) # Nova Blue
        self.cell(0, 15, 'NEURA STUDIO', 0, 1, 'C')
        self.set_font('Arial', 'B', 14)
        self.set_text_color(50, 50, 50)
        self.cell(0, 10, 'Nova Apex Engine - Master Syntax Guide', 0, 1, 'C')
        self.line(20, 35, 190, 35)
        self.ln(15)

    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 10)
        self.set_text_color(128, 128, 128)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = PDF()
pdf.add_page()

pdf.set_font("Arial", 'B', 16)
pdf.set_text_color(17, 17, 17)
pdf.cell(0, 10, "1. Core Philosophy (Bypass Reality)", 0, 1)
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8, "Nova is designed to completely bypass OS-level abstraction. By speaking directly to the CPU through NeuraVM, it achieves sub-millisecond (0.01ms) execution speeds.")
pdf.ln(10)

pdf.set_font("Arial", 'B', 16)
pdf.cell(0, 10, "2. The Master Syntaxes", 0, 1)
pdf.ln(5)

for i in range(1, 21):
    pdf.set_fill_color(245, 245, 245)
    pdf.set_font("Courier", 'B', 12)
    pdf.set_text_color(0, 0, 0)
    pdf.cell(0, 10, f" Module {i}: Advanced Execution", 0, 1, fill=True)
    
    pdf.set_font("Courier", '', 11)
    pdf.set_text_color(80, 80, 80)
    code = f" Nova.module_{i}.execute(threads=16)\n Nova.show('Process {i} compiled natively.')"
    pdf.multi_cell(0, 8, code, fill=True)
    pdf.ln(5)

pdf.output("Nova_Syntax_Master_Guide.pdf")
print("✅ PDF Generated: Nova_Syntax_Master_Guide.pdf")
