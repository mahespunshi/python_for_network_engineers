#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 11:35:00 2023

@author: maheshkumar
"""

def parse_cdp_neighbors(command_output):
    connections = {}
    hostname = None

    for line in command_output:
        columns = line.split()

        if ">" in line:
            hostname = line.split(">")[0]

        elif len(columns) >= 5 and columns[3].isdigit():
            r_host, r_int, r_int_num, *others, l_int, l_int_num = columns

            connections[(hostname, l_int + l_int_num)] = (r_host, r_int + r_int_num)

    return connections

if __name__ == "__main__":
    with open('sh_cdp_n_sw1.txt') as f:
        read = f.readlines()
        result = parse_cdp_neighbors(read)
        print(result)
