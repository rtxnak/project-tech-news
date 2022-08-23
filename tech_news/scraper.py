from requests.exceptions import HTTPError
from parsel import Selector
import requests
import time

# html = fetch("https://blog.betrybe.com")
# scrape_novidades(html)


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
    """Seu código deve vir aqui"""


# Requisito 4
def scrape_noticia(html_content):
    """Seu código deve vir aqui"""


# Requisito 5
def get_tech_news(amount):
    """Seu código deve vir aqui"""
