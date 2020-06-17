from django.http import JsonResponse, HttpResponse
from django.shortcuts import render
from scraper import scraping

def getAll(request):
    url = request.GET.get('url')
    content = scraping.main(url)
    
    data = {
        'title': content['title'],
        'url': url,
        'results': {
        	'sentences': content['sentences'],
            'total_sentences': len(content['sentences']),
        	'common_words': content['common_words'][0:5]
        }
    }
    return JsonResponse(data)

# def getData(request):
#     content = scraping.main(url)
    
#     data = {
#         'title': content['title'],
#         'url': url,
#         'results': {
#             'sentences': content['sentences'][0:3],
#             'total_sentences': len(content['sentences']),
#             'common_words': content['common_words'][0:3]
#         }
#     }
#     return HttpResponse(data)