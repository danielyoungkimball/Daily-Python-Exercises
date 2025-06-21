from typing import List

class Cat:
    __slots__ = ['name', 'age', 'tricks']  # restricts attributes to save memory

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.tricks: List[str] = []

    def __repr__(self):
        return f"Cat(name={self.name!r}, age={self.age})"

    def __str__(self):
        return f"{self.name}, age {self.age}, knows {len(self.tricks)} tricks"

    def __eq__(self, other):
        return isinstance(other, Cat) and self.name == other.name and self.age == other.age

    def __lt__(self, other):
        return self.age < other.age  # younger cat is "less than" older cat

    def __len__(self):
        return len(self.tricks)  # len(cat) gives number of tricks

    def __getitem__(self, index):
        return self.tricks[index]  # cat[0] returns first trick

    def __setitem__(self, index, value):
        self.tricks[index] = value  # cat[0] = "new trick"

    def __call__(self):
        print(f"{self.name} jumps on your lap 🐾")

    def add_trick(self, trick: str):
        self.tricks.append(trick)

# === Demo ===
if __name__ == "__main__":
    joji = Cat("Joji", 3)
    joji.add_trick("sit")
    joji.add_trick("spin")

    print(joji)                      # __str__
    print(repr(joji))               # __repr__
    print(f"Number of tricks: {len(joji)}")  # __len__

    joji()                          # __call__

    print("First trick:", joji[0])  # __getitem__
    joji[1] = "high five"           # __setitem__
    print("Updated trick:", joji[1])

    another_cat = Cat("Joji", 3)
    print("Is Joji == another_cat?", joji == another_cat)  # __eq__

    older_cat = Cat("Whiskers", 5)
    print("Is Joji < Whiskers?", joji < older_cat)  # __lt__
