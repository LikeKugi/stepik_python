import requests
from bs4 import BeautifulSoup


def get_request() -> requests.get:
    res = requests.get('https://stepik.org/media/attachments/lesson/209723/5.html')
    print(f'response status: {res.status_code}')
    return res


def write_file(res: requests.get) -> None:
    with open('response.txt', 'w') as ouf:
        ouf.writelines(res.text)


def read_file() -> str:
    with open('response.txt') as inf:
        data = inf.read().replace('\n', '')
    return data


def create_soup(data: str) -> BeautifulSoup:
    soup = BeautifulSoup(data, 'lxml')
    print(soup)
    return soup


def find_numbers(soup: BeautifulSoup) -> list:
    numbers = []
    for tag in soup.find_all("td"):
        numbers.append(int(tag.text.strip()))
    return numbers


def main() -> None:
    # res = get_request()
    # write_file(res)
    data = read_file()
    soup = create_soup(data)
    numbers = find_numbers(soup)
    print(numbers)
    print(sum(numbers))


if __name__ == '__main__':
    main()
