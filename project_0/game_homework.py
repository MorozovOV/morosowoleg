"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    count = 0
    # Задаём интервал, внутри которого нужно выбрать число:
    beg = 1 # начало интервала
    end = 100 # конец интервала
    number = np.random.randint(beg, end + 1) # Даём команду выбрать случайное число из указанного интервала. Чтобы 100 вошло в интервал, пишем end + 1
    step = end / 2 # задаём шаг, который всегда в 2 раза меньше того интервала, в котором остаётся загаданное число
    predict_number = end / 2  # предполагаемое число
    import math
    while True:
        count += 1 # Включаем счётчик попыток
        if number > predict_number: # если угадываемое число больше нашего, то ...
            step = math.ceil(step / 2) # ... уменьшаем шаг в 2 раза с округлением в большую сторону ...
            predict_number += step  # ... и увеличиваем наш прогноз на текущий шаг
        if number < predict_number: # если угадываемое число меньше нашего, то ...
            step = math.ceil(step / 2) # ... уменьшаем шаг в 2 раза с округлением в большую сторону ...
            predict_number -= step # ... и уменьшаем наш прогноз на текущий шаг
        if number == predict_number:
            break  # выход из цикла, если угадали
    return count


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    count_ls = []
    #np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(1, 101, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за: {score} попыток")
    return score



if __name__ == "__main__":
    # RUN
    score_game(random_predict)