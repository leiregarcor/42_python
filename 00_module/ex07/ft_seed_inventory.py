#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_seed_inventory.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: leigarci <leigarci@student.42urduliz.com>    +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: Invalid date        by                     #+#    #+#            #
#   Updated: 2026/10/04 16:32:59 by leigarci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_seed_inventory(seed_type: str, quantity: int, unit: str) -> None:
	if (unit == "packets"):
		print(f"{seed_type.capitalize()} seeds: {quantity} {unit} available")
	elif (unit == "grams"):
		print(f"{seed_type.capitalize()} seeds: {quantity} {unit} total")
	elif (unit == "area"):
		print(f"{seed_type.capitalize()} seeds: covers {quantity} square meters")
	else:
		print("Unknown unit type")
	
	
