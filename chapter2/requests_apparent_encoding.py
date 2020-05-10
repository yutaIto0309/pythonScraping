import sys
import requests

def main():
    '''
    レスポンスボディのバイト列から、
    推定されたエンコーディングでデコードし出力する
    '''
    url = sys.argv[1]
    r = requests.get(url)
    r.encoding = r.apparent_encoding
    print(f'encoding:{r.encoding}', file=sys.stderr)
    print(r.text)

if __name__ == "__main__":
    main()