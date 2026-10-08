#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_count_harvest_iterative.py                        :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: leigarci <leigarci@student.42urduliz.com>    +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: Invalid date        by                     #+#    #+#            #
#   Updated: 2026/10/08 20:40:47 by leigarci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_count_harvest_iterative():
    days = int(input("Days until harvest: "))
    for i in range(1, (days + 1)):
        print("Day " + str(i))
    print("Harvest time!")
