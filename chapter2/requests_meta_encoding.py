import sys
import re
import requests

def main():
    '''
    metaタグから取得したエンコーディングでデコードし出力する
    '''
    
    #コマンドライン引数からURLを取得する
    #url = sys.argv[1]
    url = "https://gihyo.jp/dp"
    r = requests.get(url)

    #metaタグはHTMLの最初の方に書かれていると期待できるため、
    #レスポンスボディの先頭1024バイトをASCII文字列としてデコードする
    scanned_text = r.content[:1024].decode('ascii', errors='replace')

    match = re.search(r'charset=["\']?([\w-]+)', scanned_text)

    if match:
        r.encoding = match.group(0)
        #r.encoding = match.group(1)
    else:
        r.encoding = 'utf-8'

    print(f'encoding:{r.encoding}', file=sys.stderr)
    print(r.text)

if __name__ == "__main__":
    main()