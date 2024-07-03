from src.trip_service_kata.exceptions import UserNotLoggedInException
from src.trip_service_kata.trip import Trip, TripRepository
from src.trip_service_kata.user import User
from src.trip_service_kata.user_session import UserSession


class TripService:
    NO_TRIPS = []

    def get_trips_by_user(self, user: User) -> list[Trip]:
        logged_user = self.logged_user()
        if not logged_user:
            raise UserNotLoggedInException()

        if user.is_friend_of(logged_user):
            return self.find_trips_by(user)
        return self.NO_TRIPS

    @staticmethod
    def find_trips_by(user: User) -> list[Trip]:
        return TripRepository.find_trips_by_user(user)

    @staticmethod
    def logged_user() -> User:
        return UserSession.get_instance().get_logged_user()
