def url_to_list():
    url_lst = []
    file = open("url.txt", "r", encoding="utf-8")  # links txt
    for url in file:
        url_lst.append(url)
    converted_list = []
    for element in url_lst:
        converted_list.append(element.strip())
    print(converted_list)
    return converted_list
