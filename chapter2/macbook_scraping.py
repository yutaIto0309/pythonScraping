"""
PyQueryを使って、
Appleのページから認定整備済み製品の品名と価格を抜き出す
"""
from pyquery import PyQuery as pq
import requests

def main():
    """
    メイン処理
    """
    while True:
        try:
            #商品リスト
            macbook_list = list()   
            #Appleのmac整備済製品のurl
            apple_url = 'https://www.apple.com/jp/shop/refurbished/mac'   
            data = pq(url=apple_url)

            for a in data('h3 > a'):
                if '13.3インチ' in a.text and 'Core i7' in a.text:
                    #商品リストに追加する
                    macbook_list.append(f"{a.text}\n")

            if len(macbook_list) != 0:
                #商品が追加されていた場合、LINEに通知し処理を終える
                post_url = "https://notify-api.line.me/api/notify"  #LineNotifyのURL
                token = "8LveveehYuxHSJfWmPpbfFuL5xTxdXqBp6Xvqx3FGvc"   #LINEに通知するためのトークン
                headers = {"Authorization": f"Bearer {token}"}
                payload = {"message": "下記の商品が追加されました。\n" + ''.join(macbook_list)}
                requests.post(post_url, headers=headers, params=payload)
                break
        except:
            #予期せぬ例外
            print("例外が発生しました", file=SystemError)
            break
        
if __name__ == "__main__":
    main()