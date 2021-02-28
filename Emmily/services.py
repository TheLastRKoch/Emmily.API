import requests
import re

class DictionaryEn():
    
    def __init__(self,search_word):
        self.user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.14; rv:65.0) Gecko/20100101 Firefox/65.0"
        self.search_word = str.lower(search_word)
    
    def __performGoogleQuery(self):
        """Return the result of the GET request of Google.com"""  
        headers = {"user-agent" : self.user_agent}
        parameters = {"hl":"en"}
        query = "Meaning+"+self.search_word.replace(' ', '+')
        url = url = f"https://google.com/search?q={query}"
        return requests.get(url,params=parameters, headers=headers)

    def __performVocabularyQuery(self):
        """Return the result of the GET request from Vocabulary.com"""
        headers = {'Content-Type': 'application/json'}
        query = self.search_word.replace(' ', '+')
        url = url = f"https://www.vocabulary.com/dictionary/definition.ajax?search={query}"
        return requests.get(url,headers=headers)

    def __performCorpusVocabularyQuery(self):
        """Return the result of the GET request from Corpus.Vocabulary.com"""
        headers = {'Content-Type': 'application/json'}
        query = self.search_word.replace(' ', '+')
        url = f"https://corpus.vocabulary.com/api/1.0/examples.json?query={query}&maxResults=1"
        return requests.get(url,headers=headers)

    def __clearString(self,text):
        """Return the parameter without \\n \\t \\r or i tags"""
        text = text.replace('<i>',"")
        text = text.replace('</i>',"")
        text_list = text.split()
        return" ".join(text_list)

    def getPhonetic(self):
        """Return the @word phonetic"""
        req = self.__performGoogleQuery()
        if req.status_code != 200:
            return "Error: Invalid request" 
        pattern = '<div class="S23sjd g30o5d"><span>\/<span>([\w\W]+?)<\/span>\/'
        match = re.search(pattern,req.text)
        if match is None:
            return "Error: phonetic not found" 
        return self.__clearString(match.group(1))

    def getDefinition(self):
        """Return the @word formal definition"""
        req = self.__performGoogleQuery()
        if req.status_code != 200:
            return "Error: Invalid request" 
        pattern = 'style="display:inline" data-dobid="dfn"><span>([\w\W]+?)<\/span>'
        match = re.search(pattern,req.text)
        if match is None:
            return "Error: Definition not found" 
        return self.__clearString(match.group(1)) 

    def getUrbanDefinition(self):
        """Return the @word urban definition"""
        req = self.__performVocabularyQuery()
        if req.status_code != 200:
            return "Error: Invalid request"  
        pattern = '<p class="short">([\w\W]+?)<\/p>'
        match = re.search(pattern,req.text)
        if match is None:
            return "Error: Definition not found" 
        return self.__clearString(match.group(1)) 

    def getSentence(self):
        """Return the @word example sentence"""
        req = self.__performCorpusVocabularyQuery()
        if req.status_code != 200:
            return "Error: Invalid request"  
        data = req.json()
        if data["result"]["totalHits"] == 0:
            return "Error: Sentences not found" 
        sentence_list = data["result"]["sentences"]
        for node in sentence_list:
            return self.__clearString(node['sentence'])