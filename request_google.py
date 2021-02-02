#####  METHODE 01 pour Manipuler l'API

import urllib.request
import urllib.parse
import simplejson
import re

p= re.compile('.*youtube\.com.*', re.IGNORECASE)
e = re.compile('<b>|</b>') # 


q = urllib.parse.urlencode({'q': 'video2brain ubuntu'})
url = 'http://ajax.googleapis.com/ajax/services/search/web?v=1.0&%s' % (q) 
print (url) #http://ajax.googleapis.com/ajax/services/search/web?v=1.0&q=video2brain+ubuntu

search = urllib.request.urlopen(url)
print(search) #<http.client.HTTPResponse object at 0x03117B50>  ( un objet de réponse)
print(search.read()) #Un fichier JSON
print(simplejson.loads(search.read()))# Fichier JSON + on peut extraire ses élément pas mieux que la version précédante
JSON =simplejson.loads(search.read())
print(JSON['responseData']['results'])# Récupérer l'élément results inclu dans l'élément responseData: une liste 

# pour chaque élément de la liste précédente on affiche que les valeurs dont les clés = 'url'
for r in JSON['responseData']['results']:
	print(r['url'])


# pour chaque élément de la liste précédente on affiche que les valeurs dont les clés = 'url' et dont il contient l'expression 'youtube.com'
for r in JSON['responseData']['results']:
	if p.match(r['url']):
	print(r['url']) # http://youtube.com/wach......

 

# pour chaque élément de la liste précédente on affiche que les valeurs dont les clés = 'url' et dont il contient l'expression 'youtube.com' + le titre
for r in JSON['responseData']['results']:
	if p.match(r['url']):
	print(r['title'], r['url']) # <b>video2brain</b> - <b>Ubuntu </b> Linux : Les fondamentaux - YouTube http://www.youtube.com/watch....

# Pour enlever les symboles : substituer les balise <b> par un '', dans le titre


for r in JSON['responseData']['results']:
	if p.match(r['url']):
	print(e.sub('', r['title']), r['url'])

#video2brain - Ubuntu  Linux : Les fondamentaux - YouTube http://www.youtube.com/watch....

print('------------------------------------------------------------------------------')



#####  METHODE 01 pour Manipuler l'API:

### Documentation en ligne: Les objets Http ont plusieurs méthodes, la plus importante est : request :qui prend comme premier paramètre le type de la sous méthode (GET/POST/PUT..)  qui donne une tuple (response, content) 


import httplib2

class HTTPConnection:

def lire(self, URL):
	h = httplib2.Http(".cache")
	reponse, contenue = h.request(URL, 'GET')
	print(reponse) # I affiche l'entete du fichier JSON 
	print(contenue) # I affiche le contenue du fichier JSON 






Print('---------------------------------------------------------------------------')

### METHODE 03 ##################

from django.http import HttpResponse

def page(request):
	render HttpResponse('Bonjour')



Print('---------------------------------------------------------------------------')

### METHODE 04 ##################

from django0shortcuts import render


def page(request):
	render render(request, 'index.html')










































#Comparer avec le fonctionnement et la syntaxe des vues: 
# def test(request):
	#return render (request, 'Bonjour')

# def test(request):
	#return HttpLib('bonjour')
