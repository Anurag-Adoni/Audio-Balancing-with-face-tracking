from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import time 

# code to test audio balance control 
# Get default audio device using PyCAW
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
print(devices)
# Get current volume of the left channel
currentVolumeLeft = volume.GetChannelVolumeLevel(0)

'''volume.SetChannelVolumeLevel(1, currentVolumeLeft - 6.0, None)'''





