#!/usr/bin/env python3
# ########################################################################### #
#   shebang: 1                                                                #
#                                                          :::      ::::::::  #
#   ft_plot_area.py                                      :+:      :+:    :+:  #
#                                                      +:+ +:+         +:+    #
#   By: leigarci <leigarci@student.42urduliz.com>    +#+  +:+       +#+       #
#                                                  +#+#+#+#+#+   +#+          #
#   Created: Invalid date        by                     #+#    #+#            #
#   Updated: 2026/09/14 16:54:25 by leigarci           ###   ########.fr      #
#                                                                             #
# ########################################################################### #

def ft_plot_area():
	length = int(input("Enter length: "))
	width = int(input("Enter width: "))
	area = length * width
	print(f"Plot area: {area}")