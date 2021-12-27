import service.trains_of_day_x
from model.day import Day
from model.train import Train
from service.train_service import availabl_trains
from utils import utils


def calendar_bestprices(response_list) -> dict:

    day1_list = []
    for train in response_list[0]:
        if train["saleable"]:
            trains = Train(**train)
            train_day1 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day1_list.append(train_day1)
            day1_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day1 = Day(00, 999, [], '00')
            day1_list.append(train_day1)
    if len(day1_list) == 0:
        train_day1 = Day(00, 999, [], '00')
        day1_list.append(train_day1)

    day2_list = []
    for train in response_list[1]:
        if train["saleable"]:
            trains = Train(**train)
            train_day2 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day2_list.append(train_day2)
            day2_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day2 = Day(00, 999, [], '00')
            day2_list.append(train_day2)
    if len(day2_list) == 0:
        train_day2 = Day(00, 999, [], '00')
        day2_list.append(train_day2)

    day3_list = []
    for train in response_list[2]:
        if train["saleable"]:
            trains = Train(**train)
            train_day3 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day3_list.append(train_day3)
            day3_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day3 = Day(00, 999, [], '00')
            day3_list.append(train_day3)
    if len(day3_list) == 0:
        train_day3 = Day(00, 999, [], '00')
        day3_list.append(train_day3)

    day4_list = []
    for train in response_list[3]:
        if train["saleable"]:
            trains = Train(**train)
            train_day4 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day4_list.append(train_day4)
            day4_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day4 = Day(00, 999, [], '00')
            day4_list.append(train_day4)
    if len(day4_list) == 0:
        train_day4 = Day(00, 999, [], '00')
        day4_list.append(train_day4)

    day5_list = []
    for train in response_list[4]:
        if train["saleable"]:
            trains = Train(**train)
            train_day5 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day5_list.append(train_day5)
            day5_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day5 = Day(00, 999, [], '00')
            day5_list.append(train_day5)
    if len(day5_list) == 0:
        train_day5 = Day(00, 999, [], '00')
        day5_list.append(train_day5)

    day6_list = []
    for train in response_list[5]:
        if train["saleable"]:
            trains = Train(**train)
            train_day6 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day6_list.append(train_day6)
            day6_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day6 = Day(00, 999, [], '00')
            day6_list.append(train_day6)
    if len(day6_list) == 0:
        train_day6 = Day(00, 999, [], '00')
        day6_list.append(train_day6)

    day7_list = []
    for train in response_list[6]:
        if train["saleable"]:
            trains = Train(**train)
            train_day7 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day7_list.append(train_day7)
            day7_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day7 = Day(00, 999, [], '00')
            day7_list.append(train_day7)
    if len(day7_list) == 0:
        train_day7 = Day(00, 999, [], '00')
        day7_list.append(train_day7)

    day8_list = []
    for train in response_list[7]:
        if train["saleable"]:
            trains = Train(**train)
            train_day8 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day8_list.append(train_day8)
            day8_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day8 = Day(00, 999, [], '00')
            day8_list.append(train_day8)
    if len(day8_list) == 0:
        train_day8 = Day(00, 999, [], '00')
        day8_list.append(train_day8)

    day9_list = []
    for train in response_list[8]:
        if train["saleable"]:
            trains = Train(**train)
            train_day9 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day9_list.append(train_day9)
            day9_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day9 = Day(00, 999, [], '00')
            day9_list.append(train_day9)
    if len(day9_list) == 0:
        train_day9 = Day(00, 999, [], '00')
        day9_list.append(train_day9)

    day10_list = []
    for train in response_list[9]:
        if train["saleable"]:
            trains = Train(**train)
            train_day10 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day10_list.append(train_day10)
            day10_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day10 = Day(00, 999, [], '00')
            day10_list.append(train_day10)
    if len(day10_list) == 0:
        train_day10 = Day(00, 999, [], '00')
        day10_list.append(train_day10)

    day11_list = []
    for train in response_list[10]:
        if train["saleable"]:
            trains = Train(**train)
            train_day11 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day11_list.append(train_day11)
            day11_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day11 = Day(00, 999, [], '00')
            day11_list.append(train_day11)
    if len(day11_list) == 0:
        train_day11 = Day(00, 999, [], '00')
        day11_list.append(train_day11)

    day12_list = []
    for train in response_list[11]:
        if train["saleable"]:
            trains = Train(**train)
            train_day12 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day12_list.append(train_day12)
            day12_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day12 = Day(00, 999, [], '00')
            day12_list.append(train_day12)
    if len(day12_list) == 0:
        train_day12 = Day(00, 999, [], '00')
        day12_list.append(train_day12)

    day13_list = []
    for train in response_list[12]:
        if train["saleable"]:
            trains = Train(**train)
            train_day13 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day13_list.append(train_day13)
            day13_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day13 = Day(00, 999, [], '00')
            day13_list.append(train_day13)
    if len(day13_list) == 0:
        train_day13 = Day(00, 999, [], '00')
        day13_list.append(train_day13)

    day14_list = []
    for train in response_list[13]:
        if train["saleable"]:
            trains = Train(**train)
            train_day14 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day14_list.append(train_day14)
            day14_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day14 = Day(00, 999, [], '00')
            day14_list.append(train_day14)
    if len(day14_list) == 0:
        train_day14 = Day(00, 999, [], '00')
        day14_list.append(train_day14)

    day15_list = []
    for train in response_list[14]:
        if train["saleable"]:
            trains = Train(**train)
            train_day15 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day15_list.append(train_day15)
            day15_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day15 = Day(00, 999, [], '00')
            day15_list.append(train_day15)
    if len(day15_list) == 0:
        train_day15 = Day(00, 999, [], '00')
        day15_list.append(train_day15)

    day16_list = []
    for train in response_list[15]:
        if train["saleable"]:
            trains = Train(**train)
            train_day16 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day16_list.append(train_day16)
            day16_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day16 = Day(00, 999, [], '00')
            day16_list.append(train_day16)
    if len(day16_list) == 0:
        train_day16 = Day(00, 999, [], '00')
        day16_list.append(train_day16)

    day17_list = []
    for train in response_list[16]:
        if train["saleable"]:
            trains = Train(**train)
            train_day17 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day17_list.append(train_day17)
            day17_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day17 = Day(00, 999, [], '00')
            day17_list.append(train_day17)
    if len(day17_list) == 0:
        train_day17 = Day(00, 999, [], '00')
        day17_list.append(train_day17)

    day18_list = []
    for train in response_list[17]:
        if train["saleable"]:
            trains = Train(**train)
            train_day18 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day18_list.append(train_day18)
            day18_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day18 = Day(00, 999, [], '00')
            day18_list.append(train_day18)
    if len(day18_list) == 0:
        train_day18 = Day(00, 999, [], '00')
        day18_list.append(train_day18)

    day19_list = []
    for train in response_list[18]:
        if train["saleable"]:
            trains = Train(**train)
            train_day19 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day19_list.append(train_day19)
            day19_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day19 = Day(00, 999, [], '00')
            day19_list.append(train_day19)
    if len(day19_list) == 0:
        train_day19 = Day(00, 999, [], '00')
        day19_list.append(train_day19)

    day20_list = []
    for train in response_list[19]:
        if train["saleable"]:
            trains = Train(**train)
            train_day20 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day20_list.append(train_day20)
            day20_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day20 = Day(00, 999, [], '00')
            day20_list.append(train_day20)
    if len(day20_list) == 0:
        train_day20 = Day(00, 999, [], '00')
        day20_list.append(train_day20)

    day21_list = []
    for train in response_list[20]:
        if train["saleable"]:
            trains = Train(**train)
            train_day21 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day21_list.append(train_day21)
            day21_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day21 = Day(00, 999, [], '00')
            day21_list.append(train_day21)
    if len(day21_list) == 0:
        train_day21 = Day(00, 999, [], '00')
        day21_list.append(train_day21)

    day22_list = []
    for train in response_list[21]:
        if train["saleable"]:
            trains = Train(**train)
            train_day22 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day22_list.append(train_day22)
            day22_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day22 = Day(00, 999, [], '00')
            day22_list.append(train_day22)
    if len(day22_list) == 0:
        train_day22 = Day(00, 999, [], '00')
        day22_list.append(train_day22)

    day23_list = []
    for train in response_list[22]:
        if train["saleable"]:
            trains = Train(**train)
            train_day23 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day23_list.append(train_day23)
            day23_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day23 = Day(00, 999, [], '00')
            day23_list.append(train_day23)
    if len(day23_list) == 0:
        train_day23 = Day(00, 999, [], '00')
        day23_list.append(train_day23)

    day24_list = []
    for train in response_list[23]:
        if train["saleable"]:
            trains = Train(**train)
            train_day24 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day24_list.append(train_day24)
            day24_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day24 = Day(00, 999, [], '00')
            day24_list.append(train_day24)
    if len(day24_list) == 0:
        train_day24 = Day(00, 999, [], '00')
        day24_list.append(train_day24)

    day25_list = []
    for train in response_list[24]:
        if train["saleable"]:
            trains = Train(**train)
            train_day25 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day25_list.append(train_day25)
            day25_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day25 = Day(00, 999, [], '00')
            day25_list.append(train_day25)
    if len(day25_list) == 0:
        train_day25 = Day(00, 999, [], '00')
        day25_list.append(train_day25)

    day26_list = []
    for train in response_list[25]:
        if train["saleable"]:
            trains = Train(**train)
            train_day26 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day26_list.append(train_day26)
            day26_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day26 = Day(00, 999, [], '00')
            day26_list.append(train_day26)
    if len(day26_list) == 0:
        train_day26 = Day(00, 999, [], '00')
        day26_list.append(train_day26)

    day27_list = []
    for train in response_list[26]:
        if train["saleable"]:
            trains = Train(**train)
            train_day27 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day27_list.append(train_day27)
            day27_list.sort(key=lambda x: x.price)
        elif IndexError:
            train_day27 = Day(00, 999, [], '00')
            day27_list.append(train_day27)
    if len(day27_list) == 0:
        train_day27 = Day(00, 999, [], '00')
        day27_list.append(train_day27)

    day28_list = []
    if len(response_list[27]) > 1:
        for train in response_list[27]:
            if train["saleable"]:
                trains = Train(**train)
                train_day28 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                                  trains.duration)
                day28_list.append(train_day28)
                day28_list.sort(key=lambda x: x.price)
            else:
                train_day28 = Day(00, 999, [], '00')
                day28_list.append(train_day28)
    else:
        train_day28 = Day(00, 999, [], '00')
        day28_list.append(train_day28)

    day29_list = []
    if len(response_list[28]) > 1:
        for train in response_list[28]:
            if train["saleable"]:
                trains = Train(**train)
                train_day29 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
                day29_list.append(train_day29)
                day29_list.sort(key=lambda x: x.price)
            else:
                train_day29 = Day(00, 999, [], '00')
                day29_list.append(train_day29)
    else:
        train_day29 = Day(00, 999, [], '00')
        day29_list.append(train_day29)

    day30_list = []
    if len(response_list[29]) > 1:
        for train in response_list[29]:
            if train["saleable"]:
                trains = Train(**train)
                train_day30 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                                  trains.duration)
                day30_list.append(train_day30)
                day30_list.sort(key=lambda x: x.price)
            else:
                train_day30 = Day(00, 999, [], '00')
                day30_list.append(train_day30)
    else:
        train_day30 = Day(00, 999, [], '00')
        day30_list.append(train_day30)

    day31_list = []
    if len(response_list[30]) > 1:
        for train in response_list[30]:
            if train["saleable"]:
                trains = Train(**train)
                train_day31 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                                  trains.duration)
                day31_list.append(train_day31)
                day31_list.sort(key=lambda x: x.price)
            else:
                train_day31 = Day(00, 999, [], '00')
                day31_list.append(train_day31)
    else:
        train_day31 = Day(00, 999, [], '00')
        day31_list.append(train_day31)

    calendar_list = {
        "01": f"{day1_list[0].price}", "02": f"{day2_list[0].price}", "03": f"{day3_list[0].price}",
        "04": f"{day4_list[0].price}", "05": f"{day5_list[0].price}", "06": f"{day6_list[0].price}",
        "07": f"{day7_list[0].price}", "08": f"{day8_list[0].price}", "09": f"{day9_list[0].price}",
        "10": f"{day10_list[0].price}", "11": f"{day11_list[0].price}", "12": f"{day12_list[0].price}",
        "13": f"{day13_list[0].price}", "14": f"{day14_list[0].price}", "15": f"{day15_list[0].price}",
        "16": f"{day16_list[0].price}", "17": f"{day17_list[0].price}", "18": f"{day18_list[0].price}",
        "19": f"{day19_list[0].price}", "20": f"{day20_list[0].price}", "21": f"{day21_list[0].price}",
        "22": f"{day22_list[0].price}", "23": f"{day23_list[0].price}", "24": f"{day24_list[0].price}",
        "25": f"{day25_list[0].price}", "26": f"{day26_list[0].price}", "27": f"{day27_list[0].price}",
        "28": f"{day28_list[0].price}", "29": f"{day29_list[0].price}", "30": f"{day30_list[0].price}",
        "31": f"{day31_list[0].price}",
    }
    return calendar_list


origin = "Milano Centrale"
destination = "Giulianova"
date = f"01/01/2022"
n_adult = 1
n_baby = 0
