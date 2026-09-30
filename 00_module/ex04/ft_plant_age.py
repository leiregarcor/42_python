#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plant_age.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: leigarci <leigarci@student.42urduliz.com>    +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: Invalid date        by                     #+#    #+#            #
#   Updated: 2026/09/28 17:33:54 by leigarci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def	ft_plant_age():
	days = int(input("Enter plant age in days: "))
	if (days > 60):
		print("Plant is ready to harvest!")
	else:
		print("Plant needs more time to grow.")
	