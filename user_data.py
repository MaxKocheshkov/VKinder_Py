from vk_data import Vk, USER_URL, params, TOKEN, user_id


class User(Vk):

    def get_user(self):
        user_param = {'fields': 'bdate, sex, city, screen_name'}
        params.update(user_param)
        user_info = Vk(TOKEN, user_id).get_request(USER_URL, params)
        return user_info

    def user_info_data(self):
        for user_value in self.get_user().values():
            user_dict = user_value[0]
            if user_dict['sex'] == 2:
                gender = 'М'
            else:
                gender = 'Ж'
            new_user_dict = {
                'ids': user_dict['id'],
                'first name': user_dict.get('first_name'),
                'last name': user_dict.get('last_name'),
                'birth': user_dict.get('bdate'),
                'city': user_dict.get('city'),
                'gender': gender,
            }
            return new_user_dict


user_1 = User(TOKEN, user_id)
