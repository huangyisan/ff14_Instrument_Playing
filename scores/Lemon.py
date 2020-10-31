from key_mapping import *
import time
# 4/4

base_time = 4.7

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
    def repeat():
        # Line 1
        Pause(one_time)
        Pause(one_time)
        Pause(one_time)
        Treble_Do(half_time)
        Treble_Re(half_time)
        #
        Treble_Mi(one_time)
        Treble_Do(half_time)
        Normal_La(one_half_time)
        Treble_Re(one_time)
        #
        Normal_Si(one_time)
        Normal_So(half_time)
        Normal_Mi(one_half_time)
        Normal_Si(one_time)
        #
        Normal_La(one_time)
        Normal_So(half_time)
        Normal_Do(one_half_time)
        Normal_So(one_time)
        #
        Normal_Mi(three_time)
        Normal_Re(half_time)
        Normal_Mi(half_time)

        # Line 2
        Normal_Fa(two_time)
        Treble_Do(one_time)
        Normal_Si(one_time)
        Treble_Do(half_time)
        #
        Normal_So(two_time)
        Normal_Fa(one_time)
        Normal_Mi(half_quarter_time)
        Normal_Fa(quarter_time)
        #
        Normal_Fa_s(two_time)
        Treble_Do(one_time)
        Normal_Si(one_time)
        Normal_La(half_time)
        Normal_So_s(three_time)
        Treble_Do(half_time)
        Treble_Re(half_time)
        #
        Treble_Mi(one_time)
        Treble_Do(half_time)
        Normal_La(one_half_time)
        Treble_Re(one_time)

        # Line 3
        Normal_Si(one_time)
        Normal_So(half_time)
        Normal_Mi(one_half_time)
        Normal_Si(one_time)
        #
        Normal_La(one_time)
        Normal_So(half_time)
        Normal_Do(one_half_time)
        Normal_So(one_time)
        #
        Normal_Mi(three_time)
        Normal_Re(half_time)
        Normal_Mi(half_time)
        #
        Normal_Fa(two_time)
        Normal_So(one_time)
        Normal_Fa(one_time)
        Normal_So(half_time)
        #
        Normal_Mi(one_time)
        Normal_So(one_time)
        Treble_Do(one_time)
        Treble_Mi(one_time)
        #
        Treble_Re(half_time)
        Treble_Re(one_half_time)
        Treble_Re(half_time)
        Treble_Do(one_half_time)
        #
        Treble_Do(four_time)

    repeat()
    Pause(four_time)
    # repeat
    repeat()

    # Line 8
    Normal_La(one_half_time)
    Normal_Si(half_time)
    Treble_Do(one_time)
    Normal_Si(half_time)
    Normal_La(half_time)
    #
    Normal_So(one_time)
    Treble_Mi(one_time)
    Treble_Mi(two_time)
    #
    Treble_Re(one_half_time)
    Treble_Mi(half_time)
    Treble_Fa(one_time)
    Treble_Mi(half_time)
    Treble_Re(half_time)
    #
    Treble_Do(one_time)
    Treble_Re(one_time)
    Normal_So(two_time)











