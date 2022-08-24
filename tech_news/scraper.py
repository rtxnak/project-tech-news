from requests.exceptions import HTTPError
from parsel import Selector
from tech_news.database import create_news
import requests
import time


# Requisito 1
def fetch(url):
    try:
        response = requests.get(
            url, timeout=3, headers={"user-agent": "Fake user-agent"}
        )
        response.raise_for_status()
        time.sleep(1)
    except requests.ReadTimeout:
        return None
    except HTTPError:
        return None
    else:
        return response.text


# Requisito 2
def scrape_novidades(html_content):
    selector = Selector(text=html_content)
    news_url = selector.css("a.cs-overlay-link::attr(href)").getall()
    return news_url


# Requisito 3
def scrape_next_page_link(html_content):
    selector = Selector(text=html_content)
    next_page_url = selector.css("a.next.page-numbers::attr(href)").get()
    return next_page_url


# Requisito 4
def scrape_noticia(html_content):
    selector = Selector(text=html_content)
    url = selector.css("link[rel='canonical']::attr(href)").get()
    title = selector.css("h1.entry-title::text").get()
    timestamp = selector.css("li.meta-date::text").get()
    writer = selector.css("span.author a::text").get()
    comments_count = selector.css("div[id='comments'] h5::text").get()

    summary = selector.css(
        "div.entry-content > p:first-of-type *::text"
    ).getall()  # lista com todos os elementos do primeiro p

    # convertendo lista em string
    # https://www.delftstack.com/pt/howto/python/how-to-convert-a-list-to-string/

    summary_content = "".join(summary).strip()
    tags = selector.css("a[rel='tag']::text").getall()
    category = selector.css("span.label::text").get()

    if comments_count is not None:
        comments_count_number = int(comments_count.split("comments")[0])
    else:
        comments_count_number = 0

    return {
        "url": url,
        "title": title.strip(),
        "timestamp": timestamp,
        "writer": writer,
        "comments_count": comments_count_number,
        "summary": summary_content,
        "tags": tags,
        "category": category,
    }


# Requisito 5
def get_tech_news(amount):
    URL_BASE = "https://blog.betrybe.com/"
    html = fetch(URL_BASE)
    url_news = scrape_novidades(html)
    next_page_link = scrape_next_page_link(html)
    # url_news_length = len(url_news)
    news = []

    while len(url_news) < amount:
        next_page_html = fetch(next_page_link)
        next_page_url_news = scrape_novidades(next_page_html)
        url_news += next_page_url_news
        next_page_link = scrape_next_page_link(next_page_html)

    for index in range(0, amount):
        news_html = fetch(url_news[index])
        news_scraped = scrape_noticia(news_html)
        news.append(news_scraped)

    create_news(news)
    return news
