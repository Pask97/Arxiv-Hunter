import random
import feedparser

class Arxiv:
    
    def __init__(self,articles_number:int,start:int)->None:
        
        self._start = start
        
        self._quantity = articles_number       
    
        self._start_url = 'http://export.arxiv.org/api/query?search_query='
         
        
    def _id_parser(self,url):
        
        id_list = []
        d = feedparser.parse(url)
        for n in range(len(d['entries'])):
           id_list.append(d['entries'][n]['id'])
                       
        return id_list        
          
         
    def complete_random_search(self, author:str , title:str, abstract:str):       
        number = random.randint(self._start,self._start + 20)       
        url = self._start_url + f'au:{author}+AND+ti:{title}+AND+abs:{abstract}&start={str(number)}&max_results={str(self._quantity)}'
        for n in range(number,0,-1):
            number = number - 1
            url = self._start_url + f'au:{author}+AND+ti:{title}+AND+abs:{abstract}&start={str(number)}&max_results={str(self._quantity)}'
            if len(self._id_parser(url)) != 0:
                break
        if number < 1:
            print('Start number is too high.')
        return self._id_parser(url)
   
    def complete_relevance_search(self, author:str , title:str, abstract:str):
        url = self._start_url + f'au:{author}+AND+ti:{title}+AND+abs:{abstract}&start={str(self._start)}&max_results={str(self._quantity)}&sortBy=relevance&sortOrder=descending'
        return self._id_parser(url)
   
    def complete_date_search(self, author:str , title:str, abstract:str):
        url = self._start_url + f'au:{author}+AND+ti:{title}+AND+abs:{abstract}&start={str(self._start)}&max_results={str(self._quantity)}&sortBy=submittedDate&sortOrder=descending'
        return self._id_parser(url)   
    
    def author_title_random_search(self, author:str , title:str):       
        number = random.randint(self._start, self._start +20)          
        url = self._start_url + f'au:{author}+AND+ti:{title}&start={str(number)}&max_results={str(self._quantity)}'
        for n in range(number,0,-1):
            number = number - 1
            url = self._start_url + f'au:{author}+AND+ti:{title}&start={str(number)}&max_results={str(self._quantity)}'
            if len(self._id_parser(url)) != 0:
                break
        return self._id_parser(url)
   
    def author_title_relevance_search(self, author:str , title:str):
        url = self._start_url + f'au:{author}+AND+ti:{title}&start={str(self._start)}&max_results={str(self._quantity)}&sortBy=relevance&sortOrder=descending'
        return self._id_parser(url)
   
    def author_title_date_search(self, author:str , title:str):
        url = self._start_url + f'au:{author}+AND+ti:{title}&start={str(self._start)}&max_results={str(self._quantity)}&sortBy=submittedDate&sortOrder=descending'
        return self._id_parser(url)
    
    def author_abstract_random_search(self, author:str , abstract:str):       
        number = random.randint(self._start, self._start +20)          
        url = self._start_url + f'au:{author}+AND+abs:{abstract}&start={str(number)}&max_results={str(self._quantity)}'
        for n in range(number,0,-1):
            number = number - 1
            url = self._start_url + f'au:{author}+AND+abs:{abstract}&start={str(number)}&max_results={str(self._quantity)}'
            if len(self._id_parser(url)) != 0:
                break
        return self._id_parser(url)
   
    def author_abstract_relevance_search(self, author:str , abstract:str):
        url = self._start_url + f'au:{author}+AND+abs:{abstract}&start={str(self._start)}&max_results={str(self._quantity)}&sortBy=relevance&sortOrder=descending'
        return self._id_parser(url)
   
    def author_abstract_date_search(self, author:str , abstract:str):
        url = self._start_url + f'au:{author}+AND+abs:{abstract}&start={str(self._start)}&max_results={str(self._quantity)}&sortBy=submittedDate&sortOrder=descending'
        return self._id_parser(url)
    
    def title_abstract_random_search(self, title:str , abstract:str):       
        number = random.randint(self._start, self._start +20)          
        url = self._start_url + f'ti:{title}+AND+abs:{abstract}&start={str(number)}&max_results={str(self._quantity)}'
        for n in range(number,0,-1):
            number = number - 1
            url = self._start_url + f'ti:{title}+AND+abs:{abstract}&start={str(number)}&max_results={str(self._quantity)}'
            if len(self._id_parser(url)) != 0:
                break
        return self._id_parser(url)
   
    def title_abstract_relevance_search(self, title:str , abstract:str):
        url = self._start_url + f'ti:{title}+AND+abs:{abstract}&start={str(self._start)}&max_results={str(self._quantity)}&sortBy=relevance&sortOrder=descending'
        return self._id_parser(url)
   
    def title_abstract_date_search(self, title:str , abstract:str):
        url = self._start_url + f'ti:{title}+AND+abs:{abstract}&start={str(self._start)}&max_results={str(self._quantity)}&sortBy=submittedDate&sortOrder=descending'
        return self._id_parser(url)
    
    def author_random_search(self, author:str):       
        number = random.randint(self._start, self._start +20)          
        url = self._start_url + f'au:{author}&start={str(number)}&max_results={str(self._quantity)}'
        for n in range(number,0,-1):
            number = number - 1
            url = self._start_url + f'au:{author}&start={str(number)}&max_results={str(self._quantity)}'
            if len(self._id_parser(url)) != 0:
                break
        return self._id_parser(url)
   
    def author_relevance_search(self, author:str):
        url = self._start_url + f'au:{author}&start={str(self._start)}&max_results={str(self._quantity)}&sortBy=relevance&sortOrder=descending'
        return self._id_parser(url)
   
    def author_date_search(self, author:str):
        url = self._start_url + f'au:{author}&start={str(self._start)}&max_results={str(self._quantity)}&sortBy=submittedDate&sortOrder=descending'
        return self._id_parser(url)  
    
    def title_random_search(self, title:str):       
        number = random.randint(self._start, self._start +20)          
        url = self._start_url + f'ti:{title}&start={str(number)}&max_results={str(self._quantity)}'
        for n in range(number,0,-1):
            number = number - 1
            url = self._start_url + f'ti:{title}&start={str(number)}&max_results={str(self._quantity)}'
            if len(self._id_parser(url)) != 0:
                break
        return self._id_parser(url)
   
    def title_relevance_search(self,title:str):
        url = self._start_url + f'ti:{title}&start={str(self._start)}&max_results={str(self._quantity)}&sortBy=relevance&sortOrder=descending'
        return self._id_parser(url)
   
    def title_date_search(self, title:str):
        url = self._start_url + f'ti:{title}&start={str(self._start)}&max_results={str(self._quantity)}&sortBy=submittedDate&sortOrder=descending'
        return self._id_parser(url) 
    
    def abstract_random_search(self, abstract:str):       
        number = random.randint(self._start, self._start +20)          
        url = self._start_url + f'abs:{abstract}&start={str(number)}&max_results={str(self._quantity)}'
        for n in range(number,0,-1):
            number = number - 1
            url = self._start_url + f'abs:{abstract}&start={str(number)}&max_results={str(self._quantity)}'
            if len(self._id_parser(url)) != 0:
                break
        return self._id_parser(url)
   
    def abstract_relevance_search(self,abstract:str):
        url = self._start_url + f'abs:{abstract}&start={str(self._start)}&max_results={str(self._quantity)}&sortBy=relevance&sortOrder=descending'
        return self._id_parser(url)
   
    def abstract_date_search(self, abstract:str):
        url = self._start_url + f'abs:{abstract}&start={str(self._start)}&max_results={str(self._quantity)}&sortBy=submittedDate&sortOrder=descending'
        return self._id_parser(url) 
    