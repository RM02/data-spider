import requests
import nltk
from bs4 import BeautifulSoup as bs

def getPage(url):
	try:
		res = requests.get(url)
		soup = bs(res.content, "html.parser")
		return soup
	except:
		pass

def getContent(page):
	
	content = {
		"paragraph": [],
		"title": []
	}

	try:
		content['paragraph'] = [i.get_text() for i in page.findAll("p")]
		content['title'] = page.title.get_text()
		return content
	except:
		return content

def sentences_analysis(data):

	n_sentences = []

	for paragraph in data:
		
		sentences = nltk.sent_tokenize(paragraph)

		if len(sentences) > 1:
			for sentence in sentences:
				n_sentences.append(sentence)
		else:
			n_sentences += sentences

	return n_sentences

def word_analysis(data):
    
    words_list = []
    list_common_words = []
    tokenizer = nltk.tokenize.RegexpTokenizer(r'\W+')
    
    for sentence in data:
    	words = nltk.word_tokenize(sentence)
    	for word in words:
    		if len(word) > 2:
    			words_list.append(word)
    list_common_words = nltk.FreqDist(words_list).most_common()

    return list_common_words

def main(url):

	page = getPage(url)
	results = {
		"title": [],
		"sentences": [],
		"total_sentences": [],
		"common_words": []
	}
	if page:
		data = getContent(page)
		results['title'] = data['title']
		results['sentences'] = sentences_analysis(data['paragraph'])
		results['total_sentences'] = len(results['sentences'])
		results['common_words'] = word_analysis(results['sentences'])

	return results