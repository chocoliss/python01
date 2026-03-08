class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"{self.name}:{self.height} cm,{self.age} days old")

    def grow(self):
        self.height += 1

    def grow_age(self):
        self.age += 1


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    plant = Plant("Rose", 25, 30)
    plant.get_info()

    days = 7
    for i in range(days - 1):
        plant.grow_age()
        plant.grow()

    print(f"=== Day {days} ===")
    plant.get_info()
    print(f"Growth this week: +{days - 1}cm")
