"""Program to help plan a cozy tea party."""

__author__: str = "730574267"


def main_planner(guests: int) -> None:
    """Calls each function and produces printed output."""
    print("A Cozy Tea Party for " + str(guests) + " People!")
    print("Tea Bags: " + str(tea_bags(people=guests)))
    print("Treats: " + str(treats(people=guests)))
    print(
        "Cost: $"
        + str(
            cost(tea_count=tea_bags(people=guests), treat_count=treats(people=guests))
        )
    )
    return None


def tea_bags(people: int) -> int:
    """Compute the number of tea bags needed based on number of guests."""
    return people * 2


def treats(people: int) -> int:
    """Compute the number of treats needed based on the number of teas."""
    return int(tea_bags(people=people) * 1.5)


def cost(tea_count: int, treat_count: int) -> float:
    """Compute the cost of the tea bags and the treats combined."""
    return tea_count * 0.5 + treat_count * 0.75


if __name__ == "__main__":
    main_planner(guests=int(input("How many guests are attending your tea party? ")))
