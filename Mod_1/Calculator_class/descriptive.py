#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Sep  4 14:25:52 2019

@author: swilson5
"""
import math


class Calculator:
    def __init__(self, data):
        self.data = sorted(data)
        # self.length = self._calc_length()
        self.mean = self._calc_mean(data)
        self.median = self._calc_med(data)
        self.variance = self._calc_var(data)
        self.stand_dev = self._calc_stand_dev(data)


    def add_data(self, data):
        self.data.extend(new_data)


    def remove_data(self, new_data):
        for number in new_data:
            if number in self.data:
                self.data.remove(number)


    def _calc_mean(self, data):
        #declare variable vfor sum, then length, then divide

        add = (sum(self.data))
        return add / len(self.data)




    def _calc_med(self, data):
        if len(self.data)%2 == 0:
            mid_left = self.data[len(self.data) // 2 -1]
            mid_right = self.data[len(self.data) // 2 ]
            avg = (mid_left + mid_right) / 2
        else:
            avg = self.data[len(self.data) // 2]
        return avg



    def _calc_var(self, data):
        indices = list(range(len(self.data)))
        alpha = sum([((self.data[index]) - self.mean) ** 2 for index in indices])
        return alpha / (len(self.data) - 1)



#standard deviation function
    def _calc_stand_dev(self, data):
        return _calc_var(self) ** .5



# Your class should have the following methods:
#
# .add_data() - which can take in  a list of values and extend the .data attribute
# .remove_data() accept a list of numbers and remove any of the numbers in that list from your object data
