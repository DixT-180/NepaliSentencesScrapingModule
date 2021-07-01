import re


def senten_linebyline():
    file = open("para.txt", "r", encoding="utf-8")
    doclist = [line for line in file]
    docstr = '' . join(doclist)
    sentences = re.split(r'[।]', docstr)
    with open('sent.txt', 'w', encoding="utf-8") as f:
        for item in sentences:
            f.write("%s।\n" % item)
