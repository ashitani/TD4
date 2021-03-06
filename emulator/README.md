
# TD4エミュレータ・アセンブラ

[CPUの創りかた](https://www.amazon.co.jp/dp/4839909865)で題材になっている4bit CPU、TD4のエミュレータとアセンブラをpython3で記述したものです。

キーイベント取得のためだけにSDL2を使用しています。下記で導入できます。

```
pip install sdl2
```

# アセンブル

下記のようなコードを例にします。0x07から0x10まで数えたら（１０数えたら）LEDを全点灯して終了です。

ラベルが使えます。即値はpythonのマナーで、10進数は10, 16進数は0xA, 2進数は0b1010,というふうに記述してください。

```
        MOV A,6
LOOP:   ADD A,1
        JNC LOOP
        OUT 15
HALT:   JMP HALT
```

下記のようにアセンブル結果を出力できます。エラーチェック等は全くやっていません。

```
> python assemble.py src/test.asm
37
01
E1
BF
F4
00
00
00
00
00
00
00
00
00
00
00
```

# エミュレータ実行

アセンブラファイルをそのまま突っ込めばアセンブルして実行開始します。同番地へのジャンプはHALTと解釈され終了します。

```
> python run.py src/test.asm
00000:  A[7] B[0] C[0] PC[1] INST[37]    IN[0000] OUT[0000]
00001:  A[8] B[0] C[0] PC[2] INST[01]    IN[0000] OUT[0000]
00002:  A[8] B[0] C[0] PC[1] INST[E1]    IN[0000] OUT[0000]
00003:  A[9] B[0] C[0] PC[2] INST[01]    IN[0000] OUT[0000]
00004:  A[9] B[0] C[0] PC[1] INST[E1]    IN[0000] OUT[0000]
00005:  A[A] B[0] C[0] PC[2] INST[01]    IN[0000] OUT[0000]
00006:  A[A] B[0] C[0] PC[1] INST[E1]    IN[0000] OUT[0000]
00007:  A[B] B[0] C[0] PC[2] INST[01]    IN[0000] OUT[0000]
00008:  A[B] B[0] C[0] PC[1] INST[E1]    IN[0000] OUT[0000]
00009:  A[C] B[0] C[0] PC[2] INST[01]    IN[0000] OUT[0000]
00010:  A[C] B[0] C[0] PC[1] INST[E1]    IN[0000] OUT[0000]
00011:  A[D] B[0] C[0] PC[2] INST[01]    IN[0000] OUT[0000]
00012:  A[D] B[0] C[0] PC[1] INST[E1]    IN[0000] OUT[0000]
00013:  A[E] B[0] C[0] PC[2] INST[01]    IN[0000] OUT[0000]
00014:  A[E] B[0] C[0] PC[1] INST[E1]    IN[0000] OUT[0000]
00015:  A[F] B[0] C[0] PC[2] INST[01]    IN[0000] OUT[0000]
00016:  A[F] B[0] C[0] PC[1] INST[E1]    IN[0000] OUT[0000]
00017:  A[0] B[0] C[1] PC[2] INST[01]    IN[0000] OUT[0000]
00018:  A[0] B[0] C[1] PC[3] INST[E1]    IN[0000] OUT[0000]
00019:  A[0] B[0] C[1] PC[4] INST[BF]    IN[0000] OUT[1111]
00020:  A[0] B[0] C[1] PC[4] INST[F4]    IN[0000] OUT[1111]
HALTED
```

クロック周波数を変えたい場合は引数に[Hz]を与えてください。

```
> python sim.py src/test.asm 100
```

キーボードから0-9,A-Fのキーを入力するとINポートを変更できます。Rキーを押すとリセットが入ります。

# その他

本誌内に記載のあるプログラム(blink.asm, ramen.asm)も載せてあります。

