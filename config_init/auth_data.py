from urllib.parse import urlencode
import re
import configparser
import subprocess

APP_ID = 7530136
OAUTH_URL = 'https://oauth.vk.com/authorize'
OAUTH_PARAMS = {
    'client_id': APP_ID,
    'display': 'page',
    'scope': 'offline, user, friends',
    'response_type': 'token',
    'v': '5.52'
}

try:
    config = configparser.ConfigParser()
    config.read('token.ini')
    TOKEN = config.get('APP_TOKEN', 'token')
except configparser.NoSectionError:
    open_url = '?'.join((OAUTH_URL, urlencode(OAUTH_PARAMS)))
    print(f'Перейдите по сслыке и скопируйте данные из адресной строки: {open_url}')
    token_url = input('Введите полученную ссылку: ')
    token_regex = re.compile(r'\w{6}\_\w{5}\=(.{85})')
    user_token = token_regex.findall(str(token_url))
    config = configparser.ConfigParser()
    config.add_section('APP_TOKEN')
    config.set('APP_TOKEN', 'token', user_token[0])
    with open('token.ini', "w") as config_file:
        config.write(config_file)
    config.read('token.ini')
    TOKEN = config.get('APP_TOKEN', 'token')

subprocess.call(['attrib', '+h', 'token.ini'])