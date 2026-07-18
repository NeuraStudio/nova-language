from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font('Arial', 'B', 16)
        self.set_text_color(0, 207, 255)
        self.cell(0, 10, 'NEURA STUDIO - Official Nova Documentation', 0, 1, 'C')
        self.ln(5)
    def footer(self):
        self.set_y(-15)
        self.set_font('Arial', 'I', 8)
        self.set_text_color(100, 100, 100)
        self.cell(0, 10, f'Page {self.page_no()}', 0, 0, 'C')

pdf = PDF()
pdf.add_page()
pdf.set_font("Arial", 'B', 24)
pdf.set_text_color(0, 0, 0)
pdf.cell(0, 20, "Nova Engine Master Syntax Guide", 0, 1, 'C')
pdf.set_font("Arial", 'I', 14)
pdf.cell(0, 10, "Chief Architect: JAVED", 0, 1, 'C')
pdf.ln(10)

biodata = """ABOUT NOVA:
Nova is built to completely bypass traditional OS kernels. 
It allocates hardware threads dynamically to eliminate the Global Interpreter Lock (GIL). 
This enables true 0.01ms execution for AI models and complex backend architectures."""
pdf.set_font("Arial", '', 12)
pdf.multi_cell(0, 8, biodata)

syntax_counter = 1
for page in range(2, 49):
    pdf.add_page()
    pdf.set_font("Arial", 'B', 16)
    pdf.cell(0, 10, f"Chapter {page}: Engine Mechanics", 0, 1)
    pdf.ln(5)
    
    for _ in range(3): 
        if syntax_counter <= 91:
            pdf.set_fill_color(240, 240, 240)
            pdf.set_font("Courier", 'B', 12)
            pdf.cell(0, 10, f"Syntax #{syntax_counter}", 0, 1, fill=True)
            pdf.set_font("Courier", '', 11)
            code_block = f"// Standard Operation\nNova.module_{syntax_counter}.execute()\nNova.system.log('Module executed natively')"
            pdf.multi_cell(0, 8, code_block, fill=True)
            pdf.ln(10)
            syntax_counter += 1

pdf.output("Nova_Official_Documentation.pdf")
print("✅ Robust PDF Generated!")
