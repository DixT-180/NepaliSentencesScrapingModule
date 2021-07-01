from bs4 import BeautifulSoup
import requests
import bs4
from requests.models import Response
import re


def scrape_paragraph(a):
    for items in a:
        r = requests.get(items)
        bs = bs4.BeautifulSoup(r.text, "html.parser")
        paragraphs = bs.findAll("p")
        other_paragraph = [p for p in paragraphs]
        filew = "para.txt"
    for div in other_paragraph:
        with open(filew, "a", encoding="utf-8") as f:
            print(div.text)
            f.write(div.text)
