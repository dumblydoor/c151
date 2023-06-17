#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jun 17 16:57:55 2023

@author: aquilavijayanayagam
"""

month =("jan","feb"",mar","apr","may","jun","jul","aug","sep","oct","nov","dec")

profits =("10000","1000000","10000000","1000000000","100000000000","10000000000000","100000000000000","1000000000000","1000000000000000","10000000000000","10000000000","10000000000000000.1")

max_profits = max(profits)
max_profits_index=max_profits.index(max_profits)
print(max_profits_index)

max_profits_months = max(month)[max_profits_index]
print("the maximum profit was " + str(max_profits) + " it was recorded in " + str(max_profits_months))



min_profits = min(profits)
min_profits_index=min_profits.index(min_profits)
print(min_profits_index)

max_profits_months = max(month)[max_profits_index]
print("the minimum profit was " + str(min_profits) + " it was recorded in " + str(max_profits_months))




