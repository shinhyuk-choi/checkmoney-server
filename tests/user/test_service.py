from django.core.exceptions import ValidationError
from django.db import IntegrityError
from django.test import TestCase

from user import models
from user.models import User
from user.services import UserService


class TestUser(TestCase):
    @classmethod
    def setUpTestData(cls):
        user = UserService().create(
            email="test@email.com",
            password=1111
        )

    def test_create_duplicate_email_user(self):
        result = False
        try:
            user = UserService().create(
                email="test@email.com",
                password=1111
            )
        except IntegrityError:
            result = True
        assert result

    def test_create_no_password_user(self):
        have_not_key = False
        have_not_value = False
        try:
            user = UserService().create(
                email="test2@email.com"
            )
        except ValidationError:
            have_not_key = True
        try:
            user = UserService().create(
                email="test2@email.com",
                password=''
            )
        except ValidationError:
            have_not_value = True
        assert (have_not_key and have_not_value)

    def test_create_user(self):
        user = UserService().create(
            email="test2@email.com",
            password=1111
        )
        assert user == User.objects.get(email="test2@email.com")
