# love-injection
コロンレスPythonでラブ注入するやつにゃ！
## なりゆき
にゃあの知り合いにゃんこが[セミコロンレスJavaでラブ注入するやつ](https://github.com/h-kono-it/love-injection)を作ったのをみて、にゃあもやらねばらぬにゃ！と手をつけたにゃ。Pythonはそもそもセミコロンなんて使わないにゃ。その代わりコロンを禁則文字とするにゃ。コロンを使えないのは大激痛にゃ。

+ 関数が定義できない
+ クラスが定義できない
+ 辞書型が使えない
+ if文が使えない
+ for, while文が使えない
+ try, except, finally文が使えない
+ lambda が使えない
+ with とかも使えない

これでプログラムを書くにゃ？ドMにゃ。

## 仕様
`ドド` と `スコ` をランダムに発生する装置があるにゃ。それが`ドド`の次に連続3回`スコ`を発生させると`ラブ注入❤`が発生するにゃ。オリジナルは「ドドスコスコスコ」が連続3回ということにゃが、まあこれでも仕組みとしては問題ないにゃ。

## 苦労したにゃ～
繰り返し処理は必須にゃ。それは内包表記で決まりにゃ。if文についてはどうしても必要なところは三項演算子を使うにゃよ。しかしそれではパターン照合なんてできないにゃあ。そこでオートマトンを使うにゃ！そして作ってみたら、内包表記の中で代入文が使えないことがわかってしまったにゃ・・・絶望にゃ。知恵を絞ってなんとかいけたにゃ。疲れたにゃ・・・
[追記] なににゃ～！セイウチ演算子(`:=`)というものがあるにゃ？知っておったらもっと楽にできていたにゃ。ということで少し書き換えてみるにゃ。

## 動作環境
Python3 で十分動くと思うにゃよ。もしかすると2.7でも動くかもしれないにゃ。
[追記] セイウチ演算子を使ったので3.8以上でしか動かないにゃ。

## 参考
+ **【元凶】** : [セミコロンレスJavaでラブ注入するやつ](https://github.com/h-kono-it/love-injection)
