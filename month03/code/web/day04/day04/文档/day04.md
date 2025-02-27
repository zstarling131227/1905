[TOC]
# 一、布局方式
## 3. 定位布局
结合偏移属性调整元素的显示位置
#### 1）属性
position
#### 2） 取值
可取relative（相对定位）/ absolute（绝对定位）/ fixed（固定定位）
```css
postion:relative/absolute/fixed
```
#### 3）偏移属性
设置定位的元素可以使用偏移属性调整距离参照物的位置
```text
top   	距参照物的顶部
right	距参照物的右侧
bottom	距参照物的底部
left	距参照物的左侧
```
#### 4）分类 
+ relative 相对定位
**相对移动是相对初始位置而言的移动。**
```text
元素设置相对定位,可参照元素在文档中的原始位置进行偏移,不会脱离文档流
```
+ absolute 绝对定位
```text
1. 绝对定位的元素参照离他*最近*的**已经定位**的祖先元素进行偏移,如果没有,则参照窗口进行偏移
2. 绝对定位的元素会脱流,在文档中不占位,可以手动设置宽高
```
使用绝对定位 :
	"父相子绝" : 父元素设置相对定位,子元素绝对定位，参照已定位的父元素偏移.
+ fixed	固定定位
```text
  1. 参照窗口进行定位,不跟随网页滚动而滚动
  2. 脱离文档流
```
#### 5）堆叠次序 
元素发生堆叠时可以使用 z-index 属性调整已定位元素的显示位置，值越大元素越靠上：
+ 属性 : z-index
+ 取值 : 无单位的数值,数值越大,越靠上
+ 堆叠：
 1. 定位元素与文档中正常元素发生堆叠，永远是已定位元素在上
 2. 同为已定位元素发生堆叠，按照 HTML 代码的书写顺序，后来者居上
# 二、背景属性
## 1. 背景颜色
```css
background-color: red;
```
## 2. 背景图片相关
#### 1） 设置背景图片
```css
background-image : url("路径");
```
设置背景图片，指定图片路径，如果路径中出现中文或空格，需要加引号
#### 2） 设置背景图片的重复方式
默认背景图片从元素的左上角显示，如果图片尺寸与元素尺寸不匹配时，会出现以下情况：
1. 如果元素尺寸大于图片尺寸，会自动重复平铺，直至铺满整个元素
2. 如果元素尺寸小于图片尺寸，图片默认从元素左上角开始显示，超出部分不可见
```css
background-repeat:repeat/repeat-x/repeat-y/no-repeat
```
```text
取值 ：
	repeat  默认值，沿水平和垂直方向重复平铺
	repeat-x 沿X轴重复平铺
	repeat-y 沿Y轴重复平铺
	no-repeat 不重复平铺
```
#### 3） 设置背景图片的显示位置
默认显示在元素左上角
```css
background-position:x y;
```
取值方式 ：
```text
1. 像素值
	设置背景图片的在元素坐标系中的起点坐标
2. 方位值
	水平：left/center/right
	垂直：top/center/bottom
	注：如果只设置某一个方向的方位值，另外一个方向默认为center
```
精灵图技术 ：为了减少网络请求，可以将所有的小图标拼接在一张图片上，一次网络请求全部得到；借助于background-position 进行背景图片位置的调整，实现显示不同的图标
#### 4）设置背景图片的尺寸
```css
background-size:width height;
```
取值方式 ：
```text
1. 像素值
	1. 500px 500px; 同时指定宽高
	2. 500px;  指定宽度，高度自适应
2. 百分比
	百分比参照元素的尺寸进行计算
	1. 50% 50%; 根据元素宽高,分别计算图片的宽高
	2. 50%; 根据元素宽度计算图片宽高,图片高度等比例缩放
```

## 3. 背景属性简写
```css
background:color url("") repeat position;
```
注意 ：
1. 如果需要同时设置以上属性值，遵照相应顺序书写
2. background-size 单独设置
#  三、文本属性
## 1. 字体相关
#### 1） 设置字体大小
```css
font-size:20px;
```
#### 2）设置字体粗细程度
```css
font-weight:normal;
```
取值 ：
```text
1. normal（默认值）等价于400
2. bold   (加粗) 等价于700
```
#### 3）设置斜体
```css
font-style:italic;
```
#### 4） 设置字体名称
```css
font-family:Arial,"黑体"; 
```
取值 :
    1. 可以指定多个字体名称作为备选字体，使用逗号隔开
        
   2. 如果字体名称为中文，或者名称中出现了空格，必须使用引号

         例 :

```Css
font-family:Arial;
font-family:"黑体","Microsoft YaHei",Arial;
```

#### 5）字体属性简写
```css
font : style weight size family;
```
注意 :
       1. 如果四个属性值都必须设置，严格按照顺序书
       2. size family 是必填项

## 2. 文本样式
#### 1）文本颜色
```css
color:red;
```
#### 2） 文本装饰线
```css
text-decoration:none;
```
取值 :
    underline		  下划线
    overline		     上划线
    line-through 	 删除线
    none			       取消装饰线

#### 3）文本内容的水平对齐方式
```css
text-align:center;
```
取值 : 
```text
left(默认值)	左对齐
center		  居中对齐
right		  右对齐
```
#### 4）行高
```css
line-height:30px;
```
使用 :
    文本在当前行中永远垂直居中，可以借助行高调整文本在元素中的垂直显示位置
     	line-height = height 设置一行文本在元素中垂直居中
     	line-height > height 文本下移显示
     	line-height < height 文本靠上显示
     特殊 :
     	line-height可以采用无单位的数值，代表当前字体大小的倍数,以此计算行高

# 补充：

1.通过伪类选择器获取相同元素的某个元素
```
   <style>
        /* 在集合中查找某一个子类用nth-child() */
        div:nth-child(1){}
        div:nth-child(2){}
    </style>
```
