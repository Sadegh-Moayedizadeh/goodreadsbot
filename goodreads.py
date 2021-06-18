from bs4 import BeautifulSoup
import time
import random
import requests
import datetime


def random_quote():
    """generates random quotes from goodreads.com"""

    page_num = random.randint(1, 100)
    url = f'https://www.goodreads.com/quotes?page={page_num}&ref=nav_comm_quotes'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    quotes = soup.find_all("div", {"class": "quoteText"})
    return random.choice(quotes).get_text()


def get_news():
    """returns the 5 most popular news from goodreads.com"""

    news = []
    for page_num in range(1, 4):
        url = f'https://www.goodreads.com/news?page={page_num}&ref=nav_brws_news'
        r = requests.get(url)
        soup = BeautifulSoup(r.text, 'html.parser')
        news.extend(soup.find_all("div", {"class": "editorialCard"}))
        time.sleep(0.1)
    lst = []
    for item in news:
        title = item.find_all("a", {"class": "gr-hyperlink gr-hyperlink--bold"})[0].get_text().strip('\n ')
        link =  item.find_all("a", {"class": "gr-hyperlink gr-hyperlink--bold"})[0]['href']
        likes = int(item.find_all("div", {"class": "likesAndComments"})[0].get_text().split('\n')[1].split(' ')[0])
        date = item.find_all("a", {"class": "gr-hyperlink gr-hyperlink--naked"})[0].get_text().strip('\n ')
        lst.append({'title': title, 'likes': likes, 'link': link, 'date': date})
    lst = sorted(lst, key = lambda x: x['likes'], reverse = True)
    res = ''
    for i in range(5):
        res += f"title: {lst[i]['title']} \n date: {lst[i]['date']} \t likes: {lst[i]['likes']} \n link: {lst[i]['link']} \n \n"
    return res.strip('\n ')


def new_releases():
    """returns 5 most popular books released in the current month"""

    month = datetime.datetime.now().month
    year = datetime.datetime.now().year
    url = f'https://www.goodreads.com/new_releases/{year}/{month}?tab=by_genre'
    r = requests.get(url)
    soup = BeautifulSoup(r.text(), 'html.parser')

    


if __name__ == '__main__':
    new_releases()
