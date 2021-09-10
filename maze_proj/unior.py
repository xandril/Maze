import time
import serial
from struct import pack, unpack


class Unior:
    BOTTOM_THR_EMG = 0
    TOP_THR_EMG = 51000
    ser = serial.Serial('/dev/ttyS0', baudrate=57600, timeout=1.5)

    def __init(self):
        pass

    def handshake(self, channels):
        reply = str()
        number_of_channels = len(channels)
        while True:
            try:
                s = self.ser.read(3).decode()  # read 3 bytes
                print(s)
                if s == "OK\n":
                    for n in range(0, number_of_channels):
                        if n != 0:
                            reply += ";"
                        reply += str(channels[n])

                    reply += "\r"
                    print(reply)
                    self.ser.write(reply.encode())
                    return True
            except KeyboardInterrupt:  #
                print("Stopped connection with ttyS0 port")
                return False

    def _read(self, channel):
        while True:
            self.ser.flushInput()  # clear buffer
            self.ser.write(pack('B', channel))
            time.sleep(.005)  # defeat fucking garbage
            if self.ser.inWaiting():  # check buffer is not empty
                rawdata = self.ser.read(4)  # read 4 byte - float
                data, = unpack('f', rawdata)  # decode , unpack return tuple (data, )
                if data != data:  # check NaN
                    continue
                else:
                    break
        return data

    def map(self, x, in_min, in_max, out_min, out_max):
        return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

    # return emg
    def emg(self, channel):
        e = self._read(channel)
        if self.BOTTOM_THR_EMG < e < self.TOP_THR_EMG:
            return e
        else:
            return self.BOTTOM_THR_EMG
