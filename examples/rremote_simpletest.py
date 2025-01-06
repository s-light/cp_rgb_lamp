# SPDX-FileCopyrightText: 2021 ladyada for Adafruit Industries
# SPDX-License-Identifier: MIT
# source: https://docs.circuitpython.org/projects/irremote/en/latest/examples.html

import pulseio
import board
import adafruit_irremote


pulsein = pulseio.PulseIn(board.GP27, maxlen=120, idle_state=True)
decoder = adafruit_irremote.GenericDecode()


while True:
    pulses = decoder.read_pulses(pulsein)
    print("Heard", len(pulses), "Pulses:", pulses)

    try:
        code = decoder.decode_bits(pulses)
        print("Decoded:", code)
    except adafruit_irremote.IRNECRepeatException:  # unusual short code!
        print("NEC repeat!")
    except (
        adafruit_irremote.IRDecodeException,
        adafruit_irremote.FailedToDecode,
    ) as e:  # failed to decode
        print("Failed to decode: ", e.args)

    print("----------------------------")
