
def decorator_imprimir(func): # criando a função
    def wrapper(capital, taxa, tempo): #função que retorna a original
        resultado = func(capital, taxa, tempo) #retornando os parametros e o resultado
        print(f'Capital:{capital}, Taxa:{taxa}, Tempo:{tempo}, Resultado:{resultado}')
        return resultado
    return wrapper

@decorator_imprimir # Utilizando o decorador
def juros_simples(capital, taxa, tempo): # realizando o calculo de juros
    return capital * (taxa / 100) * tempo

# entrada de dados
capital = float(input("Insira o valor do capital: "))
taxa = float(input("Insira o valor da taxa de juros: "))
tempo = float(input("Insira a quantidade de parcelas: "))

# resultado da simulação
juros_simples(capital, taxa, tempo)

juros_total = "Total com Juros: ", capital * (taxa / 100)  * tempo + capital
print(juros_total)