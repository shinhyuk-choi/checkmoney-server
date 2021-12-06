from django.test import TestCase

from user.services import UserService


class TestUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = UserService().create(
            email="test@email.com",
            password=1111
        )
        backend = 'django.contrib.auth.backends.ModelBackend'

    def test_post_users(self):
        data = dict()
        response = self.client.post('/users/', data=data)
        assert response.status_code == 400

        data['email'] = 'test1@email.com'
        response = self.client.post('/users/', data=data)
        assert response.status_code == 400

        data['password'] = ''
        response = self.client.post('/users/', data=data)
        assert response.status_code == 400

        data['password'] = 1111
        response = self.client.post('/users/', data=data)
        assert response.status_code == 201

        result = response.json()
        assert result.get('email') == 'test1@email.com'
        assert 'id' in result.keys()
        assert 'token' in result.keys()
