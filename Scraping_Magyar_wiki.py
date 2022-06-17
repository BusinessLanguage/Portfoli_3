import re
import requests


def scrape_wiki_magyar():

    pages = {"wiki_page_1": "https://en.wiktionary.org/wiki/Category:Hungarian_suffixes",
             "wiki_page_2": "https://en.wiktionary.org/w/index.php?title=Category:Hungarian_suffixes&pagefrom=ENEM%0A-enem#mw-pages",
             "wiki_page_3": "https://en.wiktionary.org/w/index.php?title=Category:Hungarian_suffixes&pagefrom=LLIK%0A-llik#mw-pages",
             "wiki_page_4": "https://en.wiktionary.org/w/index.php?title=Category:Hungarian_suffixes&pagefrom=TAD%0A-tad#mw-pages"
             }

    for url in pages.values():
        content = requests.get(url).text
        with open("content.txt", "a", encoding="utf-8") as c:
            c.write(content)
        # print(content)
        regex = "<li><a href=\"/wiki/-(?:.*)\" title=\"(?:.*)\">(.*?)</a></li>"
        set1 = set()
        with open("Magyar_suffixes_scraped.txt", "a", encoding="utf-8") as f:
            matches = re.finditer(regex, content, re.MULTILINE)
            for matchNum, match in enumerate(matches, start=1):
                for groupNum in range(0, len(match.groups())):
                    set1.add(match.group(1))
            f.write(str(set1))


if __name__ == '__main__':
    scrape_wiki_magyar()
