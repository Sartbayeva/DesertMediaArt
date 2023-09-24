import time
import board
import neopixel

# Initialize the onboard RGB LED
led = neopixel.NeoPixel(board.NEOPIXEL, 1)
led.brightness = 0.1  # Set brightness to a low value

# Define the colors for the breathing effect
colors = [(0, 0, 255), (0, 0, 0)]  # Blue (on) and Off (off)

# Define the duration of each phase in seconds
fade_in_duration = 2
pause_duration = 2
fade_out_duration = 2

while True:
    # Fade in
    for brightness in range(0, 256, 16):  # 0 to 255 with step 16
        led[0] = (
            (colors[0][0] * brightness) // 255,  # Adjust red component
            (colors[0][1] * brightness) // 255,  # Adjust green component
            (colors[0][2] * brightness) // 255,  # Adjust blue component
        )
        time.sleep(fade_in_duration / 16)  # Control the transition speed

    # Pause at full brightness
    led[0] = colors[0]
    time.sleep(pause_duration)  # Pause at full brightness

    # Fade out
    for brightness in range(255, -1, -16):  # 255 to 0 with step -16
        led[0] = (
            (colors[0][0] * brightness) // 255,  # Adjust red component
            (colors[0][1] * brightness) // 255,  # Adjust green component
            (colors[0][2] * brightness) // 255,  # Adjust blue component
        )
        time.sleep(fade_out_duration / 16)  # Control the transition speed

    # Pause at off state
    led[0] = colors[1]
    time.sleep(pause_duration)  # Pause at off state
