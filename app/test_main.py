from app.main import get_human_age


def test_should_return_zero_for_zero_ages() -> None:
    assert get_human_age(0, 0) == [0, 0]


def test_should_not_give_human_year_before_first_15_years() -> None:
    assert get_human_age(14, 14) == [0, 0]


def test_should_give_one_human_year_at_15_years() -> None:
    assert get_human_age(15, 15) == [1, 1]


def test_should_not_increase_human_age_during_second_stage_until_completed() -> None:
    assert get_human_age(23, 23) == [1, 1]


def test_should_give_two_human_years_after_24_years() -> None:
    assert get_human_age(24, 24) == [2, 2]


def test_should_not_increase_during_extra_years_before_full_cycle() -> None:
    assert get_human_age(27, 27) == [2, 2]


def test_should_handle_different_cat_and_dog_conversion_rates() -> None:
    assert get_human_age(28, 28) == [3, 2]


def test_should_correctly_convert_large_ages() -> None:
    assert get_human_age(100, 100) == [21, 17]
