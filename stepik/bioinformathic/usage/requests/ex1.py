#  Вашей программе на вход подается ссылка на HTML файл.
# Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... >
# и вывести список сайтов, на которые есть ссылка.

import requests
import re

a1 = [
    'adworker.ru', 'banner.rbc.ru', 'biztorg.ru', 'blogi.rbc.ru', 'cnews.ru',
    'consensus.rbc.ru', 'conv.rbc.ru', 'credit.rbc.ru', 'data.rbc.ru', 'dict.rbc.ru',
    'drinktime.ru', 'events.cnews.ru', 'export.rbc.ru', 'finolymp.ru', 'gift.cnews.ru',
    'graph.rbc.ru', 'magazine.rbc.ru', 'map.rbc.ru', 'marketing.rbc.ru', 'memori.ru',
    'otc-pif.rbc.ru', 'otc-stock.rbc.ru', 'pda.rbc.ru', 'pogoda.rbc.ru', 'portfolio.rbc.ru',
    'quote-otc.rbc.ru', 'quote.ru', 'raiting.rbc.ru', 'rating.rbc.ru', 'realty.rbc.ru', 'redir.rbc.ru',
    'rss.rbc.ru', 'seminar.rbc.ru', 'spb.rbc.ru', 'sport.rbc.ru', 'static.feed.rbc.ru',
    'stock.rbc.ru', 'style.rbc.ru', 'ta.rbc.ru', 'tata.ru', 'top.rbc.ru', 'top100.rambler.ru',
    'turbo.ru', 'tv.rbc.ru', 'ug.rbc.ru', 'ulov-umov.ru', 'videoarchive.rbc.ru',
    'www.5ballov.ru', 'www.armd.ru', 'www.autonews.ru', 'www.biztorg.ru', 'www.cnews.ru',
    'www.conf.rbc.ru', 'www.event.rbc.ru', 'www.iglobe.ru', 'www.informer.ru', 'www.ivd.ru',
    'www.liveinternet.ru', 'www.m-2.ru', 'www.nashidengi.ru', 'www.pochta.ru', 'www.quote.ru',
    'www.quoterate.ru', 'www.quotetotal.ru', 'www.rbc.ru', 'www.rbc.ua', 'www.rbcdaily.ru',
    'www.rbcinfosystems.com', 'www.rbcnews.com', 'www.rbctv.ru', 'www.refunder.ru',
    'www.salon.ru', 'www.seminar.rbc.ru', 'www.top.rbc.ru', 'www.turbo.ru', 'www.turist.ru',
    'www.utro.ru', 'www.worldclass.ru', 'zoom.cnews.ru'
]

a2 = ['bya-2.ru', 'bya.ru', 'mail-2.ru', 'mail.ru', 'neerc.ifmo-2.ru', 'neerc.ifmo.ru', 'sas-_0123d.ifmo.ru',
      'sasd.ifmo-2.ru', 'steeeeeeepic.org', 'stepic-2.org', 'stepic.org', 'test.com', 'www.gtu.edu-2.ge',
      'www.gtu.edu.ge',
      'www.kya-2.ru', 'www.kya.ru', 'www.masdaya.ru', 'www.mya-2.ru', 'www.ya-2.ru', 'www.ya.ru'
      ]

a3 = ['bya.ru', 'mail.ru', 'neerc.ifmo.ru', 'sasd.ifmo.ru',
      'stepic.org', 'www.gtu.edu.ge', 'www.kya.ru',
      'www.mya.ru', 'www.ya.ru'
      ]


# Эта функция сравнивает твой ответ с правильным ответом.
# Функция принимает список из ответов
def checker(*answer):
    # для смены теста поменяй в условиях a1 на a2 или a3
    print(set(a1) - set(answer))
    for ans in answer:
        if ans not in a1:
            print('Wrong answer! [', answer, ']\n')


def get_query(): return input()


def create_request(page: str) -> list:
    links = []
    print(f'parsing {page}')
    req = requests.get(page)
    pattern = re.compile(r'''<a[^>]*?href=['"](.*?)['"][^>]*?>''')
    l = re.findall(pattern, req.text)
    links.extend(l)

    return links


def main():
    # парсим эти ссылки как по заданию
    urlForA1 = 'http://pastebin.com/raw/7543p0ns'  # Для теста a1
    urlForA2 = 'http://pastebin.com/raw/hfMThaGb'  # Для теста a2
    urlForA3 = 'http://pastebin.com/raw/2mie4QYa'  # Для теста a3

    # здесь вставляем ссылку urlForA1/urlForA2/urlForA3 /под каждую ссылку свой тест


    # твой код



    links = []
    out_links = set()
    links.extend(create_request(urlForA1))
    # print(links)
    for link in links:
        if link[0].isalpha():
            link = link.replace('ftp://', '').replace('http://', '').replace('https://', '').replace(':', '/')
            # print(link)
            if link.find('/') > -1:
                out_links.add(link[:link.find('/')])
            else:
                out_links.add(link)
    else:
        print('end')

    checker(*sorted(out_links))

    with open('out_links.txt', 'w') as ouf:
        print(*sorted(out_links), sep='\n', file=ouf)


if __name__ == '__main__':
    main()
