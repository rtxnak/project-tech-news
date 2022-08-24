from tech_news.database import find_news


# Requisito 10
def top_5_news():
    search_result = find_news()
    search_result.sort(key=lambda x: x["title"])
    search_result.sort(reverse=True, key=lambda x: x["comments_count"])
    top_5_news_list = []

    if len(search_result) < 5:
        max_length = len(search_result)
    else:
        max_length = 5

    for index in range(0, max_length):
        top_5_news_list.append(
            (search_result[index]["title"], search_result[index]["url"])
        )

    return top_5_news_list


# Requisito 11
def top_5_categories():
    """Seu código deve vir aqui"""
