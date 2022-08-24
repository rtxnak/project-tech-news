from tech_news.database import search_news


# Requisito 6
def search_by_title(title):
    search_result = search_news({"title": {"$regex": title, "$options": "-i"}})
    news_list = []

    for news in search_result:
        news_list.append((news["title"], news["url"]))

    return news_list


# consultar palavras incluidas
# https://stackoverflow.com/questions/10610131/checking-if-a-field-contains-a-string
# ingorar case sensitive no regex
# https://stackoverflow.com/questions/4976278/python-mongodb-regex-ignore-case

# Requisito 7
def search_by_date(date):
    """Seu código deve vir aqui"""


# Requisito 8
def search_by_tag(tag):
    """Seu código deve vir aqui"""


# Requisito 9
def search_by_category(category):
    """Seu código deve vir aqui"""
