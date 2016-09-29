import numpy as np

def smashPlot(movie_in, plot_out, start_time = 0, end_time = np.inf, interval = 1):

	# ex [1,3] if players 1 and 3
	player_nums = detectPlayers(movie_in)
	
	# digit_image_dict = dictionary with keys
	#  ['p1d1','p1d2','p1d3','p2d1',... etc] for every present player
	#  p# is player number, d# is digit number of damage meter
	#  Values are ndarrays with dimensions num_timepts x num_pixels_per_digit_image
	digit_image_dict = getDamageImgs(movie_in, player_nums)
	
	# damage_values_dict = dictionary with keys
	#  ['p1','p2',...] for every present player
	#  Values are ndarray vectors containing damage values at each time point
	damage_values_dict = classifyDigits(digit_image_dict)
	
	plotDamage(damage_values_dict, plot_out)
 
     #Gittest