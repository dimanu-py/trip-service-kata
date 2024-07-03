import unittest

from src.trip_service_kata.exceptions import UserNotLoggedInException
from src.trip_service_kata.service import TripService
from src.trip_service_kata.trip import Trip
from src.trip_service_kata.user import User


class SeamTripService(TripService):

    def __init__(self, test_instance):
        self.test_instance = test_instance
    
    def logged_user(self) -> User:
        return self.test_instance.logged_user

    def find_trips_by(self, user: User) -> list[Trip]:
        return user.trips


class TestTripService(unittest.TestCase):
    GUEST_USER = None
    APPLICATION_USER = User()
    GENERIC_USER = User()
    GREECE = Trip()

    def setUp(self):
        self.logged_user = self.APPLICATION_USER
        self.trip_service = SeamTripService(self)

    def test_user_cannot_get_trips_if_is_not_logged_in(self) -> None:
        self.logged_user = self.GUEST_USER

        with self.assertRaises(UserNotLoggedInException):
            self.trip_service.get_trips_by_user(self.GUEST_USER)

    def test_user_gets_no_trips_if_is_not_friend(self) -> None:
        stranger = User()
        stranger.add_friend(self.GENERIC_USER)
        stranger.add_trip(self.GREECE)

        trips = self.trip_service.get_trips_by_user(stranger)

        self.assertEqual(trips, [])

    def test_user_gets_trips_of_friend(self) -> None:
        friend = User()
        friend.add_friend(self.logged_user)
        friend.add_trip(self.GREECE)

        trips = self.trip_service.get_trips_by_user(friend)

        self.assertEqual(trips, [self.GREECE])