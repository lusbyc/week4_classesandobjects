#Exercise Lab 1: Restaurant Class
class Restaurant:
    def __init__(self, name, cuisine):
        self.name = name
        self.cuisine = cuisine

    def welcome(self):
        print(f"We are {self.name} and we specialize in {self.cuisine} food.\n")
    

r1 = Restaurant("Honey Molasses", "cajun")
r2 = Restaurant("Island Breeze", "island")
r3 = Restaurant("Pho", "Vietnamese")

r1.welcome()
r2.welcome()
r3.welcome()

#Exercise Lab 2 and 3: User Class
class User:

    favorite_restaurants = []

    def __init__(self, name, age, nationality):
        self.name = name
        self.age = age
        self.nationality = nationality


    def description(self):
        print(f"Name: {self.name}\nAge: {self.age}\nNationality: {self.nationality}")
        for restaurant in self.favorite_restaurants:
            print(restaurant)
        print()

user1 = User("Charlotte", 25, "American")
user2 = User("Chloe", 4, "Jamaican")

user1.description()
user2.description()

user3 = User("Mark", 16, "Canadian")
user4 = User("Jill", 37, "French")

user3.favorite_restaurants.append(r1.name)
user4.favorite_restaurants.append(r3.name)
user3.description()
user4.description()
