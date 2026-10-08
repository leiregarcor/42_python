#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_seed_inventory.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: leigarci <leigarci@student.42urduliz.com>    +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: Invalid date        by                     #+#    #+#            #
#   Updated: 2026/10/08 20:45:22 by leigarci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
    type_cap = seed_type.capitalize()
    if (unit == "packets"):
        print(f"{type_cap} seeds: {quantity} {unit} available")
    elif (unit == "grams"):
        print(f"{type_cap} seeds: {quantity} {unit} total")
    elif (unit == "area"):
        print(f"{type_cap} seeds: covers {quantity} square meters")
    else:
        print("Unknown unit type")
