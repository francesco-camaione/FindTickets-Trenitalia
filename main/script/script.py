from main.model.day import Day
from main.model.train import Train
from main.service.train_service import GetTrains
from main.utils import utils
import time

start = time.time()

date_input1 = "01/01/2022"
treni = GetTrains(date_input1).availables_trains()  # -> list


def calendar_bestprices(response_list):

    day1_list = []
    for train in response_list[0]:
        if train["saleable"]:
            trains = Train(**train)
            train_day1 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day1_list.append(train_day1)
    day1_list.sort()

    day2_list = []
    for train in response_list[1]:
        if train["saleable"]:
            trains = Train(**train)
            train_day2 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day2_list.append(train_day2)
    day2_list.sort()

    day3_list = []
    for train in response_list[2]:
        if train["saleable"]:
            trains = Train(**train)
            train_day3 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day3_list.append(train_day3)
    day3_list.sort()

    day4_list = []
    for train in response_list[3]:
        if train["saleable"]:
            trains = Train(**train)
            train_day4 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day4_list.append(train_day4)
    day4_list.sort()

    day5_list = []
    for train in response_list[4]:
        if train["saleable"]:
            trains = Train(**train)
            train_day5 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day5_list.append(train_day5)
    day5_list.sort()

    day6_list = []
    for train in response_list[5]:
        if train["saleable"]:
            trains = Train(**train)
            train_day6 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day6_list.append(train_day6)
    day6_list.sort()

    day7_list = []
    for train in response_list[6]:
        if train["saleable"]:
            trains = Train(**train)
            train_day7 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day7_list.append(train_day7)
    day7_list.sort()

    day8_list = []
    for train in response_list[7]:
        if train["saleable"]:
            trains = Train(**train)
            train_day8 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day8_list.append(train_day8)
    day8_list.sort()

    day9_list = []
    for train in response_list[8]:
        if train["saleable"]:
            trains = Train(**train)
            train_day9 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                             trains.duration)
            day9_list.append(train_day9)
    day9_list.sort()

    day10_list = []
    for train in response_list[9]:
        if train["saleable"]:
            trains = Train(**train)
            train_day10 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day10_list.append(train_day10)
    day10_list.sort()

    day11_list = []
    for train in response_list[10]:
        if train["saleable"]:
            trains = Train(**train)
            train_day11 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day11_list.append(train_day11)
    day11_list.sort()

    day12_list = []
    for train in response_list[11]:
        if train["saleable"]:
            trains = Train(**train)
            train_day12 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day12_list.append(train_day12)
    day12_list.sort()

    day13_list = []
    for train in response_list[12]:
        if train["saleable"]:
            trains = Train(**train)
            train_day13 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day13_list.append(train_day13)
    day13_list.sort()

    day14_list = []
    for train in response_list[13]:
        if train["saleable"]:
            trains = Train(**train)
            train_day14 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day14_list.append(train_day14)
    day14_list.sort()

    day15_list = []
    for train in response_list[14]:
        if train["saleable"]:
            trains = Train(**train)
            train_day15 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day15_list.append(train_day15)
    day15_list.sort()

    day16_list = []
    for train in response_list[15]:
        if train["saleable"]:
            trains = Train(**train)
            train_day16 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day16_list.append(train_day16)
    day16_list.sort()

    day17_list = []
    for train in response_list[16]:
        if train["saleable"]:
            trains = Train(**train)
            train_day17 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day17_list.append(train_day17)
    day17_list.sort()

    day18_list = []
    for train in response_list[17]:
        if train["saleable"]:
            trains = Train(**train)
            train_day18 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day18_list.append(train_day18)
    day18_list.sort()

    day19_list = []
    for train in response_list[18]:
        if train["saleable"]:
            trains = Train(**train)
            train_day19 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day19_list.append(train_day19)
    day19_list.sort()

    day20_list = []
    for train in response_list[19]:
        if train["saleable"]:
            trains = Train(**train)
            train_day20 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day20_list.append(train_day20)
    day20_list.sort()

    day21_list = []
    for train in response_list[20]:
        if train["saleable"]:
            trains = Train(**train)
            train_day21 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day21_list.append(train_day21)
    day21_list.sort()

    day22_list = []
    for train in response_list[21]:
        if train["saleable"]:
            trains = Train(**train)
            train_day22 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day22_list.append(train_day22)
    day22_list.sort()

    day23_list = []
    for train in response_list[22]:
        if train["saleable"]:
            trains = Train(**train)
            train_day23 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day23_list.append(train_day23)
    day23_list.sort()

    day24_list = []
    for train in response_list[23]:
        if train["saleable"]:
            trains = Train(**train)
            train_day24 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day24_list.append(train_day24)
    day24_list.sort()

    day25_list = []
    for train in response_list[24]:
        if train["saleable"]:
            trains = Train(**train)
            train_day25 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day25_list.append(train_day25)
    day25_list.sort()

    day26_list = []
    for train in response_list[25]:
        if train["saleable"]:
            trains = Train(**train)
            train_day26 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day26_list.append(train_day26)
    day26_list.sort()

    day27_list = []
    for train in response_list[26]:
        if train["saleable"]:
            trains = Train(**train)
            train_day27 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day27_list.append(train_day27)
    day27_list.sort()

    day28_list = []
    for train in response_list[27]:
        if train["saleable"]:
            trains = Train(**train)
            train_day28 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day28_list.append(train_day28)
    day28_list.sort()

    day29_list = []
    for train in response_list[28]:
        if train["saleable"]:
            trains = Train(**train)
            train_day29 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day29_list.append(train_day29)
    day29_list.sort()

    day30_list = []
    for train in response_list[29]:
        if train["saleable"]:
            trains = Train(**train)
            train_day30 = Day(utils.get_date(trains.departuretime), trains.originalPrice, trains.trainlist,
                              trains.duration)
            day30_list.append(train_day30)
    day30_list.sort()

    calendar_list = [day1_list[0], day2_list[0], day3_list[0], day4_list[0], day5_list[0], day6_list[0], day7_list[0],
                     day8_list[0], day9_list[0], day10_list[0], day11_list[0], day12_list[0], day13_list[0],
                     day14_list[0], day15_list[0], day16_list[0], day17_list[0], day18_list[0], day19_list[0],
                     day20_list[0], day21_list[0], day22_list[0], day23_list[0], day24_list[0], day25_list[0],
                     day26_list[0], day27_list[0], day28_list[0], day29_list[0], day30_list[0],]
    return calendar_list


prezzi = calendar_bestprices(treni)
print(prezzi)

end = time.time()
print(end-start)
