"""Testing program."""

__author__: str = "730574267"

from exercises.ex03.dictionary import invert
import pytest
from exercises.ex03.dictionary import count
from exercises.ex03.dictionary import favorite_color
from exercises.ex03.dictionary import bin_len


def test_invert_use_1() -> None:
    """Test the invert function."""
    assert invert({"bird": "sparrow", "dog": "poodle", "snake": "python"}) == {
        "sparrow": "bird",
        "poodle": "dog",
        "python": "snake",
    }


def test_invert_use_2() -> None:
    """Test the invert function."""
    assert invert({"book": "mystery", "documentary": "movie", "music": "jazz"}) == {
        "mystery": "book",
        "movie": "documentary",
        "jazz": "music",
    }


def test_invert_edge() -> None:
    """Test the invert function."""
    with pytest.raises(KeyError):
        invert({"biology": "science", "calculus": "math", "statistics": "math"})


def test_count_use_1() -> None:
    """Test the count function."""
    assert count(["genome", "carroll", "phillips", "genome", "phillips"]) == {
        "genome": 2,
        "carroll": 1,
        "phillips": 2,
    }


def test_count_use_2() -> None:
    """Test the count function."""
    assert count(["apples", "apples", "milk", "milk", "bananas", "bread"]) == {
        "apples": 2,
        "milk": 2,
        "bananas": 1,
        "bread": 1,
    }


def test_count_edge() -> None:
    """Test the count function."""
    assert count([]) == {}


def test_favorite_color_use1() -> None:
    """Test the favorite color function."""
    assert (
        favorite_color(
            {
                "julie": "blue",
                "andrew": "green",
                "martha": "purple",
                "peter": "orange",
                "samuel": "green",
            }
        )
        == "green"
    )


def test_favorite_color_use2() -> None:
    """Test the favorite color function."""
    assert (
        favorite_color(
            {"james": "red", "erica": "pink", "carson": "red", "tabitha": "blue"}
        )
        == "red"
    )


def test_favorite_color_edge() -> None:
    """Test the favorite color function."""
    assert (
        favorite_color(
            {"cindy": "yellow", "leslie": "red", "david": "black", "stacy": "pink"}
        )
        == "yellow"
    )


def test_bin_len_use1() -> None:
    """Test the bin len function."""
    assert bin_len(["more", "plenty", "good"]) == {4: {"more", "good"}, 6: {"plenty"}}


def test_bin_len_use2() -> None:
    """Test the bin len function."""
    assert bin_len(["ball", "shoe", "floor", "basket"]) == {
        4: {"ball", "shoe"},
        5: {"floor"},
        6: {"basket"},
    }


def test_bin_len_edge() -> None:
    """Test the bin len function."""
    assert bin_len([]) == {}
