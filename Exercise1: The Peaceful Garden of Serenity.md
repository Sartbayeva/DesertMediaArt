# The Peaceful Garden of Serenity

Imagine you're in this tranquil garden where the leaves sway gently in the breeze. Soft blue lights twinkle among the greenery, creating a soothing, almost otherworldly atmosphere. It's as if the garden itself is radiating positive energy, wrapping you in a cozy cocoon of calmness… 
![](https://github.com/Sartbayeva/DesertMediaArt/blob/main/IMG_9350.JPG)

### Concept / Intention for the Work:

In this mini-project called “The Peaceful Garden of Serenity”, I bring together nature, soft blue LED lights, and the magic of meditation for a relaxing experience. A blue LED animation designed to emulate the calming and rhythmic sensation of deep breathing. The gentle transition between blue light and darkness represents the ebb and flow of a peaceful breath. The intention is to create a soothing and meditative ambience, encouraging relaxation and mindfulness. 

It's like the garden's own heartbeat, syncing with your inner calm. This simple visual effect serves as a reminder to take a moment for tranquillity and self-reflection.

### Code Snippet - The Breathing Animation:

#fade in
for brightness in range(0, 256, 16):  #0 to 255 with step 16
    led[0] = (
        (colors[0][0] * brightness) // 255,
        (colors[0][1] * brightness) // 255,
        (colors[0][2] * brightness) // 255,
    )
    time.sleep(fade_in_duration / 16)

The code snippet above is responsible for the "fade in" phase of the breathing animation. It gradually increases the brightness of the LED from off to full blue. Here's how it works: the for loop iterates through values of brightness from 0 to 255 in increments of 16. These values represent the gradual increase in LED brightness. Within each iteration, the LED color is set using the RGB values from the colors list. The values are adjusted according to the current brightness level to smoothly transition from off (0, 0, 0) to full blue (0, 0, 255). The time.sleep function controls the duration of each step, ensuring a smooth and timed transition.

### Reflection:

I'm submitting this work a bit later than planned due to a bit of a tech hiccup. You know how sometimes things just don't work the way you expect them to? Well, that's what happened.

I was excited to start my project, but when I tried to find the bootloader on my laptop, it was nowhere to be found. I tried everything I could think of - resetting the feather M4 express board, reloading it, reinstalling files, and even restarting my laptop. But no luck.

That's when I decided to ask Professor Michael for help. Together, we tried all sorts of things. First, we thought maybe it was a problem with the board itself, so we tested it on his board, and it worked perfectly. Next, we turned our attention to the adapter, and guess what? It was working too! After a few more twists and turns, we found out that the cable I was using was the problem all along. It had decided to go on vacation or something hahah. That's why I couldn't update the featherboot. Once the cable issue was fixed, I started learning about CircuitPython and the Mu editor. That part was not difficult!

I believe this exercise achieved its goal of creating a calming and meditative atmosphere. The simplicity of the LED animation is elegant in its representation of breath, making it a valuable tool for relaxation and mindfulness practices. 

#### Ways to further develop this work include:

I would like to integrate THE SPEAKER. Specifically, combine the LED animation with ambient sounds or soothing music to create a more immersive meditative environment.

### Demo Video:

![](https://github.com/Sartbayeva/DesertMediaArt/blob/main/IMG_9353%20(1).mov)
