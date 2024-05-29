# E-fox

可能是本班~~集翔~~吉祥物

来源：Mr Li has an E fox（某个加an的英语口诀）

已经获得我们尊敬的LJ老师的认可

但是，**为什么**是一只**E-cat**而不是真正的 **fox**

原因非常简单，找不到合适的gif，就拿了一只猫充数 ~~（其实更加应该用狗的，都是犬科）~~

运行需要打包，不然可能会出现一些奇怪的问题（记得需要和图片放在同级目录下）

此外运行需要threading和win32api这两个第三方模块

***不要瞎改打包出来exe的名称***

```bash
pip install threading
pip install pywin32api
```

```bash
pyinstaller -w -F bug.py -i Icon3.ico
```
