from src.trip_service_kata.exceptions import DependendClassCallDuringUnitTestException
from src.trip_service_kata.user import User


class Trip:
  pass


class TripRepository:
  @staticmethod
  def find_trips_by_user(user: User) -> Trip:
    raise DependendClassCallDuringUnitTestException("TripDAO should not be invoked on an unit test.")