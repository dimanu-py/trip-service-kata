import unittest
from unittest.mock import Mock

from src.trip_service_kata.exceptions import UserNotLoggedInException
from src.trip_service_kata.service import TripService
from src.trip_service_kata.trip import Trip, TripRepository
from src.trip_service_kata.user import User
from src.trip_service_kata.user_builder import UserBuilder


class TestTripService(unittest.TestCase):
    GUEST_USER = None
    APPLICATION_USER = User()
    GENERIC_USER = User()
    GREECE = Trip()

    def setUp(self):
        self.logged_user = self.APPLICATION_USER
        self.trip_repository = Mock(TripRepository)
        self.trip_service = TripService(self.trip_repository)

    def test_user_cannot_get_trips_if_is_not_logged_in(self) -> None:
        self.logged_user = self.GUEST_USER

        with self.assertRaises(UserNotLoggedInException):
            self.trip_service.get_trips_by_user(self.GUEST_USER, self.logged_user)

    def test_user_gets_no_trips_if_is_not_friend(self) -> None:
        stranger = (UserBuilder()
                    .friends_with([self.GENERIC_USER])
                    .build())

        trips = self.trip_service.get_trips_by_user(stranger, self.logged_user)

        self.assertEqual(trips, [])

    def test_user_gets_trips_of_friend(self) -> None:
        friend = (UserBuilder()
                  .friends_with([self.logged_user])
                  .with_trips_to([self.GREECE])
                  .build())
        self.trip_repository.find_trips_by_user.return_value = friend.trips

        trips = self.trip_service.get_trips_by_user(friend, self.logged_user)

        self.assertEqual(trips, [self.GREECE])