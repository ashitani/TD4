# TD4 verilog version

[CPUの創りかた](https://www.amazon.co.jp/dp/4839909865) に登場するTD4
をverilogで書き直したものです。

74ロジックICのライブラリは[こちら](https://github.com/TimRudy/ice-chips-verilog)を使用しました。

# ROMデータのコピー

アセンブルの仕方はemulatorフォルダを参照ください。
アセンブル済のテキストファイルをrom.txtにコピーします。

```
cp rom/ramen.txt ./rom.txt
```

# シミュレーションと波形確認

iverilog/gtkwaveが必要です。

また、上述の74ロジックのライブラリを\~/git/ice-chips-verilogにclone済と仮定しています。
MakefileのLIBRARY変数で設定しています。

```
make
open ./test_TD4.vcd
```
