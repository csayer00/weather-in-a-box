# weather-in-a-box
It's what the title says. Press a button and it reads the weather to you out loud

## How it works
1) Arduino Nano gets weather data through an API and generates text to be said aboit the weather and uses config file to determine if it should read celsius or fahr and such when the user clicks the button.
2) Arduino aends plain text data as commands to the TTS chip to generate the TTS, communicating with UART.
3) TTS chip sends audio yranscription of weather to the audio amplifier
4) Audio amplifier sends sound to the speaker, reading the weather outloud

## Timeline
Sunday, June 7th, 2026: Boards ordered and set to arrive on Monday, June 8th, 2026
Monday, June 8th, 2026: Stuff arrived almost 12 HOURS LATE??? On the Amazon pagr it said overnight! It arrived at 6:00! Got familliar with Arduino softeare and the board itself and connected to internet amd made some small sample MicroPython examples