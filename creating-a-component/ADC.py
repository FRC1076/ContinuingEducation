import smbus
import time
class Adc:
    """
    Usage:
            adc = Adc()

            value = adc.recvADC(PORT_NUM)

     where PORT_NUM is the port number of the ADC that is
     doing the measurement.

     Notice that the Adc class wraps the smbus class.   This can
     act as another example of wrapping another class with a higher
     layer of service.
    """
    def __init__(self):
        #
        # Get I2C bus  (smbus interface is mostly compatible with I2C bus
        # See:   https://www.electronicshub.org/basics-i2c-communication/
        # Note: I2C is a standard that is used for *tons* of chips, so a
        # microcontroller can "talk" to all of those chips using
        # the smbus interface.
        self.bus = smbus.SMBus(1)
        
        # I2C address of the device
        self.ADDRESS            = 0x48
        
        # PCF8591 Command
        # See the data sheet for this chip at:
        #     https://www.nxp.com/docs/en/data-sheet/PCF8591.pdf
        # Notice this chip can also work in reverse.
        # It can convert digital to analog signals
        # that is why there is a write method. (see below)
        #
        self.PCF8591_CMD                        =0x40  #Command
        
        # ADS7830 Command
        # See the data sheet for this chip at:
        #     https://www.ti.com/product/ADS7830
        self.ADS7830_CMD                        = 0x84 # Single-Ended Inputs

        """
        Note that the Freenove was built using two different
        models of ADC chip.    This check determines which chip
        is being used and remembers the name so that appropriate
        variation of the access to the ADC can be used.
        """
        for i in range(3):
            aa=self.bus.read_byte_data(self.ADDRESS,0xf4)
            if aa < 150:
                self.Index="PCF8591"
            else:
                self.Index="ADS7830" 
    def analogReadPCF8591(self,chn):#PCF8591 read ADC value,chn:0,1,2,3
        """
        Read 9 values in quick succession.
        Sort the results and return the median.
        This helps smooth out the readings, eliminating glitches (noise).
        """
        value=[0,0,0,0,0,0,0,0,0]
        for i in range(9):
            value[i] = self.bus.read_byte_data(self.ADDRESS,self.PCF8591_CMD+chn)
        value=sorted(value)
        return value[4]   
        
    def analogWritePCF8591(self,value):#PCF8591 write DAC value
        """
        If the smbus sends a Write command, the chip will generate a
        an analog voltage of the specified value.  (This is referred
        as a DAC (Digital To Analog) conversion. 
        """
        self.bus.write_byte_data(self.ADDRESS,cmd,value)
        
    def recvPCF8591(self,channel):#PCF8591 write DAC value
        """
        Read until two successive values are equal.   This will miss
        any short spikes, and maybe remove some noise.
        """
        while(1):
            value1 = self.analogReadPCF8591(channel)   #read the ADC value of channel 0,1,2,
            value2 = self.analogReadPCF8591(channel)
            if value1==value2:
                break;
        voltage = value1 / 255.0 * 3.3  # scale from 0-255 to 0-3.3
        voltage = round(voltage,2)      # keep 2 decimal places
        return voltage
    def recvADS7830(self,channel):
        """Select the Command data from the given provided value above"""
        COMMAND_SET = self.ADS7830_CMD | ((((channel<<2)|(channel>>1))&0x07)<<4)
        self.bus.write_byte(self.ADDRESS,COMMAND_SET)
        while(1):
            value1 = self.bus.read_byte(self.ADDRESS)
            value2 = self.bus.read_byte(self.ADDRESS)
            if value1==value2:
                break;
        """
        The ADC actually returns an 8 bit number (0-255).
        This code scales it to a value between 0 and 3.3   (the voltage)
        """
        voltage = value1 / 255.0 * 3.3  #calculate the voltage value
        voltage = round(voltage,2)
        return voltage
        
    def recvADC(self,channel):
        """
        Depending on which chip is on this board, read voltage value from specified
        port (channel) of the ADC chip and return it.
        """
        if self.Index=="PCF8591":
            data=self.recvPCF8591(channel)
        elif self.Index=="ADS7830":
            data=self.recvADS7830(channel)
        return data
    # This function is not used in the test code (and there is no
    # matching open statement for the sbus (i2c bus))   There maybe
    # should be, especially if there are more than one leader device
    # on the i2c bus.  (things get too complicated at that point)
    def i2cClose(self):
        self.bus.close()

def loop():
    adc=Adc()
    while True:
        Left_IDR=adc.recvADC(0)
        print (Left_IDR)
        Right_IDR=adc.recvADC(1)
        print (Right_IDR)
        Power=adc.recvADC(2)*3
        print (Power)
        Left_FLUX=adc.recvADC(3)
        print (Left_FLUX)
        Right_FLUX=adc.recvADC(4)
        time.sleep(1)
        print ('----')
def destroy():
    pass
# Main program logic follows:
if __name__ == '__main__':
    print ('Program is starting ... ')
    try:
        loop()
    except KeyboardInterrupt:  # When 'Ctrl+C' is pressed, the child program destroy() will be  executed.
        destroy()
