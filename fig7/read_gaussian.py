
# dict keys are: ['8xnob', '8ynob', '8yb', '7xnob', '7ynob', '7yb', '6xnob', '6ynob', '6yb', '8yb-nob', '7yb-nob', '6yb-nob']
# x, y means x, y axis
# nob, means curves without bubble
# b, curves with bubble
# v6, v_turb=1e6 cm/s=10 km/s
# v7, v_turb=1e7 cm/s=100 km/s
# v8 case is redundant
gauss_file='fit_gauss_dict.pickle'
fit_gauss_dict = pickle.load(open(gauss_file, "rb"))



theo_file='theoretical_width.pickle'
theoretical_width = pickle.load(open(theo_file, "rb"))



