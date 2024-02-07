import ping3

def check_online_status(hostname):
    response_time = ping3.ping(hostname)
    if response_time is not None:
        print(f"{hostname} está online. Tempo de resposta: {response_time} ms")
    else:
        print(f"{hostname} está offline.")

# Range de IPs
start_ip = "10.255.103.139"
end_ip = "10.255.103.150"

# Obter partes do endereço IP
start_parts = start_ip.split('.')
end_parts = end_ip.split('.')

# Converter partes em inteiros
start_octets = [int(part) for part in start_parts]
end_octets = [int(part) for part in end_parts]

# Iterar sobre os endereços IP
for i in range(start_octets[3], end_octets[3] + 1):
    ip = '.'.join(start_parts[:3] + [str(i)])
    check_online_status(ip)
