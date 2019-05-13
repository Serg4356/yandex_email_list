import requests
from pprint import pprint


pdd_token='COTPKELAA4GBLULVCFFIPKPKR4YDTM4AJFRCYMIPKXRGBUVD2VUA'

if __name__ == '__main__':
    url = 'http://pddimp.yandex.ru/api2/admin/email/list'
    params = {
        'on_page': 100,
        'domain': 'cskorp.ru',
    }
    headers = {
        'PddToken': pdd_token,
    }
    response = requests.get(url, params=params, headers=headers)
    accounts_str = ''
    for account in response.json()['accounts']:
        accounts_str += '{} | {}\n'.format(account['fio'], account['login'])

    with open('accounts.txt', 'w') as acc_file:
        acc_file.write(accounts_str)

