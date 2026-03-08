class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def display(self):
        print(f"{self.name}:{self.height} cm,{self.age} days old")


if __name__ == "__main__":
    print("=== Garden Plant Registry ===")

    plant = Plant("Rose", 25, 30)
    plant.display()

    plant = Plant("Sunflower", 80, 45)
    plant.display()

    plant = Plant("Cactus", 15, 120)
    plant.display()
