class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def get_info(self):
        print(f"{self.name}:{self.height} cm,{self.age} days old")


if __name__ == "__main__":
    lst = [
        Plant("Rose", 25, 30),
        Plant("Oak", 200, 365),
        Plant("Cactus", 5, 90),
        Plant("Sunflower", 80, 45),
        Plant("Fern", 15, 120),
    ]

    count = 0
    for plant in lst:
        print(f"Created: {plant.name} ({plant.height}cm, {plant.age} days)")
        count += 1

    print(f"Total plants created: {count}")
