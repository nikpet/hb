from datetime import date


def friday_years(start, end):
    fridays = 0
    for year in range(start, end):
        if date(year,1,1).weekday() == 3 or date(year,12,31).weekday() == 3:
            fridays += 1
    return fridays


if __name__ == '__main__':
    print(friday_years(1000, 2000))
    print(friday_years(1753, 2000))
    print(friday_years(1990, 2015))
