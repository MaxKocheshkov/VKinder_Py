import requests
from config_init.auth_data import TOKEN

user_id = input('Введите id пользователя: ')
age_from = input('Введите диапазон возраста для поиска от: ')
age_to = input('до: ')
search_status = int(input('Введите значение семейного положения для поиска \n '
                          '(1 — не женат (не замужем); 2 — встречается; 3 — помолвлен(-а);'
                          '4 — женат (замужем); 5 — всё сложно; 6 — в активном поиске;'
                          '7 — влюблен(-а); 8 — в гражданском браке): '))

USER_URL = 'http://api.vk.com/method/users.get'
FRIEND_URL = 'http://api.vk.com/method/friends.get'
GROUP_URL = 'http://api.vk.com/method/groups.get'
SEARCH_URL = 'https://api.vk.com/method/users.search'
PHOTO_URL = 'https://api.vk.com/method/photos.get'


params = {
    'access_token': TOKEN,
    'user_id': user_id,
    'v': 5.103,
}


class Vk:

    def __init__(self, token, user_id):
        self.token = token
        self.user_id = user_id

    def get_request(self, url, params):
        response = requests.get(
            url,
            params,
        )
        return response.json()
