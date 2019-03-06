# ラズパイでLEDを点滅（Lチカ）してみる

## このハンズオンでできるようになること
- ラズパイにOS（Raspbian）をインストールする
- PythonでGPIOのOutputを制御する

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
ターミナルに`python3`と入力するか、IDLEを起動すると対話型のプロンプトが入力待ちの状態となる
### 対話型で実行
```python
print("Helloworld")
```

### ファイルで実行
Helloworld用のPythonソースコード `lchikahelloworld.py` をこのリポジトリからダウンロード  
```sh
wget https://raw.githubusercontent.com/rpi-mokumoku-org/hands-on/master/1.led_flashing/helloworld.py
```
`helloworld.py`を実行  
```sh
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
Lチカ用のPythonソースコード `lchika.py` をこのリポジトリからダウンロード  
```sh
wget https://raw.githubusercontent.com/rpi-mokumoku-org/hands-on/master/1.led_flashing/lchika.py
```
`lchika.py`を実行  
```sh
python3 lchika.py
```
