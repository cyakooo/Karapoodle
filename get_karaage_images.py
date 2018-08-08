import time
import re
import requests
from requests.compat import urljoin
from bs4 import BeautifulSoup

homeURL = 'https://cookpad.com/'
searchURL = 'https://cookpad.com/search/%E9%B6%8F%E3%81%AE%E3%81%8B%E3%82%89%E6%8F%9A%E3%81%92%20%20%E6%9D%90%E6%96%99%EF%BC%9A%E9%B6%8F%E8%82%89?order=date&page='

karaageSearch_urls = []

# から揚げの検索ページのURLを取得
for i in range(1, 500):
    karaageSearch_urls.append(searchURL + str(i) + '.html')

karaage_pages = []
a_tag_href_re = re.compile(r'/recipe/[0-9]*')

# から揚げのレシピページのURLを取得
for i in karaageSearch_urls:
    soup = BeautifulSoup(requests.get(i).content, 'lxml')
    for j in soup.find_all('a', class_="recipe-title font13 "):
        string = str(j)
        matchOb = re.search(a_tag_href_re, string)
        url = urljoin(homeURL, matchOb.group(0))
        karaage_pages.append(url)
        time.sleep(1)

images = []
images_src_re = re.compile(r'.*\.jpg')

# 個々のから揚げのレシピページから画像を取得
for url in karaage_pages:
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    for link in soup.find_all("img", class_="analytics_tracking photo large_photo_clickable"):
        src = link.get("src")
        correct_src = re.search(images_src_re, src).group(0)
        images.append(correct_src)

i = 1

# images[]内の画像URLから画像を取得しフォルダに保存
for target in images:
    re = requests.get(target)
    with open('karaage/' + target.split('/')[-1], 'wb') as f:
        f.write(re.content)
    print('Image file ' + str(i) + '/' + str(len(images)) + ' was written!!')
    time.sleep(1)
    i += 1

print('All completed !!')