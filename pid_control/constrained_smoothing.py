# -------------
# User Instructions
#
# Now you will be incorporating fixed points into
# your smoother. 
#
# You will need to use the equations from gradient
# descent AND the new equations presented in the
# previous lecture to implement smoothing with
# fixed points.
#
# Your function should return the newpath that it
# calculates. 
#
# Feel free to use the provided solution_check function
# to test your code. You can find it at the bottom.
#


from copy import deepcopy
######################## ENTER CODE BELOW HERE #########################

def smooth(path, fix, weight_data = 0.0, weight_smooth = 0.1, tolerance = 0.00001):
    #
    # Enter code here. 
    # The weight for each of the two new equations should be 0.5 * weight_smooth
    #
    newpath = deepcopy(path)
    change = tolerance
    while change >= tolerance:
        for i in range(len(path)):
            for j in range(len(path[i])):
                if not fix[i]:
                    aux = newpath[i][j]
                    newpath[i][j] += weight_smooth * (newpath[(i-1)%len(path)][j] + newpath[(i+1)%len(path)][j] - \
                     2.0 * newpath[i][j]) + \
                     (weight_smooth / 2.0) * (2.0 * newpath[(i-1)%len(path)][j] - \
                     newpath[(i-2)%len(path)][j] - newpath[i][j]) + \
                     (weight_smooth / 2.0) * (2.0 * newpath[(i+1)%len(path)][j] - \
                     newpath[(i+2)%len(path)][j] - newpath[i][j])
                    change = abs(newpath[i][j] - aux)
                
    return newpath



