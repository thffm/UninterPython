def menu():
    print()
    print("Entre com o tipo de servico desejado")
    print("DIG - Digitalizacao")
    print("ICO - Impressao colorida")
    print("IPB - Impressao preto e branco")
    print("FOT - Fotocopia")
    print()

def escolha_servico():

    choice = input().upper()

    if choice not in services:
        #retorna None casa seja invalida a escolha
        print("Escolha Invalida\n.Entre com o tipo de servico desejado novamente.")
        return None
    return choice


def num_paginas(choice):
    print("Entre com o numero de paginas: ")
    value = services[choice]

    numbers_pages = int(input())
    total_page = 0

    if numbers_pages < 20 and numbers_pages > 0:
        total_page = numbers_pages

    elif numbers_pages >= 20 and numbers_pages < 200:
        total_page += numbers_pages - (15 / 100 * numbers_pages)

    elif numbers_pages >= 200 and numbers_pages < 2000:
        total_page += numbers_pages - (20 / 10 * numbers_pages)

    elif numbers_pages >= 2000 and numbers_pages < 20000:
        total_page += numbers_pages - (25 / 100 * numbers_pages)

    else:
        print("Nao aceitamos tantas paginas de uma vez.")
        return None
    return total_page



def servico_extra():
    print("Deseja adiconar mais algum servico?")
    print("1 - Encadernacao Simples - R$ 10,00")
    print("2 - Encadernacao capa dura - R$ 25,00")
    print("0 - Nao desejo mais nada")
    choice = int(input())
    if choice in extra_services:
        return extra_services[choice]
    return

services = {"DIG": 1.10, "ICO": 1.00, "IPB": 0.4, "FOT": 0.2} #utilizando dict para deixar mais profissional e legivel
extra_services = {1: 10.00, 2: 25.00}


print("Bem vindo ao petshop do thiago ")

while True:
    menu()
    service = escolha_servico()
    if service is None:
        while True:
            menu()
            service = escolha_servico()
            if(service != None):
                break
    value_pages = num_paginas(service)
    if(value_pages is None):

        while True:
            try:
                value_pages/0
            except:
                value_pages = num_paginas(service)
                if(value_pages != None):
                    break


    extra_price = servico_extra()
    if extra_price != None:
        print(f"Total (R$): {services[service] * value_pages + extra_price:.2f} (servico: {services[service]} * "
              f"paginas: {value_pages} + extras (s): {extra_price} ")
    else:
        print(f"Total (R$): {services[service] * value_pages:.2f} (servico: {services[service]} * "
            f"paginas: {value_pages} extras(n)  ")
    break










