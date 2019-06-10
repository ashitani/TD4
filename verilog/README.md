# TD4 verilog version

[CPUの創りかた](https://www.amazon.co.jp/dp/4839909865) に登場するTD4
をverilogで書き直したものです。

74ロジックICのライブラリは[こちら](https://github.com/TimRudy/ice-chips-verilog)を使用しました。

# ROMデータの作成

assember.pyでアセンブルしたテキストファイルをrom.txtに
コピーします。

```
cp rom/ramen.txt ./rom.txt
```

# シミュレーションと

iverilog/gtkwaveが必要です。

```
make
open ./test_TD4.vcd
```
