# Importando biblioteca moviepy
import os
import moviepy.editor as mp

input_directory = "videos"
input_file_name = "uploaded_video.mp4"
output_directory = "audios"
output_file_name = "audio_video.wav"


# Setando o vídeo com a função VideoFileClip e armazenando na variável 'video_input'
video_input = mp.VideoFileClip(os.path.join(input_directory, input_file_name))

# Extraindo audio da variável 'video_input' e salvando com extensão '.wav'
# A extensão tem melhor desempenho na função de reconhecimento de voz, visando o reconhecimento de locutor
# Faz chamado da variável com a função 'audio.write_audiofile' para extrair arquivo final

video_input.audio.write_audiofile(
    # './audios/audio_video.wav'
    os.path.join(output_directory, output_file_name)
)
