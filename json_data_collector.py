import json
import urllib.request
from math import *

users = 'https://jsonplaceholder.typicode.com/users'
posts = 'https://jsonplaceholder.typicode.com/posts'


class UsersPosts:

    # downloading data from websites
    @staticmethod
    def download_data(link):

        r = urllib.request.urlopen(link)
        data = json.loads(r.read().decode())

        return data

    # assigning posts to authors
    @staticmethod
    def add_posts_to_user():

        users_data = UsersPosts.download_data(users)
        posts_data = UsersPosts.download_data(posts)

    # add additional key posts to users
        for user in users_data:

            user['posts'] = []

    # add to user all its posts
        for post in posts_data:

            for user in users_data:

                if user['id'] == post['userId']:
                    user['posts'].append(post)

        return users_data

    # print usernames and quantity of posts
    @staticmethod
    def get_username_and_posts_quantity():

        users_data = UsersPosts.add_posts_to_user()

        for user in users_data:
            print(f'User: {user["username"]} napisał(a) {len(user["posts"])} postów.')

        return None

    # check are existing two or more same post titles
    @staticmethod
    def check_same_titles():

        not_unique_post_title = []

        posts_data = UsersPosts.download_data(posts)

        # comparing posts titles
        for post in posts_data:
            count = (str(posts_data).count(str(post['title'])))
            if count > 1:
                not_unique_post_title.append(post['title'])

        # print all repeated titles
        for title in not_unique_post_title:
            print(f'Powtórzony tytuł: {title}')

        return not_unique_post_title

    # method which returns user who is living closest
    @staticmethod
    def get_geo_data(userId):

        users_data = UsersPosts.download_data(users)
        user_a = ''
        user_b = ''
        distance = 50000
        for user in users_data:
            if user['id'] == userId:
                user_a = user

        for user in users_data:

            localisation =round(acos(sin(radians(float(user_a['address']['geo']['lat'])))*sin(
                    radians(float(user['address']['geo']['lat'])))+cos(
                    radians(float(user_a['address']['geo']['lat'])))*cos(
                    radians(float(user['address']['geo']['lat'])))*cos(
                    radians(float(user_a['address']['geo']['lng'])-float(user['address']['geo']['lng']))))*6371)

            if localisation == 0:
                pass

            elif localisation < distance:
                distance = localisation
                user_b = user

        return user_b['username']


if __name__ == "__main__":

    same_titles = UsersPosts.check_same_titles()
    all_posts = UsersPosts.add_posts_to_user()
    closest_friend = UsersPosts.get_geo_data(4)
    get_username = UsersPosts.get_username_and_posts_quantity()


