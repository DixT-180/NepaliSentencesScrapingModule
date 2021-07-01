from bs4 import BeautifulSoup
import requests
import bs4
from requests.models import Response
import re

from url_to_list import url_to_list
from scrape_paragraph import scrape_paragraph
from senten_linebyline import senten_linebyline
from filter_for_more_than_five_words import filter_for_more_than_five_words
from remove_duplicate_sentences import remove_duplicates_sentences

converted_list = url_to_list()  # 1
print(converted_list)
scrape_paragraph(converted_list)  # 2
senten_linebyline()  # 3
remove_duplicates_sentences()  # 4
filter_for_more_than_five_words()  # 5
