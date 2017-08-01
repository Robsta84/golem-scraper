import sys; reload(sys)
sys.setdefaultencoding('utf-8')

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

    for element in range(0, len(list_of_header_elements)):
        a_tag = list_of_header_elements[element].attrs['href'] 
        headline = list_of_header_elements[element].find('h2').text        
        p_tag = list_elements[element].find('p').text  
        p_tag = p_tag[:p_tag.rfind('.') + 1] 
        p_tag = p_tag.strip()          
        new_article = Article(p_tag, a_tag, headline)              
        article_elements.append(new_article)             

    return article_elements
    
if __name__ == '__main__':

    if page.status_code == 200:
        tree = page.content
        soup = BeautifulSoup(tree, 'lxml')
        section = soup.find('section')        
        articles_list = soup.find_all('ol', "list-articles")       
        list_elements = get_list_elements(articles_list)        
        header_elements = get_header_elements(list_elements)
        articles = get_all_href_tags(header_elements, list_elements)       
        print len(articles)
        for article in articles:
            print "headline:     %s \n" % article.headline
            print "short text:   %s \n" % article.short_text
            print "link:         %s \n" % article.link 
            print "\n"        
    else:
        print ("Nothing to see here")
    


