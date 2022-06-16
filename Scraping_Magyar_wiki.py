import re
import requests


def scrape_wiki_magyar():

    wiki_page_1 = "https://en.wiktionary.org/wiki/Category:Hungarian_suffixes"

    wiki_page_2 = "https://en.wiktionary.org/w/index.php?title=Category:Hungarian_\\"\
                  "suffixes&pagefrom=ENEM%0A-en%C3%A9m#mw-pages"
    wiki_page_3 = "https://en.wiktionary.org/w/index.php?title=Category:Hungarian_\\"\
                  "suffixes&pagefrom=LOG%0A-log#mw-pages"
    wiki_page_4 = "https://en.wiktionary.org/w/index.php?title=Category:Hungarian_\\" \
                  "suffixes&pagefrom=TAL%0A-t%C3%A1l#mw-pages"

    for wiki_page in range(1, 4):
        page = f'wiki_page_{wiki_page}'
        wiki = requests.get("")
        wiki_txt = wiki.text
        with open(f"wiki_text_{wiki_page}.txt", 'w') as f:
            f.write(wiki_txt)

    regex = r"<li><a href=\"/wiki/-(.*)\">(.*?)</a></li>"
    for wiki in range(1, 5):
        with open(f'regexed_{wiki}.txt', 'w') as r:
            matches = re.finditer(regex, f'wiki_txt_{wiki}', re.MULTILINE)
            for matchNum, match in enumerate(matches, start=1):
                for groupNum in range(0, len(match.groups())):
                    groupNum = groupNum + 1
                    r.write(match.group(2))


    # with open ('combined_from_wiki.txt', "w") as combined_from_wiki:
    #     combined_from_wiki.write(wiki_txt_1)
    #     combined_from_wiki.write(wiki_txt_2)


    
if __name__ == '__main__':
    scrape_wiki_magyar()