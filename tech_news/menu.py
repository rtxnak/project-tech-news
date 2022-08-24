import sys


# Requisito 12
def analyzer_menu():
    print(
        "Selecione uma das opções a seguir:\n 0 - Popular o banco com notícias"
        ";\n 1 - Buscar notícias por título;\n 2 - Buscar notícias por data;\n"
        " 3 - Buscar notícias por tag;\n 4 - Buscar notícias por categoria;\n "
        "5 - Listar top 5 notícias;\n 6 - Listar top 5 categorias;\n 7 - Sair."
    )
    i = input("Enter number: ")
    options = [
        "Digite quantas notícias serão buscadas:",
        "Digite o título:",
        "Digite a data no formato aaaa-mm-dd:",
        "Digite a tag:",
        "Digite a categoria:",
        "",
        "",
        "",
    ]
    try:
        if 0 <= int(i) <= 7:
            print(options[int(i)])
        else:
            print("Opção inválida", file=sys.stderr)
    except ValueError:
        print("Opção inválida", file=sys.stderr)


# utilizar stderr
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
