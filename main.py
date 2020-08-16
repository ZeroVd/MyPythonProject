import requests
from lxml import etree

url_song_list = 'https://music.163.com/playlist?id=2883748780'

headers = {
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.132 Safari/537.36',
    'cookie': '_iuqxldmzr_=32; _ntes_nnid=e73f7952979e9e709e42b6fee424dcf7,1595990417584; _ntes_nuid=e73f7952979e9e709e42b6fee424dcf7; WM_NI=LRGEITlJdhFkI%2B7dyBCHCvvYV4%2FBYHqIJX%2F8W%2F1MktYhoUOQIvEAZus0SMlv4ywO3kj4T5eM3P9VA6odcW%2FaWYOyUhvZ%2FNeydnPMJCvshDtyhM3d7rMgxOb16fGUYjWIV00%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6ee91bc7c96bfae8fb147f59a8fa6d55f969f8aaff844f8be9f87e6708bb6bbabe52af0fea7c3b92a908e89a6cc60b096ac89c5618bf5f985fc4a81988d97f55396ece1a3dc44b39786b9ae3495f1ffaeea809bb8a1b6ce5b8baa8ba2d97fb1f09daeef7ef8a7b9b0b261aaec9cd6e847f190f7b7c43eadbcadb8ae6b9587819ad864b686e1afe873a8b2a0aec949b6ada8a5f773ac93fd85b67a8fb9b8b0e13bf6ba89b6dc6295979ad1b337e2a3; WM_TID=HlwJ%2FDkJVf9FEFFBBUNqXpbEK1JYm7IL; playerid=66588813; MUSIC_U=5f5027774a2c1949c28f0b6b296d2e7e556abdad0a5cd2dfe054c8a44dfbc9924e2cdec09a6d1897c53018e224407f138c3c24de17bc8a1ee381395bf06ec255; __remember_me=true; __csrf=bc376f64e60dbdef14961e7d5463c7c5; ntes_kaola_ad=1; JSESSIONID-WYYY=jlYh4cFH%2F%2BBWiMbrv6UUAFW0EjZMjzH4Ema%5C%2BKz2OBvKG923ZnCBIURXosXgME2WEkCqz%2FjHBrWPbuZ4BhTnS%2BN%5Cj%5ChPXnJRu5edDgqPisDivTeWCpfI671zTbPliGpq7zhG%5CJbwp%2FMmQbksI8bkEb8Pt9WvRnwgDZA0ZTR%5CdlPKNYWW%3A1595995699476'
}

"""

http://music.163.com/song/media/outer/url?id=412902075.mp3
http://music.163.com/song/media/outer/url?id=25640496.mp3
"""

def get_html(url_list):
    html = requests.get(url_list, headers = headers).content.decode('utf-8')
    tree = etree.HTML(html)
    url_music = tree.xpath('//ul[@class="f-hide"]/li/a/@href')
    name = tree.xpath('//ul[@class="f-hide"]/li/a/text()')

    for index, item in enumerate(url_music):
        url = 'http://music.163.com/song/media/outer/url?id=%s.mp3' % item.split('=')[-1]
        file_name = name[index]
        print(file_name)
        print(url)

        #保存
        file_path = 'D:\Home\python\爬取网易云\music\%s.mp3' % file_name
        with open(file_path, 'wb') as mu:
            req = requests.get(url, headers = headers, timeout = 30)
            mu.write(req.content)


def get_content(html):
    pass

if __name__ == '__main__':
    html = get_html(url_song_list)
    get_content(html)

