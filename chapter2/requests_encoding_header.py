import sys
import requests


def main(): 
    '''
    コマンドライン引数からURLを取得し、
    該当URLのHTMLをテキスト形式でファイルに出力する。
    '''
    url = sys.argv[1]
    r = requests.get(url)
    print(f'encoding:{r.encoding}', file=sys.stderr)
    print(r.text)

if __name__ == "__main__":
    main()

