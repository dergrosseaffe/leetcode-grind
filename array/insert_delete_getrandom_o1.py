class RandomizedSet:

    def __init__(self):
        self.elements = {}
        self.data = []


    def insert(self, val: int) -> bool:
        if val not in self.elements:
            self.data.append(val)
            self.elements[val] = len(self.data) - 1
            return True

        return False


    def remove(self, val: int) -> bool:
        if val in self.elements:
            index_to_remove = self.elements[val]

            # swap with last element in the array
            new_index_element = self.data[-1]
            self.data[index_to_remove], self.data[-1] = self.data[-1], self.data[index_to_remove]

            # update swapped element index on dictionary
            self.elements[new_index_element] = index_to_remove

            # remove references to deleted element
            self.data.pop()
            del self.elements[val]

            return True

        return False

    def getRandom(self) -> int:
        return self.data[random.randint(0, len(self.data) - 1)]



# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
