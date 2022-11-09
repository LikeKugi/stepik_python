from xlsx_parse import get_file


def main():
    url = 'https://stepik.org/media/attachments/lesson/245267/salaries.xlsx'
    get_file(url)


if __name__ == '__main__':
    main()
