## 一. 概念
### 1.块级元素(block)特性：
总是独占一行，表现为另起一行开始，而且其后的元素也必须另起一行显示;
宽度(width)、高度(height)、内边距(padding)和外边距(margin)都可控制;
### 2.内联元素(inline)特性：
和相邻的内联元素在同一行;
宽度(width)、高度(height)、内边距的top/bottom(padding-top/padding-bottom)和外边距的top/bottom(margin-top/margin-bottom)都不可改变，就是里面文字或图片的大小;

## 二.元素
### 1.块级元素主要有：
 address , blockquote , center , dir , div , dl , fieldset , form , h1 , h2 , h3 , h4 , h5 , h6 , hr , isindex , menu , noframes , noscript , ol , p , pre , table , ul , li
### 2.内联元素主要有：
a , abbr , acronym , b , bdo , big , br , cite , code , dfn , em , font , i , img , input , kbd , label , q , s , samp , select , small , span , strike , strong , sub , sup ,textarea , tt , u , var
### 3.可变元素(根据上下文关系确定该元素是块元素还是内联元素)：
applet ,button ,del ,iframe , ins ,map ,object , script

## 三.应用
### 1.CSS中块级、内联元素的应用：
利用CSS我们可以摆脱上面表格里HTML标签归类的限制，自由地在不同标签/元素上应用我们需要的属性。
### 2. 主要用的CSS样式有以下三个：
display:block  -- 显示为块级元素
display:inline  -- 显示为内联元素
display:inline-block -- 显示为内联块元素，表现为同行显示并可修改宽高内外边距等属性
我们常将<ul>元素加上display:inline-block样式，原本垂直的列表就可以水平显示了。