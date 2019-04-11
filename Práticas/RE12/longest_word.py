# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 12:09:19 2018

@author: Ricardo Nunes
"""

import urllib.request

def longest_word(url):
  
    response = urllib.request.urlopen(url)
    html = response.read().decode()
    pagina=set(html.split())
    
    response = urllib.request.urlopen("https://raw.githubusercontent.com/fpro-admin/recitas/master/words")
    words = response.read().decode()
    dicionario=set(words.split())
    
    intercesao=dicionario.intersection(pagina)
    intercesao=sorted(intercesao)
    maximo=sorted(intercesao,key=lambda x:len(x),reverse=True)
    

    return maximo[0]

