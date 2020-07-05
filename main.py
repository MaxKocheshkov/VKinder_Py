from pymongo import MongoClient
from searching_data import sort_df
import pprint
import os


def people_db(db):
    result = db.insert_many(sort_df().to_dict('records'))
    os.remove('people_df.csv')
    os.remove('photo_df.csv')
    return result


client = MongoClient()
date_db = client['VKinder_v_2_2']
people_base = date_db['Find_people_DB']
people_db(people_base)
pprint.pprint(list(people_base.find()))


