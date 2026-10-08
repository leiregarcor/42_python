#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_harvest_total.py                                  :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: leigarci <leigarci@student.42urduliz.com>    +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: Invalid date        by                     #+#    #+#            #
#   Updated: 2026/10/08 20:43:32 by leigarci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_harvest_total():
    harvest1 = int(input("Day 1 harvest: "))
    harvest2 = int(input("Day 2 harvest: "))
    harvest3 = int(input("Day 3 harvest: "))
    print(f"Total harvest: {harvest1 + harvest2 + harvest3}")
