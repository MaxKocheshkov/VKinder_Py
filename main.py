from pymongo import MongoClient
from searching_data import sort_people_df


def people_db(db):
    result = db.insert_many(sort_people_df().to_dict('records'))
    return result


client = MongoClient()
date_db = client['VKinder_v_1_8']
people_base = date_db['Find_people_DB']
people_db(people_base)
print(list(people_base.find()))


