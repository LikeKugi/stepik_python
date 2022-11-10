import requests
import shutil


def get_file(url: str) -> None:
    """
    get .xlsx file from url and save it to 'data.xlsx'
    :param url: str (url link)
    :return: None
    """
    res = requests.get(url, stream=True)

    if res.status_code == 200:
        with open('data.xlsx', 'wb') as ouf:
            res.raw.decode_content = True
            shutil.copyfileobj(res.raw, ouf)
