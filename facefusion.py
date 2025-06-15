#!/usr/bin/env python3

import os

# Set optimal threading environment variables
os.environ['KMP_DUPLICATE_LIB_OK'] = 'TRUE'  # Avoid library conflicts
os.environ['OMP_NUM_THREADS'] = '2'           # OpenMP threads
os.environ['ONNX_NUM_THREADS'] = '2'          # ONNX Runtime threads

from facefusion import core

if __name__ == '__main__':
	core.cli()
