from src.trip_service_kata.exceptions import UserNotLoggedInException
from src.trip_service_kata.trip import Trip, TripRepository
from src.trip_service_kata.user import User
from src.trip_service_kata.user_session import UserSession


class TripService:

    def get_trips_by_user(self, user: User) -> list[Trip]:
        logged_user = UserSession.get_instance().get_logged_user()
        is_friend = False
        trip_list = []
        if logged_user:
          for friend in user.get_friends():
            if friend is logged_user:
              is_friend = True
              break
          if is_friend:
            trip_list = TripRepository.find_trips_by_user(user)
          return trip_list
        else:
            raise UserNotLoggedInException()
