"""
Code converter module for trees.py
"""

def _mathematica_line_segments(tree):
    """
    Produce Mathematica graphics object elements.
    """
    for branch in tree:
        [depth, [[x0, y0], [x1, y1]]] = branch
        yield '{{Thickness[{}/300.], Line[{{{{{},{}}},{{{},{}}}}}]}}'.format(
            depth, x0, y0, x1, y1
            )

def to_mathematica(tree):
    """
    Produce Mathematica code to draw the tree.
    """
    segments = [segment for segment in _mathematica_line_segments(tree)]
    code = 'tree = {{\n{}\n}};\n\nShow[Graphics[tree], AspectRatio -> 1, PlotRange -> All]\n'.format(
            ',\n'.join(segments)
            )
    return code
