class RandomizedSet:

    def __init__(self):
        self.num = []
        self.num_dict = defaultdict(int)

    #num_dict[num]:index
    def insert(self, val: int) -> bool:
        if val not in self.num_dict:
            self.num.append(val)
            self.num_dict[val] = len(self.num)-1
            return True
        return False
        
    def remove(self, val: int) -> bool:
        if val in self.num_dict:
            index = self.num_dict[val]
            self.num_dict[self.num[-1]] = index
            self.num[index], self.num[-1] = self.num[-1], self.num[index]
            self.num.pop()
            del self.num_dict[val]
            return True
        return False

    def getRandom(self) -> int:
        return random.choice(self.num)