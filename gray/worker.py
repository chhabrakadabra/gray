from pyarrow import plasma

from constants import PLASMA_SOCKET_LOCATION

def connect_to_plasma():
    return plasma.connect(PLASMA_SOCKET_LOCATION)

def init():
    print('Worker initializing...')
    plasma_client = connect_to_plasma()
