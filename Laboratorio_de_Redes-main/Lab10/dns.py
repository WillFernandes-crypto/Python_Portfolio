import socket

tabela_dns = {
    "Alice": ("192.168.0.100", 60502),
    "Wilson": ("192.168.0.101", 60503),
    "Joao": ("192.168.0.102", 60504)
}

def servidor_dns():
    # Cria um socket UDP
    servidor_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Endereço e porta do servidor DNS
    servidor_endereco = 'localhost'
    servidor_porta = 53

    # Associa o socket ao endereço e porta do servidor
    servidor_socket.bind((servidor_endereco, servidor_porta))
    print(f"Servidor DNS iniciado em {servidor_endereco}:{servidor_porta}")

    while True:
        # Aguarda por requisições DNS
        mensagem, cliente_endereco = servidor_socket.recvfrom(1024)
        requisicao = mensagem.decode().strip()

        if requisicao in tabela_dns:
            ip, porta = tabela_dns[requisicao]
            resposta = f"Servidor encontrado: {requisicao} ({ip}:{porta})"

            # Envia a resposta de volta para o cliente
            servidor_socket.sendto(resposta.encode(), cliente_endereco)

            # Aguarda pela mensagem do cliente
            mensagem_cliente, cliente_endereco = servidor_socket.recvfrom(1024)
            mensagem_decodificada = mensagem_cliente.decode()

            # Processa a mensagem somente se o servidor for encontrado
            if mensagem_decodificada:
                print(f"Mensagem recebida do cliente para {requisicao}: {mensagem_decodificada}")
                
                # Envia a mensagem para o servidor correto (Alice, Wilson ou Joao)
                servidor_destino = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
                servidor_destino.sendto(mensagem_decodificada.encode(), ('127.0.0.1', porta))

                # Aguarda pela resposta do servidor correto
                resposta_servidor, _ = servidor_destino.recvfrom(1024)
                resposta_cliente = resposta_servidor.decode()

                # Envia a resposta ao cliente
                servidor_socket.sendto(resposta_cliente.encode(), cliente_endereco)
        else:
            resposta = f"Servidor não encontrado na tabela DNS"

            # Envia a resposta de volta para o cliente
            servidor_socket.sendto(resposta.encode(), cliente_endereco)

if __name__ == '__main__':
    servidor_dns()
