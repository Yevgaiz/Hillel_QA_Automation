import pytest
import requests

url = "https://gorest.co.in/public/v2"
headers = {"Accept": "application/json",
           "Content-Type": "application/json",
           "Authorization": "Bearer 4290fc157d1bd03cba9fd9766d9e4cefac05e9a8fb9dee9ddbe5e9874510641f"
           }


@pytest.fixture
def create_user():
    user_data = {
        "name": "Ivan Ivanov",
        "email": "ivanov_ivan@test.com",
        "gender": "male",
        "status": "active"
    }

    response = requests.post(f"{url}/users", headers=headers, json=user_data)
    response.raise_for_status()
    user = response.json()
    print(f"User created: {user}")

    yield user

    delete_response = requests.delete(f"{url}/users/{user['id']}", headers=headers)
    delete_response.raise_for_status()
    print(f"User deleted: {user}")


def create_post(user_id):
    post_data = {
        "title": "Test Title",
        "body": "Body of the test post",
        "user_id": user_id
    }

    response = requests.post(f"{url}/posts", headers=headers, json=post_data)
    response.raise_for_status()
    post = response.json()
    print(f"Post created: {post}")
    return post


def test_create_post(create_user):
    post = create_post(create_user['id'])

    assert post['title'] == "Test Title"
    assert post['body'] == "Body of the test post"
    assert post['user_id'] == create_user['id']


if __name__ == "__main__":
    pytest.main()
