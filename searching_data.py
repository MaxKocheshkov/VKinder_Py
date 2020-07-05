from auth_data import TOKEN
from user_data import user_1, User
from vk_data import Vk, user_id, SEARCH_URL, params, age_to, age_from, search_status, PHOTO_URL
from tqdm import tqdm
import sys
from time import sleep
import pandas as pd
import csv
import json


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
        for common_data in value.get('items'):
            if common_data.get('common_count') is not 0:
                ids_list.append(common_data.get('id'))
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
                'gender': people_gender,
                'city': people_data.get('city')['title'],
            }
            found_people_list.append(people_dict)
    with open('people_df.csv', "w", newline="", encoding='utf8') as file:
        columns = ['ids', 'first name', 'last name', 'birth', 'gender', 'city']
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(found_people_list)
    return found_people_list


def get_people_photo():
    photo_list = []
    for people_id in people_info_data():
        photo_params = {
            'owner_id': people_id.get('ids'),
            'album_id': 'profile',
            'rev': 1,
            'extended': 1,
        }
        params.update(photo_params)
        people_photo = Vk(TOKEN, people_id.get('ids'))
        for people_photo_info in people_photo.get_request(PHOTO_URL, params).values():
            photo_info = people_photo_info.get('items')
            if photo_info is not None:
                for photo_data in photo_info:
                    photo_dict = {
                        'ids': photo_data.get('owner_id'),
                        'photo url': photo_data.get('sizes')[-1].get('url'),
                        'photo likes': photo_data.get('likes').get('count')
                    }
                    photo_list.append(photo_dict)
    with open('photo_df.csv', "w", newline="") as file:
        columns = ['ids', 'photo url', 'photo likes']
        writer = csv.DictWriter(file, fieldnames=columns)
        writer.writeheader()
        writer.writerows(photo_list)
    return photo_list


def sort_df():
    get_people_photo()
    p_df = pd.read_csv('people_df.csv')
    ph_df = pd.read_csv('photo_df.csv')
    ph_df = ph_df.sort_values('photo likes').groupby('ids')['ids', 'photo url', 'photo likes'].max()
    ph_df = ph_df.reset_index(drop=True)
    union_df = pd.merge(p_df, ph_df, on='ids', how='outer')
    sort_data_df = union_df.sort_values('photo likes', ascending=False).reset_index(drop=True)
    n_sort_df = sort_data_df.head(10)
    return n_sort_df

