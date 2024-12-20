import socket

def servidor_alice():
    # Cria um socket UDP
    servidor_alice_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Endereço e porta do servidor Alice
    servidor_alice_endereco = '127.0.0.1'
    servidor_alice_porta = 60502

    # Associa o socket ao endereço e porta do servidor Alice
    servidor_alice_socket.bind((servidor_alice_endereco, servidor_alice_porta))
    print(f"Servidor Alice iniciado em {servidor_alice_endereco}:{servidor_alice_porta}")

    while True:
        # Aguarda pela mensagem do servidor DNS
        mensagem, dns_endereco = servidor_alice_socket.recvfrom(1024)
        mensagem_decodificada = mensagem.decode()

        # Processa a mensagem recebida do servidor DNS
        print(f"Mensagem recebida do servidor DNS: {mensagem_decodificada}")

        # Realiza a lógica de processamento desejada
        resposta_alice = "Chamada Atendida de Alice"

        # Envia a resposta de volta para o servidor DNS
        servidor_alice_socket.sendto(resposta_alice.encode(), dns_endereco)

        # Verifica se a mensagem é proveniente do cliente
        if dns_endereco[0] != servidor_alice_endereco:
            # Encaminha a mensagem para o próprio servidor Alice (127.0.0.1)
            servidor_alice_socket.sendto(mensagem, (servidor_alice_endereco, servidor_alice_porta))

if __name__ == '__main__':
    servidor_alice()

