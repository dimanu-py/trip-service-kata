import unittest

from src.trip_service_kata.exceptions import UserNotLoggedInException
from src.trip_service_kata.service import TripService
from src.trip_service_kata.user import User


class SeamTripService(TripService):

    def __init__(self, test_instance):
        self.test_instance = test_instance
    
    def logged_user(self) -> User:
        return self.test_instance.application_user


class TestTripService(unittest.TestCase):

    def setUp(self):
        self.application_user = None
        self.trip_service = SeamTripService(self)

    def test_user_cannot_get_trips_if_is_not_logged_in(self) -> None:
        with self.assertRaises(UserNotLoggedInException):
            self.trip_service.get_trips_by_user(None)
