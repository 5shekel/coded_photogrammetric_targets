"""
Example script to generate coded photogrammetric targets.

Original:
Matthew Petroff (2018) Photogrammetry Targets.
https://mpetroff.net/2018/05/photogrammetry-targets/

Python implementation by Claude
"""

import numpy as np
import matplotlib.pyplot as plt
from ring_codes import get_ring_codes
from coded_marker import get_coded_marker_polygon

def main():
    # Parameters
    dot_radius = 1
    bits = 8
    codes = get_ring_codes(bits)
    columns = 4
    rows = int(np.ceil(len(codes) / columns))

    # Create figure
    fig, axs = plt.subplots(rows, columns, figsize=(12, 3*rows))
    fig.suptitle(f'Coded Markers ({bits} bit)')
    
    # Make axs 2D if it's 1D
    if rows == 1:
        axs = np.array([axs])
    if columns == 1:
        axs = axs.reshape(-1, 1)

    # Generate each marker
    for i in range(rows):
        for j in range(columns):
            num = columns * i + j
            ax = axs[i, j]
            
            if num < len(codes):
                code = codes[num]
                marker = get_coded_marker_polygon(0, 0, dot_radius, bits, code)
                ax.add_patch(marker)
                
                # Add marker number
                ax.text(3.5*dot_radius, 3.5*dot_radius, str(num+1),
                       horizontalalignment='right',
                       verticalalignment='top',
                       color='black')

            # Set axis properties
            ax.set_xlim([-4, 4])
            ax.set_ylim([-4, 4])
            ax.set_xticks([])
            ax.set_yticks([])
            ax.set_aspect('equal')
            ax.spines['top'].set_visible(True)
            ax.spines['right'].set_visible(True)
            ax.spines['bottom'].set_visible(True)
            ax.spines['left'].set_visible(True)

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    main() 