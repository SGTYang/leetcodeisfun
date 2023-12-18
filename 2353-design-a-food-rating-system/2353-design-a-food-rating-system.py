from sortedcontainers import SortedSet

class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        self.cuisines_ratings = defaultdict(SortedSet)
        self.foods_cuisines = {}
        self.foods_ratings = {}
        
        for i in range(len(foods)):
            self.cuisines_ratings[cuisines[i]].add((-ratings[i], foods[i]))    
            self.foods_cuisines[foods[i]] = cuisines[i]
            self.foods_ratings[foods[i]] = ratings[i]
        
    def changeRating(self, food: str, newRating: int) -> None:
        curr_cuisine = self.foods_cuisines[food]
        prev_rating = self.foods_ratings[food]
        
        self.cuisines_ratings[curr_cuisine].remove((-prev_rating, food))
        self.cuisines_ratings[curr_cuisine].add((-newRating, food))
        self.foods_ratings[food] = newRating

    def highestRated(self, cuisine: str) -> str:
        return self.cuisines_ratings[cuisine][0][1]
        


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)