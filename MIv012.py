import minimalmodbus


"""

#Relé kapcsolás
instrument = minimalmodbus.Instrument('COM3', 255) #(PORT(COM3 vagy COM4 átalában), address)
instrument.serial.baudrate = 9600
modbus = instrument.write_bit(0, 1) #(relé száma(0-3), 0-ki 1-be)
print (modbus)s

#Relé cím adás
instrument = minimalmodbus.Instrument('COM3', 0)#(PORT(COM3 vagy COM4 átalában), ide valamiért nulla kell nem tom miért)
instrument.serial.baudrate = 9600
instrument.mode = minimalmodbus.MODE_RTU 
address = instrument.write_register(registeraddress=0,value=32, number_of_decimals=0,functioncode=16,signed=True)#(value= address szám (1-255))
print(address)

#Eszköz Cím lekérdezés
instrument = minimalmodbus.Instrument('COM3', 0, debug=True)#(PORT(COM3 vagy COM4 átalában), ide valamiért nulla kell nem tom miért)
instrument.serial.baudrate = 9600
instrument.mode = minimalmodbus.MODE_RTU 
address = instrument.read_register(registeraddress=0,number_of_decimals=0, functioncode=3, signed=True)
print(address)

#Relé állapot lekérdezés 
instrument = minimalmodbus.Instrument('COM3', 10)#(PORT(COM3 vagy COM4 átalában), address)
instrument.serial.baudrate = 9600
instrument.mode = minimalmodbus.MODE_RTU 
address = instrument.read_bits(registeraddress=0,number_of_bits=8,functioncode=1)
print(address)

#Bemenet jelszintje
instrument = minimalmodbus.Instrument('COM3', 10)#(PORT(COM3 vagy COM4 átalában), address)
instrument.serial.baudrate = 9600
instrument.mode = minimalmodbus.MODE_RTU 
address = instrument.read_bits(registeraddress=0,number_of_bits=8,functioncode=2)
print(address)

"""