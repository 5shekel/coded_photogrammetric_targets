"""
Generate polygon of specific coded marker.

Original:
Matthew Petroff (2018) Photogrammetry Targets.
https://mpetroff.net/2018/05/photogrammetry-targets/

Python implementation by Claude
"""

import numpy as np
from matplotlib.path import Path
import matplotlib.patches as patches

def get_coded_marker_polygon(x_center: float, y_center: float, dot_radius: float, bits: int, code: int) -> patches.PathPatch:
    """
    Generates polygon of specific coded marker
    """
    n = 2000
    phi = np.linspace(0, 360, n)
    
    # Create the center circle
    circle_x = x_center + np.cos(np.deg2rad(phi)) * dot_radius
    circle_y = y_center + np.sin(np.deg2rad(phi)) * dot_radius
    
    # Start with the center circle vertices and codes
    vertices = np.column_stack((circle_x, circle_y))
    codes = np.full(n, Path.LINETO)
    codes[0] = Path.MOVETO
    codes[-1] = Path.CLOSEPOLY

    # Add the bit segments
    for i in range(bits):
        if (1 << (bits - 1 - i)) & code:
            segment_phi = -np.linspace(360 / bits * i, 360 / bits * (i + 1), n)
            
            # Inner arc
            x_1 = x_center + np.cos(np.deg2rad(segment_phi)) * dot_radius * 2.0
            y_1 = y_center + np.sin(np.deg2rad(segment_phi)) * dot_radius * 2.0
            
            # Outer arc
            x_2 = x_center + np.cos(np.deg2rad(segment_phi)) * dot_radius * 3.0
            y_2 = y_center + np.sin(np.deg2rad(segment_phi)) * dot_radius * 3.0
            
            # Combine the arcs in the correct order
            segment_vertices = np.column_stack((
                np.concatenate([x_1, x_2[::-1], [x_1[0]]]),
                np.concatenate([y_1, y_2[::-1], [y_1[0]]])
            ))
            
            # Add codes for the new segment
            segment_codes = np.full(len(segment_vertices), Path.LINETO)
            segment_codes[0] = Path.MOVETO
            segment_codes[-1] = Path.CLOSEPOLY
            
            # Append the new segment
            vertices = np.vstack((vertices, segment_vertices))
            codes = np.concatenate((codes, segment_codes))

    # Create the path and return a patch
    path = Path(vertices, codes)
    return patches.PathPatch(path, facecolor='black', edgecolor='black') 