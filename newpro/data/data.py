import requests
from bs4 import BeautifulSoup
import html5lib

# Lấy nội dung chương
def get_content_from_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html5lib')
    title = soup.find('h2').text.strip()
    content = soup.find('div', class_='chapter-c').text  # Update the selector
    return title, content

# Lấy danh sách chương
def get_chapter_from_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links_list = soup.find('div', class_='col-xs-12 col-sm-6 col-md-6').find('ul', class_='list-chapter').find_all('a')
    links = [item['href'] for item in links_list]
    return links

# Lấy danh sách truyện
def get_novels_from_url(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links_list = soup.find('div', class_='list list-truyen col-xs-12').find_all('h3')
    novels = [[item.find('a').text, item.find('a')['href']] for item in links_list]
    return novels


def save_novel_content(novel_name,url):
    link_chapter = get_chapter_from_url(url)
    data = ""
    num=0
    for link in link_chapter:
        num+=1
        print(num,'/',len(link_chapter))
        title, content = get_content_from_url(link)
        data += title + '\n\n' + content + '\n\n'

        with open('data/'+novel_name + '.txt', 'w', encoding='utf-8') as file:
            file.write(data)


def get_novel_from_hot(url):
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    links_list=soup.find('div',class_='list list-truyen col-xs-12').find_all('h3')
    novels=[]
    num=0
    for link_tag in links_list:
        num +=1
        print(num,'/',len(links_list))
        novel_name, link=link_tag.find('a').text,link_tag.find('a')['href']
        novels.append([novel_name,link])
    return novels



url='https://truyenfull.vn/tien-nghich/'
# for i in range(0,1229):
#     url = 'https://truyenfull.vn/danh-sach/truyen-hot/trang-' +str(i)+'.html'
#     novels=get_novel_from_hot(url)
#     for novel in novels:
#         save_novel_content(novel[0],novel[1])

print(get_chapter_from_url(url))