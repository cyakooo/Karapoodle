import time
import csv
import re
import requests
from requests.compat import urljoin
from bs4 import BeautifulSoup

URL = 'https://toy-poodle.min-breeder.com/'

dogSearch_urls = []

for i in range(1, 33):
    dogSearch_urls.append('https://toy-poodle.min-breeder.com/dogSearch_' + str(i) + '.html')

dog_page_regular_expression = re.compile(r'dog[0-9]{4}-[0-9]{5}\.html')
dog_pages = []

for i in dogSearch_urls:
    response = requests.get(i).text
    soup = BeautifulSoup(response, "lxml")
    for j in soup.find_all('a', href=dog_page_regular_expression):
        string = str(j)
        dog_pages.append(string)
    time.sleep(1)   #サーバに負担をかけないように1秒間隔で実行

true_dog_pages = []

#dog_pages[]からURLを抽出、整形
for i in dog_pages:
    unshaped_url = re.search(dog_page_regular_expression, i).group(0)    
    shaped_url = 'https://toy-poodle.min-breeder.com/' + unshaped_url
    true_dog_pages.append(shaped_url)

print('You get URLs !!')
images = []

#全てのページ内の画像URLをimages[]に格納
for url in true_dog_pages:
    soup = BeautifulSoup(requests.get(url).content, 'lxml')
    for link in soup.find_all("img", class_="detail_thumb_img"):
        src = link.get("src")
        if src.endswith(".jpg"):
            images.append(urljoin(URL, src))

print('You get ' + str(len(images)) + ' Image URLs !!')

i = 1
#images[]内の画像URLから画像を取得しフォルダに保存
for target in images:
    re = requests.get(target)
    with open('poodle/' + target.split('/')[-1], 'wb') as f:
        f.write(re.content)
    print('Image file' + str(i) + '/' + str(len(images)) + ' is written!!')
    time.sleep(1)
    i += 1


