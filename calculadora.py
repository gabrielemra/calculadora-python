def calculadora():
    print("=== Calculadora ===")
    print("Digite 'sair' a qualquer momento para encerrar.\n")

    while True:
        num1_input = input("Digite o primeiro número (ou 'sair'): ")
        if num1_input.lower() == "sair":
            break

        operador = input("Digite a operação (+, -, *, /): ")
        num2_input = input("Digite o segundo número: ")

        try:
            num1 = float(num1_input)
            num2 = float(num2_input)
        except ValueError:
            print("Erro: digite números válidos.\n")
            continue

        if operador == "+":
            resultado = num1 + num2
        elif operador == "-":
            resultado = num1 - num2
        elif operador == "*":
            resultado = num1 * num2
        elif operador == "/":
            if num2 == 0:
                print("Erro: divisão por zero não é permitida.\n")
                continue
            resultado = num1 / num2
        else:
            print("Operador inválido.\n")
            continue

        print(f"Resultado: {resultado}\n")

    print("Calculadora encerrada. Até mais!")

calculadora()
