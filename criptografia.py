def deslocamento_tres_letras(mensagem):
    resultado_mensagem = ""
    for i in range(0, len(mensagem)):
        codigo = ord(mensagem[i])
        if (codigo >= 65 and codigo <= 90 or codigo >= 97 and codigo <= 122):
            codigo += 3
            resultado_mensagem += chr(codigo)
        else:
            resultado_mensagem += chr(codigo)
    return resultado_mensagem

def inverter_frase(mensagem):
    mensagem_segunda_passada = ""
    for i in range(-1, -(len(mensagem)+1), -1):
        mensagem_segunda_passada += mensagem[i]
    return mensagem_segunda_passada

def deslocamento_metade_frase(mensagem):
    resultado_mensagem = ''
    for i in range(0, len(mensagem)):
            codigo_dois = ord(mensagem[i])
            if(i >= len(mensagem)//2):
                codigo_dois -= 1
                resultado_mensagem += chr(codigo_dois)
            else:
                resultado_mensagem += chr(codigo_dois)
    return resultado_mensagem

def main():
    qtd_linhas = int(input(""))
    for i in range(0, qtd_linhas):
        mensagem_original = input("")
        primeiro_estagio_cripto = deslocamento_tres_letras(mensagem_original)
        segundo_estagio_cripto = inverter_frase(primeiro_estagio_cripto)
        terceiro_estagio_cripto = deslocamento_metade_frase(segundo_estagio_cripto)
        print(terceiro_estagio_cripto)
main()