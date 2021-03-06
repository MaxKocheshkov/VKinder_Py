from pymongo import MongoClient
from config_init.searching_data import sort_df
import pprint
import os


def people_db(db):
    result = db.insert_many(sort_df().to_dict('records'))
    os.remove('config_init/people_df.csv')
    os.remove('config_init/photo_df.csv')
    return result


if __name__ == '__main__':
    client = MongoClient()
    date_db = client['VKinder_v_3_1']
    people_base = date_db['Find_people_DB']
    people_db(people_base)
    pprint.pprint(list(people_base.find()))
