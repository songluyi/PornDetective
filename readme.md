
![](http://www.songluyi.com/wp-content/uploads/2017/01/PornDetectiveLogo.png)

# PornDetective - find porn img easilly
[![Travis](https://img.shields.io/travis/rust-lang/rust.svg)](https://pypi.python.org/pypi?name=porndetective&version=1.0.5&:action=display)
[![PyPI](https://img.shields.io/pypi/wheel/Django.svg)](https://pypi.python.org/packages/b2/5a/1c66823dedcd8d3bde6650ff46adf950473af85d903b236df96597b12a3d/porndetective-1.0.5-py3-none-any.whl#md5=f93004691e166209026aa4a473745089)
[![Hex.pm](https://img.shields.io/hexpm/l/plug.svg)]()

## Introduction of PornDetective
This is a simple package used to detect porn picture by skin pixel recognition.
It takes image or image path or image url list or folder as an object and give
you the finally detected result.

*What's More?* 
You can also change the detecting rules easily as you want.

**Now,Lets do it.**



## How to install 
1. ```pip install porndetective```

2. [click me](https://pypi.python.org/pypi?name=porndetective&version=1.0.5&:action=display)

## Quick to use
```python
from porndetective import PornDetective
test=PornDetective(img_object)
test.parse()
```

And then you can see the result on your screen.
##To do list
list | principal | process | Expected completion time| what can you do
---|:---:|---|:---:|:---:
Algorithm optimization | Louis Song | ![progress](http://progressed.io/bar/20) | **5** | wait
fix Memory footprint issue | Louis Song | ![progress](http://progressed.io/bar/40) | **3** | wait

##Ways to use
**img url lists**
```python
from porndetective import PornDetective
from porndetective import LoadWay
url_test_list =\
    ['http://www.haopic.me/wp-content/uploads/2015/04/20150430102011596.jpg'
    , 'http://www.anhuiyubo.com/a/img/b/c/f/1/2/d/16352.jpg'
    ,'http://www.qqgxzlw.cn/uploads/allimg/121207/10324M3N-6.jpg']
LoadWay.url_pic_list(url_test_list)
```

**folder way**
pass the folder path and it will auto scan the folder and find porn img
```python
from porndetective import PornDetective
from porndetective import LoadWay
folder_path=os.getcwd()
LoadWay.folder_way(folder_path)
```

notice:if pass your root path, that will cost long time.

## how to show it woks
You can use showSkinRegions() function.
```python
img = 'test.jpg'
test=PornDetective(img)
test.parse()
test.showSkinRegions()
```
It will generate test_porn.jpg if it is porn img else test_normal.jpg

## Dependencies:

- porn_detective.py	:Main module for importing

- PornError.py:Interprets exceptions thrown by PornDetective

- LoadWay:Add some methods to help you identify img

- TestCase:unitest for PornDetective
