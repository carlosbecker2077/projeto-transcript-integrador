"""
Arquivo de funções utilizadas
"""
import os
import base64
from subprocess import call
from fpdf import FPDF


class Pdf(FPDF):
    """classe customizada do FPDF"""

    def header(self):
        # font
        self.set_font('arial', 'B', 20)
        # title
        self.cell(0, 10, 'Transcrição', border=False, ln=True, align='C')
        # line break
        self.ln(20)

    # content
    def body(self, name):
        #self.cell(0, 10)
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
        self.set_font('arial', '', 10)
        # page number
        self.cell(0, 10, f'Página {self.page_no()}/{{nb}}', align='C')


def run_file(file):
    """Função que executa outros scripts"""
    call(["python", file])


def create_download_link(val, filename):
    """Função que gera o link para download do pdf"""
    b64 = base64.b64encode(val)
    return f'<a href="data:application/octet-stream;base64,{b64.decode()}" download="{filename}.pdf">Download</a>'


def save_video(file_result):
    if file_result is not None:
        with open(os.path.join("videos", "uploaded_video.mp4"), "wb") as video:
            video.write(file_result.getbuffer())
