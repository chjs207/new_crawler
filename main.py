from bs4 import BeautifulSoup
import requests

news_url_before_keyword = "http://search.naver.com/search.naver?ie=utf8&where=news&query="
news_url_before_number = "&sm=tab_pge&sort=1&photo=0&field=0&reporter_article=&pd=0&ds=&de"\
                         "=&docid=&nso=so:dd,p:all,a:all&mynews=0&start="
news_url_end = "&refresh_start=0"

def get_search_page(URL):
    html = requests.get(URL, allow_redirects=False)
    html_text = html.text
    soup = BeautifulSoup(html_text, "html.parser")
    print(soup.text)

def main():
    print("Naver News Crawler")
    print("input your keyword to search news")
    print("input keyword : ")
    keyword = input()
    number = "1"

    full_url = news_url_before_keyword + keyword + news_url_before_number + number + news_url_end

    print(full_url+'\n')

    get_search_page(full_url)

main()
