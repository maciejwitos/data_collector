from json_data_collector import UsersPosts

users = 'https://jsonplaceholder.typicode.com/users'
posts = 'https://jsonplaceholder.typicode.com/posts'


def test_check_same_titles():
    assert UsersPosts.check_same_titles() == []


def test_add_post_to_user():
    data = UsersPosts.add_posts_to_user()
    assert data[0]['posts'][0]['title'] == 'sunt aut facere repellat provident occaecati excepturi optio reprehenderit'


def test_get_geo_data():
    name = UsersPosts.get_geo_data(1)
    assert name == 'Kamren'


def test_download_data():
    assert type(UsersPosts.download_data(users)) == list


def test_get_username_and_posts_quantity():
    assert UsersPosts.get_username_and_posts_quantity() == None
