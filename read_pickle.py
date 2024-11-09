# read the pickle files as follows

import pickle

# no bubble curve (both x and y axis)
noB= pickle.load(open("nobubble.pickle","rb"))

# curves with bubble (fig4, z=12)
# x axis (frequency /MHz)
bubble12x_v7=pickle.load(open("bubble12x_rv1.pickle", "rb"))
# y axis (intensity)
bubble12y_v7=pickle.load(open("bubble12y_rv1.pickle", "rb"))


# curves with bubble (fig5, z=8)
# x axis (frequency /MHz)
bubble8x_v7=pickle.load(open("bubble8x_rv1.pickle", "rb"))
# y axis (intensity)
bubble8y_v7=pickle.load(open("bubble8y_rv1.pickle", "rb"))


