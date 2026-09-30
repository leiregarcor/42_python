#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_water_reminder.py                                 :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: leigarci <leigarci@student.42urduliz.com>    +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: Invalid date        by                     #+#    #+#            #
#   Updated: 2026/09/28 17:36:53 by leigarci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def	ft_water_reminder():
	days = int(input("Days since last watering: "))
	if (days > 2):
		print("Water the plants!")
	else:
		print("Plant are fine")
