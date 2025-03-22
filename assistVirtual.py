# Criando um assistente virtual 
import speech_recognition as sr #biblioteca usada nessa aplicaçãozinha e responsavel por ter toda IA e ser uma biblioteca de reconhecimento de VOZ completa
import os

# função para ouvir e reconhecer a fala 
def ouvir_microfone():
    # habilitando o microfone do usuário 
    microfone = sr.Recognizer()

    # usando o microfone
    with sr.Microphone() as source:
        # chamando um algoritmo de redução de ruidos no som
        microfone.adjust_for_ambient_noise(source)

        # frase para o usuário falar algo
        print("Fale alguma coisa: ")

        # armazena o que foi dito numa variável 
        audio = microfone.listen(source)
        
    try:
        # passando a variável para o algoritmo reconhecedor de padrões
        frase = microfone.recognize_google(audio, language='pt-BR')

        # Se "navegador" foi dito, abre o Chrome
        if "navegador" in frase:
            os.system("start Brave.exe")

        # Se "Excel" foi dito, abre o Excel
        elif "Excel" in frase:
            os.system("start Excel.exe")    

        # Retorna a frase pronunciada
        print("Você disse: " + frase)

    except sr.UnknownValueError:
        print("Não entendi")  # Se não reconheceu a fala

    except sr.RequestError:
        print("Não consegui me conectar ao serviço de reconhecimento de fala.")  # Falha de conexão com o Google

    return frase

# Chama a função para testar
ouvir_microfone()
