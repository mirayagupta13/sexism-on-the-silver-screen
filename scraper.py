"""
Authors: Jenna, Miraya, Jaci
Title: Sexism on the Silver Screen
"""

import requests
from bs4 import BeautifulSoup
import wikipedia
 
all_pages_text = []
for actor in list_of_actors:
    page = wikipedia.page(actor)
    all_pages_text.append(page.text)
