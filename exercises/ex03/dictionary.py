"""Program to practice dictionary functions."""

__author__: str = "730574267"


def invert(d: dict[str, str]) -> dict[str, str]:
    """Function to invert the keys and values in a dictionary."""
    empty: dict[str, str] = {}

    for keys in d:
        if d[keys] in empty:
            raise KeyError("Duplicate keys.")
        empty[d[keys]] = keys
    return empty


def count(values: list[str]) -> dict[str, int]:
    """Function to count the number of times a value appears in an input list."""
    result: dict[str, int] = {}

    for inputs in values:
        if inputs in result:
            result[inputs] += 1
        else:
            result[inputs] = 1
    return result


def favorite_color(favorites: dict[str, str]) -> str:
    """Function that finds the most frequent color in a dictionary."""
    color_count: dict[str, int] = {}

    for keys in favorites:
        if favorites[keys] in color_count:
            color_count[favorites[keys]] += 1
        else:
            color_count[favorites[keys]] = 1
    highest: int = 0
    output: str = ""
    for keys in color_count:
        if color_count[keys] > highest:
            output = keys
            highest = color_count[keys]
    return output


def bin_len(words: list[str]) -> dict[int, set[str]]:
    """Function that "bins" a list of strings into a dictionary."""
    bins: dict[int, set[str]] = {}

    for word in words:
        length = len(word)
        if length not in bins:
            bins[length] = set()
        bins[length].add(word)

    return bins
