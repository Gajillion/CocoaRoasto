class TempSensor:
    tempSensorId    = ''
    tempSensorName  = ''
    myTempSensor    = None

    def __init__(self, tempSensorId, tempSensorName, driver, spi, clk='', cs='', do=''):
        self.tempSensorId = tempSensorId
        self.tempSensorName = tempSensorName

        tempDriver = __import__(driver)
        myDriver = getattr(tempDriver,driver)

        if spi == "hardware":
            import Adafruit_GPIO.SPI as SPI

            # Raspberry Pi hardware SPI configuration.
            SPI_PORT   = 0
            SPI_DEVICE = 0
            self.myTempSensor = myDriver(spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))
        elif spi == "gpio":
            self.myTempSensor = myDriver(int(tempSensor.find('clk').text), \
                                            int(tempSensor.find('cs').text), \
                                            int(tempSensor.find('do').text))
        else:
            print "ABORT!!!"

        print("Constructing %s sensor %s"%(driver,tempSensorId))
