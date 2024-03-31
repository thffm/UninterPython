def menu():
    #menu inicial
    size_menu = 20
    left_right_size = 5
    print("   Bem-vindo a Loja de Gelados do Thiago th")
    print(size_menu*"-"+"Cardapio"+size_menu*"-")
    print(left_right_size*"-"+"| "+"Tamanho | Cupuaçu (CP) | Açai (AC) |"+left_right_size*"-")
    print(left_right_size * "-" + "| " + "   P    |   R$ 10,00   |  R$ 12,00 |" + left_right_size * "-")
    print(left_right_size * "-" + "| " + "   M    |   R$ 15,00   |  R$ 17,00 |" + left_right_size * "-")
    print(left_right_size * "-" + "| " + "   G    |   R$ 19,00   |  R$ 21,00 |" + left_right_size * "-")
    print(size_menu*"-"+8*"-"+size_menu*"-")


flavors = {"AC": "Açai",  "CP": "Cupuaçu"}
price_cp = {"P": 10.00, "M": 15.00, "G": 19.00}
price_ac = {"P": 12.00, "M": 17.00, "G": 21.00}
total = 0
menu()
while True:
    print("Entre com o sabor desejado (CP/AC):")
    choice = input().upper()#para evitar que digite algo diferente do esperado
    if choice in flavors:
        print()
        print("Entre com o tamanho desejado (P/M/G): ")
        choice_flavor = input().upper()
        if choice_flavor in price_cp and choice == "CP":
            print(f"Voce pediu {flavors[choice]} no tamanho {choice_flavor}: R$ {price_cp[choice_flavor]} ")
            total += price_cp[choice_flavor]
            continue_ = input("Deseja mais alguma coisa(s/digite outra tecla) ?: ").upper()
            if(continue_ != "S"):
                break
        elif choice_flavor in price_ac and choice == "AC":
            print(f"Voce pediu {flavors[choice]} no tamanho {choice_flavor}: R$ {price_ac[choice_flavor]} ")
            total += price_ac[choice_flavor]
            continue_ = input("Deseja mais alguma coisa(s/digite outra tecla) ?: ").upper()
            if (continue_ != "S"):
                break
        else:
            print("Tamanho invalido. Tente novamente")


    else:
        print("Sabor invalido. Tente novamente ")

if total > 0:
    print(f"O valor total a ser pago: R${total}")
