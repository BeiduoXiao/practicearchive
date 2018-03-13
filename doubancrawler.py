# -*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import urllib2
import requests
import sys
reload(sys)
sys.setdefaultencoding('utf-8')





def get_page_list():
    pass
    pageurl_list=[]
    i=0
    while(i<=225):
        istr=str(i)
        pageurl='https://movie.douban.com/top250?start='+istr
        pageurl_list.append(pageurl)
        i=i+25
    return pageurl_list


def get_single_page_url(pageurl):
    #pageurl='https://movie.douban.com/top250?start=0&filter='
    response = requests.get(pageurl)
    soup = BeautifulSoup(response.content, "html.parser")
    urllist=[]
    items = soup.find_all(class_="item")
    for item in items:
        url=item.a.get("href")
        urllist.append(url)

    return urllist


def get_detail(info_url):
    response = requests.get(info_url)
    soup = BeautifulSoup(response.content, "html.parser")
    #movie_name=soup.find('span',property="v:itemreviewed").text
    judge=soup.find('title').text
    notfound='页面不存在'
    if judge==notfound:
        detail='这里有个电影被河蟹了'
    else:
        
        movie_name=soup.find("h1").span.text
        year=soup.find(class_="year").text
        info=soup.find('div',id='info').text
        rate=soup.find('strong',class_="ll rating_num").text
        summary=soup.find('span',property="v:summary").text
        detail=movie_name+"\n"+year+"\n"+info+"\n"+"评分："+rate+"\n"+summary
    
    
    
    #print detail
    return detail


if __name__ == '__main__':
    fp=open('Top250movie.txt','a')
    pages=get_page_list()
    #print pages
    i=0
    for page in pages:
        
        urls=get_single_page_url(page)
        for url in urls:
            detail=get_detail(url)
            print detail
            fp.write(detail)
            fp.write('###########################################################################################')
            fp.write("\n")
        

    




'''for url in urls:
            detail=get_detail(url)
            fp.write(detail)
            fp.write('########################################################')
        fp.close()
        '''



'''fp=open('detail.txt','w')
fp.write(movie_name)
fp.write(year)
fp.write(info)'''

'''fp.write(year)
fp.write(test)

print(movie_name)
print type(movie_name)
#print year
#print test
'''



