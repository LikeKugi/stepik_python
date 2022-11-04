import requests
import re
from html.parser import HTMLParser


def get_query(): return input()


def create_request(page: str) -> list:
    links = []
    print(f'parsing {page}')
    req = requests.get(page)
    pattern = r'''<a\s[.\w]*?href="(.*)"'''
    l = re.findall(pattern, req.text)
    # print(l)
    links.extend(l)
    for el in l:
        for i in range(len(el)):
            if '//' in el[i]:
                print(el[i])
                links.append(el[i])

    return links


def main():
    START_PAGE = get_query()
    END_PAGE = get_query()
    links = []
    links.append(create_request(START_PAGE))
    print(links)
    for link in links[0]:
        print(link)
        try:
            if END_PAGE in create_request(link):
                print('Yes')
                break
        except:
            continue
    else:
        print('No')

    # print(links)


if __name__ == '__main__':
    main()
