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
         

print("=== Garden Plant Registry ===")
plant = Plant("Rose",25,30);
plant.get_info()
Days = 7
for i in range(Days - 1):
    plant.grow_age()
    plant.grow()

print(f"=== Day {Days} ===")
plant.get_info()
print(f"Growth this week: +{Days - 1}cm")
