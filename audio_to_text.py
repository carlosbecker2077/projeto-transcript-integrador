# Importando o SDK de Fala, e bibliotecas time e os
# O SDK de Fala fornece uma maneira de transmitir áudio para o reconhecedor como
# uma alternativa à entrada de microfone ou arquivo.
import azure.cognitiveservices.speech as speechsdk
from time import sleep
import os
import dotenv

# Carregando as variáveis de ambiente
dotenv.load_dotenv(dotenv.find_dotenv())
subscription_id = os.getenv("SUBSCRIPTION_ID")

# Lista para receber transcrição do áudio
transcript_text = []

# Variáveis de input de output de arquivo
input_directory = "audios"
input_audio_file = "audio_video.wav"
output_directory = "textos"
output_text_file = "texto_ata.txt"

# Inicializando o SpeechConfig
# Classe que define configurações para reconhecimento de fala/intenção e síntese de fala
# subscription = Recebendo chave de autenticação do Azure
# region = Recebendo local do servidor armazenado do Azure
speech_config = speechsdk.SpeechConfig(
    subscription=subscription_id, region='westus')

# Passagem de parâmetros para reconhecimento do idioma falado
speech_config.speech_recognition_language = 'pt-BR'


# Função 'def receive_file' que define recebimento do arquivo a ser inputado para transcrição
# Variável 'audio_input' recebe caminho do arquivo
# Método 'SpeechRecognizer()' recebe os parâmetros 'speech_config' e 'audio_config'
# Método 'start_continuous_recognition()' para início do reconhecimento contínuo
# Varíavel 'done' tem recebimento 'False', pois a leitura não está finalizada
def receive_file():
    audio_input = speechsdk.audio.AudioConfig(
        filename=os.path.join(input_directory, input_audio_file))

    speech_recognizer = speechsdk.SpeechRecognizer(
        speech_config=speech_config, audio_config=audio_input)

    speech_recognizer.start_continuous_recognition()

    done = False

    # Função 'def recognition' que inicia o recognition do áudio
    # Se houver alguma divergência na condição aplicada a expressão 'assert' para a execução do programa
    # o usuário será notificado a executar o procedimento novamente
    def recognition(evt):
        assert (
            evt.result.reason == speechsdk.ResultReason.RecognizedSpeech), 'Falha no reconhecimento. Tente ' \
            'novamente! '
        print('RECOGNIZED: {}'.format(evt))

    # Função 'def final_result' insere o texto transcrito na lista e salva em um arquivo txt
    # Variável 'file' recebe caminho para transcrever o texto
    # A estrutura de repetição 'for' é aplicada para iterar o texto armazenado na variável 'transcript_text'
    # para um arquivo '.txt'
    def final_result(evt):

        transcript_text.append(evt.result.text)
        file = open(
            os.path.join(output_directory, output_text_file), 'w')

        for c in transcript_text:
            file.write(str(c) + '\n')

    # Função 'def stop_callback' criada para informar fim da execução do reconhecimento
    # Método 'stop_continuous_recognition()' encerra de forma síncrona a operação de reconhecimento
    # contínuo em andamento.
    # 'Callback' é uma função de retorno, agindo de forma assíncrona, e não é executada imediatamente com o código.
    # Ela só será acionada quando for chamada dentro do código
    # nonlocal é usada para declarar a variável 'done' apresentada na função 'def receive_file' de forma local com o
    # objetivo de atribuir a variável como 'True' já que toda transformação de áudio e texto foi concluída
    def stop_callback(evt):
        print('CLOSING on {}'.format(evt))
        speech_recognizer.stop_continuous_recognition()
        nonlocal done
        done = True

    # Realizando chamado das funções aplicadas anteriormente
    speech_recognizer.recognized.connect(recognition)
    speech_recognizer.recognized.connect(final_result)
    speech_recognizer.session_stopped.connect(stop_callback)

    # A estrutura de repetição 'while not' com método 'sleep(0.5)', aguarda até que seja executado
    # a execução de todas as funções

    while not done:
        sleep(0.5)


# 'receive_file()', gera o output do código finalizado
receive_file()
