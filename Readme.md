# NRC_Project

repo to control the devellopment of the analog to didital interface module using  the KS0413 keyestudio ESP32 Core Board , [Board wiki](https://wiki.keyestudio.com/KS0413_keyestudio_ESP32_Core_Board) ,[PinOut references](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)

![](https://wiki.keyestudio.com/images/7/79/0413%E5%9B%BE%E7%89%872.png)
![](https://i0.wp.com/randomnerdtutorials.com/wp-content/uploads/2018/08/esp32-pinout-chip-ESP-WROOM-32.png?w=1401&quality=100&strip=all&ssl=1)

 ## Basic Concepts

 Python3 will be used to interact with the board on which a simple program in C/C++  that will mimic dummy analog data that would be generated by a real attophysics experiment, the data will then be processed and presented in a particular selected format.
 The ESP32 microcontroller program will be uploaded using plarformio 

 ## Description of the Experiment
High Harmonic Generation will be observed using 3 photodiodes.
The first  one will record the incoming laser impulse energy, the second will measure the beam diverted by the beam splitter.

## Demo Output

![](https://github.com/Driss-001/NRC_Attoscience_Software/blob/main/NRC_PROJ/Figure_1.png?raw=true)

