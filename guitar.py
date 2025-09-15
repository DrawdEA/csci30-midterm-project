#!/usr/bin/env python3

from guitarstring import GuitarString
from stdaudio import play_sample
import stdkeys

if __name__ == '__main__':
    # initialize window
    stdkeys.create_window()

    PLAY_DURATION = 44100 * 2 # sampling rate/second * 2 seconds to play each note

    keyboard = "q2we4r5ty7u8i9op-[=]"
    strings = []
    active_strings = []

    for i in range(len(keyboard)):
        frequency = 440 * (1.059463**(i - 12))
        strings.append(GuitarString(frequency))

    n_iters = 0
    while True:
        # it turns out that the bottleneck is in polling for key events
        # for every iteration, so we'll do it less often, say every
        # 1000 or so iterations
        if n_iters == 1000:
            stdkeys.poll()
            n_iters = 0
        n_iters += 1

        # check if the user has typed a key; if so, process it
        if stdkeys.has_next_key_typed():
            key = stdkeys.next_key_typed()
            if key in keyboard:
                index = keyboard.index(key)
                strings[index].pluck()

                if strings[index] not in active_strings:
                    active_strings.append(strings[index])


        # compute the superposition of samples
        sample = 0.0
        for string in active_strings:
            sample += string.sample()

        # play the sample on standard audio
        play_sample(sample)

        # advance the simulation of each guitar string by one step
        # this utilizes a temporary active strings list to avoid modifying the list while iterating over it
        temp_active = []
        for string in active_strings:
            string.tick()
            if string.time() <= PLAY_DURATION:
                temp_active.append(string)
        active_strings = temp_active
