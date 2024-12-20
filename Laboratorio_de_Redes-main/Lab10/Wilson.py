import socket

def servidor_wilson():
    # Cria um socket UDP
    servidor_wilson_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Endereço e porta do servidor Wilson
    servidor_Wilson_endereco = '127.0.0.1'
    servidor_Wilson_porta = 60503

    # Associa o socket ao endereço e porta do servidor Wilson
    servidor_wilson_socket.bind((servidor_Wilson_endereco, servidor_Wilson_porta))
    print(f"Servidor Wilson iniciado em {servidor_Wilson_endereco}:{servidor_Wilson_porta}")

    while True:
        # Aguarda pela mensagem do servidor DNS
        mensagem, dns_endereco = servidor_wilson_socket.recvfrom(1024)
        mensagem_decodificada = mensagem.decode()

        # Processa a mensagem recebida do servidor DNS
        print(f"Mensagem recebida do servidor DNS: {mensagem_decodificada}")

        # Realiza a lógica de processamento desejada
        resposta_Wilson = "Chamada Atendida de Wilson"

        # Envia a resposta de volta para o servidor DNS
        servidor_wilson_socket.sendto(resposta_Wilson.encode(), dns_endereco)

        # Verifica se a mensagem é proveniente do cliente
        if dns_endereco[0] != servidor_Wilson_endereco:
            # Encaminha a mensagem para o próprio servidor Wilson (127.0.0.1)
            servidor_wilson_socket.sendto(mensagem, (servidor_Wilson_endereco, servidor_Wilson_porta))

if __name__ == '__main__':
    servidor_wilson()
