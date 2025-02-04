Coded Photogrammetric Targets
=============================

Circular coded targets are frequently used in close-range photogrammetry, as these targets can be recognised fully automatically. Based on the code written by [Matthew Petroff](https://mpetroff.net/2018/05/photogrammetry-targets/), 
this repository contains both Python and MATLAB implementations of the target generation code. The script generates the ring codes of the targets using the coding scheme described in the expired German 
patent [DE19733466A1](https://patents.google.com/patent/DE19733466A1/). 

Python Implementation
-------------------
The Python implementation is in the root directory.

### Installation
1. Clone this repository
2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

### Usage
Run the example script to generate sample targets:
```bash
python example.py
```

This will display a grid of coded targets with different bit patterns.

The main functions are:
- `get_ring_codes(bits, transitions)`: Generate codes for a given number of bits
- `get_coded_marker_polygon(x_center, y_center, dot_radius, bits, code)`: Generate a specific coded marker

MATLAB Implementation
------------------
The MATLAB implementation is located in the `matlab` directory. To use it, run `example.m` in MATLAB.

Example Output
-------------
![8 bit Circular Coded Photogrammetric Targets](/coded_marker.png?raw=true "Photogrammetric Coded Targets")
