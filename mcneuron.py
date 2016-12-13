# this is a simple McNeuron program which only caculates on formula yin = x1w1 + x2w2
# realated theory is in the directory. this is just a practice we are not going to use McNeuron for project
import numpy as np
weightAndInputs = np.array([[0.2,0.3],[0.6,0.7]]) # 0th index index is input and 1st index is its associated weight
bias = 0.45
yin = 0
for x in weightAndInputs:
    yin = yin + x[0]*x[1]
yin = yin + bias
print("yin = %.2f" % yin)
