from src.trip_service_kata.exceptions import UserNotLoggedInException
from src.trip_service_kata.trip import Trip, TripRepository
from src.trip_service_kata.user import User
from src.trip_service_kata.user_session import UserSession


class TripService:

    def get_trips_by_user(self, user: User) -> list[Trip]:
        logged_user = self.logged_user()
        is_friend = False
        trip_list = []
        if logged_user:
          for friend in user.get_friends():
            if friend is logged_user:
              is_friend = True
              break
          if is_friend:
            trip_list = self.find_trips_by(user)
          return trip_list
        else:
            raise UserNotLoggedInException()

    @staticmethod
    def find_trips_by(user: User) -> list[Trip]:
        return TripRepository.find_trips_by_user(user)

    @staticmethod
    def logged_user() -> User:
        return UserSession.get_instance().get_logged_user()
