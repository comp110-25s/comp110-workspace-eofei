"""File to define River class."""

from exercises.ex04.fish import Fish
from exercises.ex04.bear import Bear


class River:
    day: int
    bears: list[Bear]
    fish: list[Fish]

    def __init__(self, num_fish: int, num_bears: int):
        """New River with num_fish Fish and num_bears Bears"""
        self.day: int = 0
        self.fish: list[Fish] = []
        self.bears: list[Bear] = []
        # populate the river with fish and bears
        for _ in range(0, num_fish):
            self.fish.append(Fish())
        for _ in range(0, num_bears):
            self.bears.append(Bear())

    def check_ages(self):
        new_fish: list[Fish] = []
        for x in self.fish:
            if x.age <= 3:
                new_fish.append(x)
        self.fish = new_fish
        new_bears: list[Bear] = []
        for x in self.bears:
            if x.age <= 5:
                new_bears.append(x)
        self.bears = new_bears
        return None

    def bears_eating(self):
        for bear in self.bears:
            if len(self.fish) >= 5:
                self.remove_fish(3)
                bear.eat(3)
        return None

    def check_hunger(self):
        surviving_bears = []
        for bear in self.bears:
            if bear.hunger_score >= 0:
                surviving_bears.append(bear)
        self.bears = surviving_bears

        return None

    def repopulate_fish(self):
        num_new_fish = (len(self.fish) // 2) * 4
        count = 0
        while count < num_new_fish:
            self.fish.append(Fish())
            count += 1
        return None

    def repopulate_bears(self):
        num_new_bears = len(self.bears) // 2
        count = 0
        while count < num_new_bears:
            self.bears.append(Bear())
            count += 1
        return None

    def view_river(self):
        print(f"~~~ Day {self.day}: ~~~")
        print(f"Fish population: {len(self.fish)}")
        print(f"Bear population: {len(self.bears)}")
        return None

    def one_river_day(self):
        """Simulate one day of life in the river"""
        # Increase day by 1
        self.day += 1
        # Simulate one day for all Bears
        for bear in self.bears:
            bear.one_day()
            self.age += 1
        # Simulate one day for all Fish
        for fish in self.fish:
            fish.one_day()
            self.age += 1
        # Simulate Bear's eating
        self.bears_eating()
        # Remove hungry Bear's from River
        self.check_hunger()
        # Remove old Fish and Bear's from River
        self.check_ages()
        # Simulate Fish repopulation
        self.repopulate_fish()
        # Simulate Bear repopulation
        self.repopulate_bears()
        # Visualize River
        self.view_river()

    def one_river_week(self):
        for _ in range(7):
            self.one_river_day()

    def remove_fish(self, amount: int):
        self.fish = self.fish[amount:]
        return None
