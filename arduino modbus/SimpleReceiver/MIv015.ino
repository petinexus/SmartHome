#define DECODE_NEC 1

#include <IRremote.h>

#if defined(__AVR_ATtiny25__) || defined(__AVR_ATtiny45__) || defined(__AVR_ATtiny85__) || defined(__AVR_ATtiny87__) || defined(__AVR_ATtiny167__)

#  if defined(ARDUINO_AVR_DIGISPARKPRO)
#define IR_RECEIVE_PIN    9
#  else
#define IR_RECEIVE_PIN    0
#  endif
#  if defined(ARDUINO_AVR_DIGISPARK)
#define LED_BUILTIN PB1
#  endif
#elif defined(ESP32)
int IR_RECEIVE_PIN = 15;
#elif defined(ARDUINO_AVR_PROMICRO)
int IR_RECEIVE_PIN = 10;
#else
int IR_RECEIVE_PIN = 11;
#endif

void setup() {
    Serial.begin(9600);

    Serial.println(F("START " __FILE__ " from " __DATE__ "\r\nUsing library version " VERSION_IRREMOTE));

    IrReceiver.begin(IR_RECEIVE_PIN, ENABLE_LED_FEEDBACK, USE_DEFAULT_FEEDBACK_LED_PIN);

    Serial.print(F("Ready to receive IR signals at pin "));
    Serial.println(IR_RECEIVE_PIN);
}

void loop() {

    if (IrReceiver.decode()) {

        IrReceiver.printIRResultShort(&Serial);
        if (IrReceiver.decodedIRData.protocol == UNKNOWN) {

            IrReceiver.printIRResultRawFormatted(&Serial, true);
        }
        Serial.println();

        IrReceiver.resume(); 

        if (IrReceiver.decodedIRData.command == 0x10) {

        } else if (IrReceiver.decodedIRData.command == 0x11) {
        }
    }
}
