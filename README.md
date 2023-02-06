# ESP32 with joystick and LED matrix

![Cover photo](https://github.com/ejdam87/esp32led/blob/master/canvas.jpg)

This repository contains architecture based on:
- [ESP32 board](https://www.ebay.com/itm/174113523987?norover=1&mkevt=1&mkrid=711-167022-139639-2&mkcid=2&itemid=174113523987&targetid=1890534104577&device=c&mktype=pla&googleloc=9062583&poi=&campaignid=19170533672&mkgroupid=142899455734&rlsatarget=pla-1890534104577&abcId=9303996&merchantid=119648210&gclid=Cj0KCQiA54KfBhCKARIsAJzSrdoumUhoh9Bns0EqzDmkRxOYK0tZFFLQVGbdyU24g9pdGa_9BsLqWscaAlu3EALw_wcB) ( serves as processing unit )
- [joystick](https://www.banggood.com/JoyStick-Module-Shield-2_54mm-5-pin-Biaxial-Buttons-Rocker-for-PS2-Joystick-Game-Controller-Sensor-p-1566502.html?utm_source=googleshopping&utm_medium=cpc_organic&gmcCountry=SK&utm_content=minha&utm_campaign=aceng-pmax-sk-en-pc&currency=EUR&cur_warehouse=CN&createTmp=1&utm_source=googleshopping&utm_medium=cpc_eu&utm_content=dcr&utm_campaign=aceng-pmax-de-all-feed-test-220906&ad_id=&gclid=Cj0KCQiA54KfBhCKARIsAJzSrdqxJcrmT4jsG1kZSKjEyvS4Y7jUnto58v3P1GdZELFyhkm_j92MQVAaAnW3EALw_wcB) ( serves as input unit )
- [led matrix](https://www.ebay.com/itm/373724468139?norover=1&mkevt=1&mkrid=711-167022-139639-2&mkcid=2&itemid=373724468139&targetid=1890534104577&device=c&mktype=pla&googleloc=9062583&poi=&campaignid=19170533672&mkgroupid=142899455734&rlsatarget=pla-1890534104577&abcId=9303996&merchantid=661137743&gclid=Cj0KCQiA54KfBhCKARIsAJzSrdqzI9Daxg9E03-KLKGt4284z5_G1Jiki16qya1kzVBxo9JEEz7seX4aAnSeEALw_wcB) ( serves as output unit )

Wiring between respective devices can be found in **wiring.txt** file.

For micropython firmware flashing I used [esptool](https://github.com/espressif/esptool) ( exact usage is present in **flash.txt** )

For sending files from PC to board I used [ampy](https://github.com/scientifichackers/ampy) ( exact usage is present in **flash.txt** )

I modified and upgraded already existing driver for LED matrices which can be found [here](https://github.com/mcauser/micropython-max7219).

Currently, there is only a little test program for communication between led matrix and joystick ( via esp32 ) present. I am planning to add more interesting programs later on.