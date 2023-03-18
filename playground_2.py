from typing import Union, Sequence
from functools import lru_cache


def stairway_path(stairway: Sequence[Union[float, int]]) -> Union[float, int]:
    """
    Рассчитайте минимальную стоимость подъема на верхнюю ступень,
    если мальчик умеет наступать на следующую ступень и перешагивать через одну.

    :param stairway: список целых чисел, где каждое целое число является стоимостью конкретной ступени
    :return: минимальная стоимость подъема на верхнюю ступень
    """
    def lazy_stair(stairs):
        if stairs == 0 or stairs == 1:
            return stairway[stairs]
        return stairway[stairs] + min(lazy_stair(stairs-1),lazy_stair(stairs-2))
    return lazy_stair(len(stairway)-1)


if __name__ == '__main__':
    print(stairway_path((1, 3, 1, 5)))  # 7
