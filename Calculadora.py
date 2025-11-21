def calculadora():
    print("=== Calculadora Simples ===")
    print("Escolha a operação:")
    print("1 - Somar")
    print("2 - Subtrair")
    print("3 - Multiplicar")
    print("4 - Dividir")

    escolha = input("Digite o número da operação: ")
    try:
        n1 = float(input("Digite o primeiro número: "))
        n2 = float(input("Digite o segundo número: "))
    except ValueError:
        return "Erro: por favor digite números válidos!"

    if escolha == "1":
        resultado = n1 + n2
    elif escolha == "2":
        resultado = n1 - n2
    elif escolha == "3":
        resultado = n1 * n2
    elif escolha == "4":
        if n2 == 0:
            return "Erro: divisão por zero!"
        resultado = n1 / n2
    else:
        return "Opção inválida!"

    return f"Resultado: {resultado}"

if _name_ == "_main_":
    print(calculadora())
