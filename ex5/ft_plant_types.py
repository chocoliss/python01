class Plant:
    def __init__(self, name: str, height: int, age: int) -> None:
        self.name = name
        self.height = height
        self.age = age

    def info(self):
        print(f"{self.name}:{self.height} cm,{self.age} days,", end="")


class Tree(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        trunk_diameter: int
    ) -> None:
        super().__init__(name, height, age)
        self.diameter = trunk_diameter

    def get_info(self) -> None:
        super().info()
        print(f"{self.diameter}cm diameter")

    def produce_shade(self) -> None:
        shade = 3.1416 * ((self.diameter * 10) ** 2) / 10000
        print(
            f"{self.name} provides {shade:.0f} "
            f"square meters of shade"
        )


class Flower(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        color_attribute: str
    ) -> None:
        super().__init__(name, height, age)
        self.color_attribute = color_attribute

    def get_info(self) -> None:
        super().info()
        print(self.color_attribute, "color")

    def bloom(self) -> None:
        print(f"{self.name} is blooming beautifully!")


class Vegetable(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        age: int,
        harvest_season: str,
        nutritional_value: str
    ) -> None:
        super().__init__(name, height, age)
        self.season = harvest_season
        self.nutritional_value = nutritional_value

    def get_info(self) -> None:
        super().info()
        print(f"{self.season} harvest")
        print(
            f"{self.name} rich with vitamine "
            f"{self.nutritional_value}"
        )


if __name__ == "__main__":
    print("=== Garden Plant Types ===\n")

    rose = Flower("Rose", 25, 30, "red")
    tulip = Flower("Tulip", 20, 15, "yellow")

    oak = Tree("Oak", 500, 1825, 50)
    pine = Tree("Pine", 600, 2000, 40)

    tomato = Vegetable("Tomato", 80, 90, "summer", "C")
    carrot = Vegetable("Carrot", 30, 70, "spring", "A")

    rose.get_info()
    rose.bloom()
    print()

    oak.get_info()
    oak.produce_shade()
    print()

    tomato.get_info()
