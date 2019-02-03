# https://stackoverflow.com/questions/51804365/why-is-fft-different-in-swift-than-in-python
import numpy as np

frames = np.array( [ 1.0, 2.0, 3.0, 4.0 ] )
fftArray = np.fft.fft( frames, len( frames ) )

print( fftArray )
