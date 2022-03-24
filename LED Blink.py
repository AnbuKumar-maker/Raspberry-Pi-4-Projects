import time
from grove.grove_ryb_led_button import GroveLedButton
 
def main():
    ledbtn = GroveLedButton(5)
 
    while True:
        ledbtn.led.light(True)
        time.sleep(1)
 
        ledbtn.led.light(False)
        time.sleep(1)
 
if __name__ == '__main__':
    main()
