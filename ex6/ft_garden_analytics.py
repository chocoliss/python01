class Plant:
    def __init__(self, name: str, height: int) -> None:
        self.name = name
        self.height = height

    def grow(self, amount: int) -> None:
        self.height += amount
        print(f"{self.name} grew {amount}cm")

    def get_info(self) -> None:
        print(f"- {self.name}: {self.height}cm")


class FloweringPlant(Plant):
    def __init__(
        self,
        name: str,
        height: int,
        flower_color: str
    ) -> None:
        super().__init__(name, height)
        self.flower_color = flower_color

    def get_info(self) -> None:
        print(
            f"- {self.name}: {self.height}cm, "
            f"{self.flower_color} flowers (blooming)"
        )


class PrizeFlower(FloweringPlant):
    def __init__(
        self,
        name: str,
        height: int,
        flower_color: str,
        prize_points: int
    ) -> None:
        super().__init__(name, height, flower_color)
        self.prize_points = prize_points

    def get_info(self) -> None:
        print(
            f"- {self.name}: {self.height}cm, "
            f"{self.flower_color} flowers (blooming), "
            f"Prize points: {self.prize_points}"
        )


class Garden:
    def __init__(self, owner: str) -> None:
        self.owner = owner
        self.plants = []
        self.total_growth = 0

    def add_plant(self, plant: Plant) -> None:
        print(f"Added {plant.name} to {self.owner}'s garden")
        self.plants.append(plant)

    def grow_all(self, amount: int) -> None:
        print(f"{self.owner} is helping all plants grow...")
        for plant in self.plants:
            plant.grow(amount)
            self.total_growth += amount

    def display_report(self) -> None:
        print(f"\n=== {self.owner}'s Garden Report ===")
        print("Plants in garden:")
        for plant in self.plants:
            plant.get_info()


class GardenManager:
    total_gardens = 0

    def __init__(self) -> None:
        self.gardens = []

    def create_garden(self, owner: str) -> Garden:
        garden = Garden(owner)
        self.gardens.append(garden)
        GardenManager.total_gardens += 1
        return garden

    class GardenStats:
        def __init__(self, garden: Garden) -> None:
            self.garden = garden

        def display_stats(self) -> None:
            plants = self.garden.plants

            regular = [
                p for p in plants
                if isinstance(p, Plant)
                and not isinstance(p, FloweringPlant)
            ]

            flowering = [
                p for p in plants
                if isinstance(p, FloweringPlant)
                and not isinstance(p, PrizeFlower)
            ]

            prize = [
                p for p in plants
                if isinstance(p, PrizeFlower)
            ]

            print(
                f"Plants added: {len(plants)}, "
                f"Total growth: {self.garden.total_growth}cm"
            )

            print(
                f"Plant types: {len(regular)} regular, "
                f"{len(flowering)} flowering, "
                f"{len(prize)} prize flowers"
            )

    @classmethod
    def create_garden_network(cls):
        return cls()

    @staticmethod
    def validate_height(height: int) -> bool:
        return height >= 0

    @staticmethod
    def calculate_score(garden: Garden) -> int:
        score = sum(p.height for p in garden.plants)
        for p in garden.plants:
            if isinstance(p, PrizeFlower):
                score += p.prize_points
        return score


if __name__ == "__main__":
    print("=== Garden Management System Demo ===")

    manager = GardenManager.create_garden_network()

    alice_garden = manager.create_garden("Alice")
    bob_garden = manager.create_garden("Bob")

    oak = GardenManager.create_regular_plant("Oak Tree", 100)
    rose = GardenManager.create_flowering_plant("Rose", 25, "red")
    sunflower = GardenManager.create_prize_flower(
        "Sunflower", 50, "yellow", 10
    )

    alice_garden.add_plant(oak)
    alice_garden.add_plant(rose)
    alice_garden.add_plant(sunflower)

    alice_garden.plants_growth(1)

    stats = GardenManager.GardenStats(len(alice_garden.plants), 0)
    stats.display_stats(alice_garden, 1)

    alice_garden.display_garden()

    print(
        "Height validation test:",
        GardenManager.validate_height(10)
    )

    bob_garden.add_plant(
        GardenManager.create_regular_plant("Carrot", 40)
    )
    bob_garden.add_plant(
        GardenManager.create_flowering_plant("Lily", 30, "white")
    )
    bob_garden.add_plant(
        GardenManager.create_prize_flower("Tulip", 20, "purple", 2)
    )

    alice_score = GardenManager.calculate_score(alice_garden)
    bob_score = GardenManager.calculate_score(bob_garden)

    print(f"Garden scores - Alice: {alice_score}, Bob: {bob_score}")
    print(f"Total gardens managed: {manager.total_gardens}")
