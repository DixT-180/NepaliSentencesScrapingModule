
def remove_duplicates_sentences():
    lines_seen = set()  # holds lines already seen
    outfile = open("duplicates_removed.txt", "w", encoding="utf-8")
    infile = open("sent.txt", "r", encoding="utf-8")
    for line in infile:
        if line not in lines_seen:  # not a duplicate
            outfile.write(line)
            lines_seen.add(line)
    outfile.close()
