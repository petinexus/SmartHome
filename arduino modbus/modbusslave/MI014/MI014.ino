#include <ModbusSlave.h>

Modbus slave(15, 8); // [stream = Serial,] slave id = 1, rs485 control-pin = 8

void setup() {

    slave.cbVector[CB_WRITE_COILS] = writeDigitalOut;

    Serial.begin(9600);
    slave.begin(9600);
}

void loop() {

    slave.poll();
}

uint8_t writeDigitalOut(uint8_t fc, uint16_t address, uint16_t length) {
    if (slave.readCoilFromBuffer(0) == HIGH)
    {
        digitalWrite(address, HIGH);
    }
    else
    {
        digitalWrite(address, LOW);
    }
    return STATUS_OK;
}
