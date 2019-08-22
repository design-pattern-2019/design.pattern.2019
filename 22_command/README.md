# Command Pattern

## 必要なライブラリ

### ubuntu
- tkinter
#### Installation
```
sudo apt install python3-tk
```
## python3での修飾子について
python3ではjavaのように変数やメソッドにprivate,protected修飾子を付けることができない、変わりに以下の様に表現する
```
# private
# 名前の前に_を２つ付ける
__hoge = 'hoge'
def __hoge():
  pass

# protected
# 名前の前に_を1つ付ける
_hoge = 'hoge'
def _hoge():
  pass
```
