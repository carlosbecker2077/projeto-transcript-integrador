from fpdf import FPDF


class Pdf(FPDF):
    def header(self):
        # font
        self.set_font('helvetica', 'B', 20)
        # title
        self.cell(0, 10, 'Transcrição', border=False, ln=True, align='C')
        # line break
        self.ln(20)

    # content
    def body(self, name):
        # read text file
        with open(name, 'r') as fh:
            txt = fh.read()
        # set font
        self.set_font('arial', '', 12)
        # insert text
        self.multi_cell(0, 5, txt)
        # line break
        self.ln()

    def footer(self):
        # set position of the footer
        self.set_y(-15)
        self.set_font('helvetica', '', 10)
        # page number
        self.cell(0, 10, f'Page {self.page_no()}/{{nb}}', align='C')


# create fpdf object
# layout ('P', 'L') portrait ou landscape
# Unit ('mm', 'cm', 'in') como eu vou medir as coisas do pdf
# format (A3, A4 (default), A5, Letter, Legal, (100, 150))
pdf = Pdf('P', 'mm', 'Letter')

# get total page number
pdf.alias_nb_pages()
pdf.set_auto_page_break(auto=True, margin=15)
# adicionar página
pdf.add_page()

# body
pdf.body('./textos/texto_ata.txt')


pdf.output('pdf_1.pdf')
