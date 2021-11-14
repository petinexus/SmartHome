import minimalmodbus
instrument = minimalmodbus.Instrument('COM3', 15, debug=True) #(PORT(COM3 vagy COM4 átalában), address)
instrument.serial.baudrate = 9600
modbus = instrument.write_bit(3, 0) #(relé száma(0-3), 0-ki 1-be)
print (modbus)