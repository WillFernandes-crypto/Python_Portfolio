import socket

def servidor_Joao():
    # Cria um socket UDP
    servidor_Joao_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Endereço e porta do servidor Joao
    servidor_Joao_endereco = '127.0.0.1'
    servidor_Joao_porta = 60503

    # Associa o socket ao endereço e porta do servidor Joao
    servidor_Joao_socket.bind((servidor_Joao_endereco, servidor_Joao_porta))
    print(f"Servidor Joao iniciado em {servidor_Joao_endereco}:{servidor_Joao_porta}")

    while True:
        # Aguarda pela mensagem do servidor DNS
        mensagem, dns_endereco = servidor_Joao_socket.recvfrom(1024)
        mensagem_decodificada = mensagem.decode()

        # Processa a mensagem recebida do servidor DNS
        print(f"Mensagem recebida do servidor DNS: {mensagem_decodificada}")

        # Realiza a lógica de processamento desejada
        resposta_Joao = "Chamada Atendida de Joao"

        # Envia a resposta de volta para o servidor DNS
        servidor_Joao_socket.sendto(resposta_Joao.encode(), dns_endereco)

        # Verifica se a mensagem é proveniente do cliente
        if dns_endereco[0] != servidor_Joao_endereco:
            # Encaminha a mensagem para o próprio servidor Joao (127.0.0.1)
            servidor_Joao_socket.sendto(mensagem, (servidor_Joao_endereco, servidor_Joao_porta))

if __name__ == '__main__':
    servidor_Joao()
