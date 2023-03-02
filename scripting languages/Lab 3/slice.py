#!/usr/bin/env python3

## name_of_variable[starting_index:last_index+1]

a = "Batman"
##slicing
print(a[0:2])
print(a[:-1]) ##cuts off the last letter ->Batma
print(a[1:-1]) ##cuts off the first and last letter -> atma
print(a[-5:-1]) ## does the same thing -> atma

## step sizing
print(a[::2]) ## will give every second letter -> Bta
print(a[::1]) ## will give the whole string > Batman
print(a[::-1]) ## will reverse the whole string
