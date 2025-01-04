def converter_temperatura(valor, unidade_origem, unidade_destino):
    if unidade_origem == 'C' and unidade_destino == 'F':
        return (valor * 9/5) + 32
    elif unidade_origem == 'F' and unidade_destino == 'C':
        return (valor - 32) * 5/9
    elif unidade_origem == 'C' and unidade_destino == 'K':
        return valor + 273.15
    elif unidade_origem == 'K' and unidade_destino == 'C':
        return valor - 273.15
    elif unidade_origem == 'F' and unidade_destino == 'K':
        return (valor - 32) * 5/9 + 273.15
    elif unidade_origem == 'K' and unidade_destino == 'F':
        return (valor - 273.15) * 9/5 + 32
    else:
        return "Unidade não suportada"


def converter_distancia(valor, unidade_origem, unidade_destino):
    fatores = {
        'm': 1,       # metro
        'km': 1000,   # quilômetro
        'cm': 0.01,   # centímetro
        'mm': 0.001,  # milímetro
        'mi': 1609.34,  # milha
        'yd': 0.9144,  # jarda
        'ft': 0.3048,  # pé
        'in': 0.0254   # polegada
    }

    if unidade_origem in fatores and unidade_destino in fatores:
        return valor * (fatores[unidade_origem] / fatores[unidade_destino])
    else:
        return "Unidade não suportada"


def converter_peso(valor, unidade_origem, unidade_destino):
    fatores = {
        'kg': 1,      # quilograma
        'g': 0.001,   # grama
        'mg': 0.000001,  # miligrama
        'lb': 0.453592,  # libra
        'oz': 0.0283495  # onça
    }

    if unidade_origem in fatores and unidade_destino in fatores:
        return valor * (fatores[unidade_origem] / fatores[unidade_destino])
    else:
        return "Unidade não suportada"


if __name__ == "__main__":
    print("Conversor de Unidades")
    print("1. Temperatura (C, F, K)")
    print("2. Distância (m, km, cm, mm, mi, yd, ft, in)")
    print("3. Peso (kg, g, mg, lb, oz)")

    opcao = int(input("Escolha uma opção: "))

    valor = float(input("Digite o valor a ser convertido: "))
    unidade_origem = input("Digite a unidade de origem: ").strip().lower()
    unidade_destino = input("Digite a unidade de destino: ").strip().lower()

    if opcao == 1:
        resultado = converter_temperatura(valor, unidade_origem.upper(), unidade_destino.upper())
    elif opcao == 2:
        resultado = converter_distancia(valor, unidade_origem, unidade_destino)
    elif opcao == 3:
        resultado = converter_peso(valor, unidade_origem, unidade_destino)
    else:
        resultado = "Opção inválida"

    print(f"Resultado: {resultado}")
