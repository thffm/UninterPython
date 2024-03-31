name = "thiago"
ru = 4613941


def discount_price(param_value: float, param_unit: int):
    """
    funcao que faz o calculo do desconto e aplica ele retornando um valor final ja com desconto
    :param param_value:float
    :param param_unit: integer
    :return:

    """

    value_unit = param_value * param_unit
    if value_unit < 2500.00:
        return value_unit, 0
    elif 2500.00 <= value_unit < 6000.00:
        return value_unit - (4 / 100 * value_unit), 4
    elif 6000.00 <= value_unit < 10000.00:
        return value_unit - (7 / 100 * value_unit), 7
    return value_unit - (11 / 100 * value_unit), 11


print(f"Bem-Vindo a Loja do < {name} Ru: {ru} >")  # utilizando f string pois acho mais pratico
value = float(input("Entre com o valor unitario do produto: R$ "))
unit = int(input("Entre com a quantidade do produto: "))
print(f"O valor sem desconto foi R${value * unit}")
discount = discount_price(value, unit)  # funcao para retornar o valor final e a porcentagem
print(f"O valor com desconto foi R${discount[0]} (desconto {discount[1]}%)")
