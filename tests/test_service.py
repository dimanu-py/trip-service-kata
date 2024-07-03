import unittest

from src.trip_service_kata.exceptions import UserNotLoggedInException
from src.trip_service_kata.service import TripService


class SeamTripService(TripService):
    
    @staticmethod
    def logged_user():
        return None


class TestTripService(unittest.TestCase):

    def test_user_cannot_get_trips_if_is_not_logged_in(self) -> None:
        trip_service = SeamTripService()
        with self.assertRaises(UserNotLoggedInException):
            trip_service.get_trips_by_user(None)