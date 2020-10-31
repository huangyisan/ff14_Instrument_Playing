from key_mapping import *
import time
# 4/4

base_time = 1.4

quarter_time = 0.25 / base_time
half_time = 0.5 / base_time
half_quarter_time = 0.75 / base_time
one_time = 1 / base_time
one_half_time = 1.5 / base_time
one_half_quarter_time = 1.75 / base_time
two_time = 2 / base_time
two_half_time = 2.5 / base_time
three_time = 3 / base_time
four_time = 4 / base_time

if __name__ == '__main__':
    time.sleep(2)

    # Line 1
    Pause(half_time)
    Bass_So(half_time)
    Bass_La(half_time)
    Normal_Do(half_time)

    #
    Normal_Re(two_time)
    Normal_Mi(half_time)
    Normal_Re(quarter_time)
    Normal_Mi(quarter_time)
    Normal_Do(one_half_time)
    Bass_La(quarter_time)
    #
    Normal_Mi(two_time)
    Pause(half_time)
    Bass_So(half_time)
    Bass_La(half_time)
    Normal_Do(half_time)
    #
    Normal_Re(two_time)
    Normal_Mi(half_time)
    Normal_Re(quarter_time)
    Normal_Mi(quarter_time)
    Normal_Do(one_half_time)
    Normal_So(two_time)
    # Line 2
    # Normal_So(one_half_time)
    Normal_Mi(one_time)
    Pause(one_time)
    Bass_So(half_time)
    Bass_La(quarter_time)
    Normal_Do(quarter_time)
    #
    Normal_Re(two_time)
    Normal_Mi(half_time)
    Normal_Re(quarter_time)
    Normal_Mi(quarter_time)
    Normal_Do(one_half_time)
    Bass_La(quarter_time)
    #
    Normal_Mi(two_time)
    Pause(half_time)
    Bass_So(half_time)
    Bass_La(half_time)
    Normal_Do(half_time)
    #
    Normal_Re(two_time)
    Normal_Mi(half_time)
    Normal_Re(quarter_time)
    Normal_Mi(quarter_time)
    Normal_Do(one_time)
    # Line 3
    Bass_La(two_time)
    Pause(one_time)
    Normal_So(one_time)
    #
    Normal_La(three_time)
    Normal_So(half_time)
    Normal_La(quarter_time)
    Normal_So(one_half_quarter_time)
    #
    Normal_Mi(one_time)
    Pause(half_time)
    Normal_So(one_time)
    #
    Normal_La(quarter_time)
    Normal_So(quarter_time)
    Normal_La(two_half_time)
    Normal_So(half_time)
    Normal_La(quarter_time)
    Normal_So(one_half_quarter_time)
    #
    Normal_Mi(one_time)
    Pause(half_time)
    Normal_Do(half_time)
    Normal_Mi(half_time)
    #
    Normal_Re(quarter_time)
    Normal_Do(quarter_time)
    Normal_Re(two_half_time)
    Normal_Do(half_quarter_time)
    Bass_La(quarter_time)
    #
    Normal_Mi(two_time)
    Pause(half_time)
    Normal_Do(half_time)
    Normal_Mi(half_time)
    #
    Normal_Re(quarter_time)
    Normal_Do(quarter_time)
    Normal_Re(two_time)
    Normal_Mi(half_time)
    Normal_Re(quarter_time)
    Normal_Mi(quarter_time)
    Normal_Do(one_time)
    # Line 5
    Bass_La(four_time)










