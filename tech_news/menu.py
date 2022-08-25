import sys
from tech_news.scraper import get_tech_news
from tech_news.analyzer.search_engine import (
    search_by_title,
    search_by_date,
    search_by_tag,
    search_by_category,
)
from tech_news.analyzer.ratings import top_5_news, top_5_categories


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
    function_options = [
        get_tech_news,
        search_by_title,
        search_by_date,
        search_by_tag,
        search_by_category,
        top_5_news,
        top_5_categories,
    ]
    try:
        if 0 <= int(i) <= 7:
            return conditonal_reponse(i, options, function_options)
        else:
            print("Opção inválida", file=sys.stderr)
    except ValueError:
        print("Opção inválida", file=sys.stderr)


def conditonal_reponse(i, options, function_options):
    if int(i) == 0:
        response = input(options[int(i)])
        return function_options[int(i)](int(response))
    elif int(i) == 7:
        print("Encerrando script")
    else:
        if options[int(i)] != "":
            response = input(options[int(i)])
            return function_options[int(i)](str(response))
        else:
            return function_options[int(i)]()


# utilizar stderr
# https://stackoverflow.com/questions/5574702/how-to-print-to-stderr-in-python
