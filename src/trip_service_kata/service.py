from src.trip_service_kata.exceptions import UserNotLoggedInException
from src.trip_service_kata.trip import Trip, TripRepository
from src.trip_service_kata.user import User
from src.trip_service_kata.user_session import UserSession


class TripService:
    NO_TRIPS = []

    def __init__(self, trip_repository: TripRepository = None) -> None:
        self.trip_repository = trip_repository

    def get_trips_by_user(self, user: User, logged_user: User) -> list[Trip]:
        self.validate(logged_user)

        return self.trip_repository.find_trips_by_user(user) if user.is_friend_of(logged_user) else self.NO_TRIPS

    @staticmethod
    def validate(logged_user: User) -> None:
        if not logged_user:
            raise UserNotLoggedInException()

    @staticmethod
    def find_trips_by(user: User) -> list[Trip]:
        return TripRepository.find_trips_by_user(user)
