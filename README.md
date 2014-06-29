engadget-fes2014teamB-raspi
===========================
Engadget Fes 2014
http://japanese.engadget.com/2014/05/22/engadget-fes-2014-egfes/

Engadget Fesでも電子工作部やります！ 今回はアルコールや炎を検知するセンサーも試せます #egfes
http://japanese.engadget.com/2014/06/04/engdget-fes-egfes/

グループBのRaspberry Piカメラモジュールに使ったPythonコードです。

ハード構成
---------

  konashi --(gpio)-> raspberry pi

主なソースの簡単な説明
-------------------
- intervalCamera.py
インターバル撮影を行うメインプログラム
- controlPort.py
GPIOによるkonashiからの信号線の解釈
- camera.py
単純なカメラ動作のパッケージ
- playBuzzer.py
ブザーを鳴らす部分のプログラム
