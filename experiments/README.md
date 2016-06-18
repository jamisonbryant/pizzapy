# Experiments

This directory contains scripts that were written to test out an idea or write some
quick-and-dirty code to explore a concept. It's unlikely that any of these scripts
will be of any use to anyone other than me.

### Morse Coder
Contains functions for converting a given string to a series of dits and dahs (dots
and dashes) and outputting the series both to the computer's speakers and an Arduino's
LEDs if one is connected. The sound generation is done by turning a particular hardware
module on and off, so it will likely only work on OSes like mine (Ubuntu 16.04.3).

**Dependencies:**
 * pyserial (https://github.com/pyserial/pyserial)
