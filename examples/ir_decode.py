import board
import pulseio
import neopixel
import adafruit_irremote

pulsein = pulseio.PulseIn(board.GP27, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()


def read_command():
    """Try to read an IR command. If none seen or if error, return None."""
    try:
        pulses = decoder.read_pulses(pulsein, blocking=False)
        if pulses:
            code = decoder.decode_bits(pulses)
            if len(code) > 3:
                print("Decoded:", code)
                return code[2]
        # if code is less than or equal to 3 characters long or no pulses received
        return None
    except adafruit_irremote.IRNECRepeatException:  # unusual short code!
        print("NEC repeat!")
        return CMD_REPEAT
    except adafruit_irremote.IRDecodeException as e:  # failed to decode
        print("Failed to decode:", e)
        return None
    except MemoryError as e:
        print("Memory error: ", e)
        return None

def  handle_command(command):
    print("Command", command)

def main():
    last_command = None
    command = read_command()
    if command is not None:
        if command == CMD_REPEAT:
            command = last_command
        last_command = command
        handle_command(command)


while True:
    main()
