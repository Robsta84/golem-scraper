from bs4 import BeautifulSoup
import requests
from article import Article

page = requests.get('https://www.golem.de/')

def get_list_elements(list_of_articles):
    list_elements = []

    for element in list_of_articles:
        list_element = element.find_all('li')
        list_elements.extend(list_element)
    
    return list_elements

def get_header_elements(list_of_header):
    header_elements = []

    for header in list_of_header:
        link = header.find('header')        
        header_elements.extend(link)

    return header_elements

def get_all_href_tags(list_of_header_elements, list_elements):
    article_elements = []

    for header_element in list_of_header_elements:
        a_tag = header_element.attrs['href']    
        for list_element in list_elements:
            p_tag = list_element.find('p').text                
            new_article = Article(p_tag, a_tag)      
            article_elements.append(new_article)        

    return article_elements
    

if page.status_code == 200:
    tree = page.content
    soup = BeautifulSoup(tree, 'lxml')
    section = soup.find('section')        
    articles_list = soup.find_all('ol', "list-articles")       
    list_elements = get_list_elements(articles_list)        
    header_elements = get_header_elements(list_elements)
    articles = get_all_href_tags(header_elements, list_elements)      
    print "article: ", (articles[0].link, articles[0].short_text)
else:
    print ("Nothing to see here")
    


