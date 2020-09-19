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
                s = self.ser.read(3).decode()  # Читаем только 3 байта
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
            except KeyboardInterrupt:  # Делаем исключение на всякий случай
                # для корректного завершения работы порта
                print("Stopped connection with ttyS0 port")
                return False

    def _read(self, channel):
        while True:
            self.ser.flushInput()  # Очистка буфера
            self.ser.write(pack('B', channel))
            time.sleep(.005)  # Задержка перед считыванием данных, чтобы не получить мусор
            if self.ser.inWaiting():  # Проверка на наличие входных данных в буфере
                rawdata = self.ser.read(4)  # Читаем ровно 4 байта, потому что нужен float
                data, = unpack('f', rawdata)  # Декодировка, unpack возврящает tuple (data, )
                if data != data:  # Проверка на NaN
                    continue
                else:
                    break
        return data

    def map(self, x, in_min, in_max, out_min, out_max):
        return ((x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min)

    # Возвращает ЭМГ
    def emg(self, channel):
        e = self._read(channel)
        # print("eeeee ==", e)
        if self.BOTTOM_THR_EMG < e < self.TOP_THR_EMG:
            return e
        else:
            return self.BOTTOM_THR_EMG
