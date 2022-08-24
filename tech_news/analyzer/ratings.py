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
    search_result = find_news()
    category_list = list(set(news["category"] for news in search_result))
    value = 0

    category_dict = dict.fromkeys(category_list, value)

    for news in search_result:
        category_dict[news["category"]] += 1

    category_dict_sorted_by_name = dict(
        sorted(category_dict.items(), key=lambda x: x[0])
    )

    category_dict_sorted_by_quantity = dict(
        sorted(
            category_dict_sorted_by_name.items(),
            reverse=True,
            key=lambda x: x[1],
        )
    )

    return list(category_dict_sorted_by_quantity)


# organizar dicionario por valor
# https://stackoverflow.com/questions/613183/how-do-i-sort-a-dictionary-by-value
