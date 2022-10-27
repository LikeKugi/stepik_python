# Ваша задача написать функцию get_domain_name, которая принимает строку url,
# извлекает из нее доменное имя и возвращает его в качестве строки


def get_domain_name(url: str) -> str:
    start_index = max(url.find('://')+3, url.find('www.')+4)
    end_index = url.find('.', start_index + 1)
    return url[start_index:end_index]


checks = ["http://google.com", "http://google.co.jp", "www.xakep.ru", "https://youtube.com", "https://www.asos.com",
          "http://www.lenovo.com"]

for check in checks:
    print(get_domain_name(check))
