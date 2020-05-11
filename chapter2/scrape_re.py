import re
from html import unescape
from urllib.parse import urljoin

def main():
    '''
    正規表現によるスクレイピング
    '''

    #ファイルの中身を変数htmlに設定
    with open('dp.html') as f:
        html = f.read()

        for partial_html in re.findall(r'<a itemprop="url".*?</ul>\s*</a></li>', html, re.DOTALL):
            #書籍のURLはitemprop="url"という属性をもつa要素のhref属性から取得する
            url = re.search(r'<a itemprop="url" href="(.*?)">', partial_html).group(1)
            url = urljoin('https://gihyo.jp/dp', url)

            #書籍のタイトルはitemprop="name"という属性をもつp要素から取得する
            title = re.search(r'<p itemprop="name".*?</p>', partial_html).group(0)
            title = title.replace('<br/>', ' ')
            title = re.sub(r'<>*?>', '', title)
            title = unescape(title)

            print(url, title)
            
if __name__ == "__main__":
    main()