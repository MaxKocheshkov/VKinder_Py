from auth_data import TOKEN
from user_data import user_1, User
from vk_data import Vk, user_id, SEARCH_URL, params, age_to, age_from, search_status, PHOTO_URL
from tqdm import tqdm
import sys
from time import sleep
import pandas as pd


def get_search():
    for value in tqdm(user_1.get_user().values(), file=sys.__stdout__):
        user_data = value[0]
        if user_data['sex'] == 1:
            searching_sex = 2
        else:
            searching_sex = 1
        search_params = {
            'count': 1000,
            'fields': 'bdate, city, common_count',
            'sex': searching_sex,
            'city': int(user_data['city']['id']),
            'age_from': int(age_from),
            'age_to': int(age_to),
            'status': search_status,
            'has_photo': 1,
        }
        params.update(search_params)
    search_info = Vk(TOKEN, user_id).get_request(SEARCH_URL, params)
    return search_info


def get_common_count():
    ids_list = []
    for value in tqdm(get_search().values(), file=sys.__stdout__):
        for common_data in value['items']:
            if common_data['common_count'] is not 0:
                ids_list.append(common_data['id'])
    return ids_list


def ids_info():
    info_list = []
    for ids in tqdm(get_common_count(), file=sys.__stdout__):
        ids_params = {
            'user_id': ids,
            'fields': 'bdate, relation, common_count',
        }
        params.update(ids_params)
        people_info = User(TOKEN, ids)
        sleep(0.5)
        for info_values in people_info.get_user().values():
            info_list.append(info_values)
            sleep(0.5)
    return info_list


def people_info_data():
    found_people_list = []
    for elements in tqdm(ids_info(), file=sys.__stdout__):
        for people_data in tqdm(elements, file=sys.__stdout__):
            if people_data.get('sex') == 2:
                people_gender = 'М'
            else:
                people_gender = 'Ж'
            people_dict = {
                'ids': people_data.get('id'),
                'first name': people_data.get('first_name'),
                'last name': people_data.get('last_name'),
                'birth': people_data.get('bdate'),
                'city': people_data.get('city')['title'],
                'gender': people_gender,
            }
            found_people_list.append(people_dict)
    return found_people_list


# def get_people_photo():
#     for ids in tqdm(get_common_count(), file=sys.__stdout__):
#         photo_params = {
#             'owner_id': ids,
#             'album_id': 'profile',
#             'rev': 1,
#             'extended': 1,
#         }
#         params.update(photo_params)
#         people_photo = Vk(TOKEN, ids).get_request(PHOTO_URL, params)
#         return people_photo
# for photo_values in people_photo.values():
#     photo_elem = photo_values.get('items')
#     return photo_elem


def sort_people_df():
    people_df = pd.DataFrame(people_info_data())
    p_df = people_df[['ids', 'first name', 'last name', 'birth', 'gender', 'city']]
    p_df_sort = p_df.head(10)
    p_df_sort.to_json('sort_people_DF.json', force_ascii=False)
    return p_df_sort
