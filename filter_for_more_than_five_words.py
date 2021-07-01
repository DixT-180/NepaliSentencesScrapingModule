
def filter_for_more_than_five_words():
    file = open("duplicates_removed.txt", "r", encoding="utf-8")
    doclist = [line for line in file]
    c = []
    for item in doclist:
        word_list = item.split(' ')
        no_of_words = len(word_list)
        if no_of_words in range(5, 14):
            c.append(item)
    with open('final.txt', 'w', encoding="utf-8") as f:
        for item in c:
            f.write("%s" % item)
