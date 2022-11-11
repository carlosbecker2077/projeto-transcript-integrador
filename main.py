import os
from os.path import exists
import streamlit as st
from utils import *

texto_pagina = ''

st.title('Bem-vindo ao Transcript!')
progress_bar = st.progress(0)

file_result = st.file_uploader(
    "Selecione o vídeo para transcrever", type=["mp4", "webm"])

# Salvando vídeo
save_video(file_result)

# Lógica do botão que processa o vídeo
if file_result is not None:
    bt_video = st.button('Processar vídeo')
    if bt_video:
        # Rodando o primeiro script
        progress_bar.progress(30)
        run_file("video_to_audio.py")
        progress_bar.progress(50)
        progress_bar.progress(70)
        # Rodando o segundo script
        run_file("audio_to_text.py")
        progress_bar.progress(90)
        progress_bar.progress(100)
        st.success('Concluído!')

if exists(os.path.join('textos', 'texto_ata.txt')):
    with open(os.path.join('textos', 'texto_ata.txt')) as txt:
        texto_pagina = txt.readlines()
    for linhas in texto_pagina:
        st.write(linhas)


if exists(os.path.join('textos', 'texto_ata.txt')):
    export_as_pdf = st.button("Fazer download")

    if export_as_pdf:
        pdf = Pdf('P', 'mm', 'Letter')
        pdf.alias_nb_pages()
        pdf.set_auto_page_break(auto=True, margin=15)
        pdf.add_page()
        pdf.body(os.path.join('textos', 'texto_ata.txt'))

        html = create_download_link(pdf.output(
            dest="S"), "transcript")

        st.markdown(html, unsafe_allow_html=True)
