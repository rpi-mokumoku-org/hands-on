# ラズパイでLEDを点滅（Lチカ）してみる

## ラズパイの構成要素を見る
- Raspberry Pi 3 Model B+  
![](https://github.com/rpi-mokumoku-org/hands-on/blob/images/raspi3modelbplus.jpg?raw=true)  
- ACアダプター（2.5A以上）  
![](https://github.com/rpi-mokumoku-org/hands-on/blob/images/ac_adaptor.jpg?raw=true)  
- microSDカード  
![](https://github.com/rpi-mokumoku-org/hands-on/blob/images/microsdcard.jpg?raw=true)  
- キーボード・マウス  
![](https://github.com/rpi-mokumoku-org/hands-on/blob/images/keyboard_mouse.jpg?raw=true)  

## ラズパイにOSをインストールする
ラズパイのOSイメージを取得し、インストールする  
https://github.com/rpi-mokumoku-org/hands-on/wiki/microSDカードにRaspbianをインストールする

## Pythonのプログラムを実行してみる
### 対話型で実行
```python
print("Helloworld")
```

### ファイルで実行
```sh
echo 'print("Helloworld")' > helloworld.py
python3 helloworld.py
```


## Lチカしてみる
### 電子回路を組む
![](https://github.com/rpi-mokumoku-org/hands-on/blob/images/kairozu.jpg?raw=true)  

### 対話型でLチカ
```python
import gpiozero
led = gpiozero.LED(2)
led.on() # → LEDが点灯
led.off() # → LEDが消灯
```


### ファイルでLチカ
下のソースコードを`lchika.py`として作成  
```python
#!/usr/bin/env python
# -*- coding: utf-8 -*-

import RPi.GPIO as GPIO
from time import sleep

def led_on_off():
    LED = 2 #GPIO Number
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(LED, GPIO.OUT)

    #Main loop
    try:
        while True:
            GPIO.output(LED, GPIO.HIGH)
            sleep(0.5)
            GPIO.output(LED, GPIO.LOW)
            sleep(0.5)

    #When Ctl +C pushed
    except KeyboardInterrupt :
        pass  #Noting to do

    #clean up GPIO
    GPIO.cleanup()

if __name__ == '__main__':
    led_on_off()
```
`lchika.py`を実行  
```sh
python3 lchika.py
```
