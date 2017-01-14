import converters
import math
import random
import sys

def random_real(a, b):
    """
    Random real between a and b inclusively.
    """
    return a + random.random() * (b - a)

def branch_length(depth):
    """
    Somewhat random length of the branch.  Play around
    with this to achieve a desired tree structure.
    """
    return  math.log(depth) * random_real(.5, 1)

def branch_angle(initial_lean, max_lean):
    """
    Somewhat random angle of the branch.  Play around
    with this to achieve a desired tree structure.
    """
    return initial_lean + max_lean * random_real(-.5, .5)

def branches(x0, y0, depth, nfurcation, max_lean, initial_lean):
    """
    Make a tree!
    """
    # maximum depth achieved, stop adding branches
    # maybe add a fruit or flower here
    if not depth:
        return []
    angle = branch_angle(initial_lean, max_lean)
    length = branch_length(depth)
    # branch is the line segment (x0, y0) - (x1, y0)
    x1 = x0 + length*math.sin(angle)
    y1 = y0 + length*math.cos(angle)
    # construct the branch
    # the depth -- or inverse height -- is stored so that the 
    # rendering code can use it to vary the thickness of the
    # branches, color, etc.
    new_branches = [[depth, [[x0, y0], [x1, y1]]]]
    # number of branches
    n = random.randint(1, nfurcation)
    # branches growing out of this branch
    for _ in xrange(n):
        # angle of the current branch becomes the initial lean
        new_branches.extend(
            branches(x1, y1, depth-1, nfurcation, max_lean, angle)
            )
    return new_branches

def main():
    tree = branches(
        # origin
        0, 0,
        # 11 branches from trunk to crown
        11,
        # at each juncture, there's either 1 or 2 branches
        2,
        # the branch can deviate 90/2=45 degrees in either direction
        math.pi/2,
        # initial lean [bias] is zero degrees
        0
        )
    print(converters.to_mathematica(tree))

if __name__ == '__main__':
    main()
