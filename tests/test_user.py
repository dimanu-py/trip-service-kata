import unittest

from src.trip_service_kata.user import User


class TestUser(unittest.TestCase):

    def test_user_is_friend_of_other_user(self) -> None:
        user = User()
        friend = User()
        user.add_friend(friend)

        self.assertTrue(user.is_friend_of(friend))