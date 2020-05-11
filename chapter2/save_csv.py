import csv

def main():
    '''
    リストをCSV形式で保存する。
    '''
    with open('top_cities.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        #ヘッダの出力
        writer.writerow(['rank','city', 'population'])
        #データの出力
        writer.writerows([
            [1, '上海', 24150000],
            [2, 'カラチ', 2350000],
            [3, '北京', 21516000],
            [4, '天津', 14722100],
            [5, 'イスタンブール', 14160467]
        ])

if __name__ == "__main__":
    main()
