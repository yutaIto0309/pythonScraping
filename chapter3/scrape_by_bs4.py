from urllib.parse import urljoin
from bs4 import BeautifulSoup

#HTMLファイルを読み込んでBeautifulSoupオブジェクトを得る。
with open('dp.html') as f:
    soup = BeautifulSoup(f, 'html.parser')

    #select()メソッドでa要素のリストを取得して、個々のa要素に対して処理を行う
    for a in soup.select('#listBook > li > a[itemprop="url"]'):
        #a要素のhref属性から書籍のURLを取得する
        url = urljoin('https://gihyo.jp/dp', a.get('href'))

        #書籍の名前はp要素のitemprop="name"から取得する
        p = a.select('p[itemprop="name"]')[0]
        title = p.text

        print(url, title)