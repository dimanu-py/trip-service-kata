

class User:

    def __init__(self):
        self.trips: list = []
        self.friends: list[User] = []

    def add_friend(self, user: "User") -> None:
        self.friends.append(user)

    def add_trip(self, trip) -> None:
        self.trips.append(trip)

    def get_trips(self) -> list:
        return self.trips

    def is_friend_of(self, other_user: "User") -> bool:
        return other_user in self.friends
