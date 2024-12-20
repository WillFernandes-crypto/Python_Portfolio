import time
import random
from socket import *

# Cria o socket UDP
clientSocket = socket(AF_INET, SOCK_DGRAM)

# Define o endereço e a porta do servidor
serverAddress = ('127.0.0.1', 50000)

# Configura o tempo limite (timeout) para 1 segundo
clientSocket.settimeout(1)

# Variáveis para o cálculo dos RTTs
rtt_min = float('inf')
rtt_max = 0
rtt_total = 0
received_count = 0

# Define a taxa de perda de pacotes
packet_loss_rate = 0.3

# Envia 10 pings para o servidor da seguinte forma:
# Sequência começa com o valor 1 inclusivo
# Vai até o valor 10 inclusivo
# Valor 11 é exclusivo
# Logo, conta-se de 1 a 10, oara os pings
for sequence_number in range(1, 11):
    # Gera um número aleatório entre 0 e 1
    random_number = random.uniform(0, 1)

    if random_number < packet_loss_rate:
        # Pacote perdido, continua para o próximo ping
        print(f'Ping {sequence_number}: Request time out')
        continue

    # Obtém o tempo de envio do ping
    send_time = time.time()

    # Formata a mensagem do ping
    message = f'Ping {sequence_number} {send_time}'

    try:
        # Envia a mensagem para o servidor
        clientSocket.sendto(message.encode(), serverAddress)

        # Espera pela resposta do servidor
        response, serverAddress = clientSocket.recvfrom(1024)

        # Obtém o tempo de recebimento do ping
        receive_time = time.time()

        # Calcula o tempo de ida e volta (RTT)
        rtt = receive_time - send_time

        # Atualiza os valores mínimo, máximo e total dos RTTs
        rtt_min = min(rtt_min, rtt)
        rtt_max = max(rtt_max, rtt)
        rtt_total += rtt

        # Incrementa o contador de pacotes recebidos
        received_count += 1

        # Imprime a resposta do servidor e o RTT
        print(f'Resposta do servidor: {response.decode()}')
        print(f'Tempo de ida e volta (RTT): {rtt} segundos')
    except timeout:
        # Caso ocorra timeout
        print(f'Ping {sequence_number}: Request time out')

# Calcula a taxa de perda de pacotes
actual_packet_loss_rate = (10 - received_count) / 10 * 100

# Imprime os valores mínimo, máximo e médio dos RTTs e a taxa de perda dos pacotes
rtt_average = rtt_total / received_count
print(f'\nEstatísticas do ping:')
print(f'RTT mínimo: {rtt_min} segundos')
print(f'RTT máximo: {rtt_max} segundos')
print(f'RTT médio: {rtt_average} segundos')
print(f'Taxa de perda de pacotes: {actual_packet_loss_rate}%')

# Fecha o socket do cliente
clientSocket.close()
