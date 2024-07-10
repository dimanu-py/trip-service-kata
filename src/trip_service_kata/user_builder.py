from src.trip_service_kata.trip import Trip
from src.trip_service_kata.user import User


class UserBuilder:

    def __init__(self):
        self.trips: list[Trip] = []
        self.friends: list[User] = []

    def friends_with(self, *friends: list[User]) -> "UserBuilder":
        self.friends = list(friends)
        return self

    def with_trips_to(self, *trips: Trip) -> "UserBuilder":
        self.trips = list(trips)
        return self

    def build(self) -> User:
        user = User()
        for friend in self.friends:
            user.add_friend(friend)
        for trip in self.trips:
            user.add_trip(trip)
        return user
