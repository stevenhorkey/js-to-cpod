import time
import pyxid2

scanner = pyxid2.XIDDeviceScanner.GetDeviceScanner()

print "Detecting XID devices, stand by..."
scanner.DetectXIDDevices()

devCount = scanner.DeviceCount()
if (devCount == 0):
    print "No devices found."
    quit()

devCon = scanner.DeviceConnectionAtIndex(0)
print devCon.GetCombinedInfo()

devCon.SetPulseDuration(100)
linesBitmask = 1
# for bm in xrange (0, 8):
devCon.RaiseLines(linesBitmask)
linesBitmask = linesBitmask << 1
time.sleep(.5)

devCon.ClearLines()