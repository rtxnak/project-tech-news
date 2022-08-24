from tech_news.database import search_news
from datetime import datetime


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
    news_list = []
    try:
        date_time_obj = datetime.strptime(date, "%Y-%m-%d")
        date_time_str = datetime.strftime(date_time_obj, "%d/%m/%Y")
        search_result = search_news({"timestamp": date_time_str})
    except ValueError:
        raise ValueError("Data inválida")
    else:
        for news in search_result:
            news_list.append((news["title"], news["url"]))
        return news_list


# Requisito 8
def search_by_tag(tag):
    search_result = search_news({"tags": {"$regex": tag, "$options": "-i"}})
    news_list = []

    for news in search_result:
        news_list.append((news["title"], news["url"]))

    return news_list


# Requisito 9
def search_by_category(category):
    search_result = search_news(
        {"category": {"$regex": category, "$options": "-i"}}
    )
    news_list = []

    for news in search_result:
        news_list.append((news["title"], news["url"]))

    return news_list
