class FoodRatings:

    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        
        self.values = defaultdict(list)
        self.food = defaultdict(list)
        for i in range(len(foods)):
            heapq.heappush(self.values[cuisines[i]],(-ratings[i],foods[i]))
            self.food[foods[i]] = [ratings[i],cuisines[i]]
        

    def changeRating(self, food: str, newRating: int) -> None:
        
        cuisine = self.food[food][1]
        self.food[food][0] = newRating
        heappush(self.values[cuisine],(-newRating,food))
        

    def highestRated(self, cuisine: str) -> str:
        
        while self.values[cuisine][0][0] * -1 != self.food[self.values[cuisine][0][1]][0]:
            heappop(self.values[cuisine])
        
        return self.values[cuisine][0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)