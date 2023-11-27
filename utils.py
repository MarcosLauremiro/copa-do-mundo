from exceptions import ImpossibleTitlesError, InvalidYearCupError, NegativeTitlesError


def data_processing(dicionario):
    if dicionario["titles"] < 0:
        raise NegativeTitlesError("titles cannot be negative")
    fist_cup = int(dicionario["first_cup"][:4])
    if fist_cup < 1930 or (fist_cup - 1930) % 4 != 0:
        raise InvalidYearCupError("there was no world cup this year")
    num_cups = (2022 - fist_cup) // 4 + 1
    if dicionario["titles"] > num_cups:
        raise ImpossibleTitlesError("impossible to have more titles than disputed cups")
