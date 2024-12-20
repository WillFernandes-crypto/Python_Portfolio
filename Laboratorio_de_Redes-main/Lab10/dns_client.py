import socket

def cliente_dns():
    # Cria um socket UDP
    cliente_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Endereço e porta do servidor DNS
    servidor_endereco = 'localhost'
    servidor_porta = 53

    # Solicita o nome do servidor ao usuário
    servidor_nome = input("Digite o nome do servidor: ")

    # Envia o nome do servidor para o servidor DNS
    cliente_socket.sendto(servidor_nome.encode(), (servidor_endereco, servidor_porta))

    # Aguarda a resposta do servidor DNS
    resposta, _ = cliente_socket.recvfrom(1024)
    resposta_decodificada = resposta.decode()

    # Exibe a resposta do servidor DNS
    print(resposta_decodificada)

    # Verifica se o servidor foi encontrado
    if resposta_decodificada.startswith("Servidor encontrado"):
        mensagem_dns = input("Digite a mensagem a ser enviada ao servidor DNS: ")

        # Envia a mensagem para o servidor DNS
        cliente_socket.sendto(mensagem_dns.encode(), (servidor_endereco, servidor_porta))

        # Aguarda a resposta do servidor DNS
        resposta_servidor, _ = cliente_socket.recvfrom(1024)
        print(resposta_servidor.decode())

    cliente_socket.close()

if __name__ == '__main__':
    cliente_dns()
