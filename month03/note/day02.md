[TOC]
# CSS 基础使用
## 一、CSS介绍
 CSS全称为层叠样式表 ，与HTML相辅相成，实现网页的排版布局与样式美化
## 二、CSS使用方式
### 1. 行内样式/内联样式（单一页面中使用）
  借助于style标签属性，为当前的元素添加样式声明
  ```html
 <标签名 style="样式声明">
  ```
  CSS样式声明 : 由CSS属性和值组成
  例：

  ```html
 style="属性:值;属性:值;"
  ```
  常用CSS属性 :
  - 设置文本颜色 color:red;
  - ###### 设置背景颜色 background-color:green;
  - 设置字体大小 font-size:32px;
### 2. 内嵌样式（少量页面中使用）
  借助于style标签，在HTML文档中嵌入CSS样式代码，可以实现CSS样式与HTML标签之间的分离。同时需借助于CSS选择器到HTML 中匹配元素并应用样式
  示例:

  ```
  <style>
     	选择器{
     	 	属性:值;
      		属性:值;
     	}
  </style>
  ```
  选择器 : 通过标签名或者某些属性值到页面中选取相应的元素，为其应用样式
  示例：
  ```css     					
/*标签选择器 : 根据标签名匹配所有的该元素*/  
p{
    color:red;
  }
  ```
### 3. 外链样式表（项目中使用）
  - 创建外部样式表文件 后缀使用.css
  - 在HTML文件中使用<link>标签引入外部样式表
  ```html
 <link rel="stylesheet" href="URL" type="text/css">
  ```
  - 样式表文件中借助选择器匹配元素应用样式
##  三、 样式表特征
### 1. 层叠性
多组CSS样式共同作用于一个元素
### 2. 继承性
后代元素可以继承祖先元素中的某些样式
例 : 大部分的文本属性都可以被继承

### 3. 样式表的优先级
优先级用来解决样式冲突问题。同一个元素的同一个样式(例如文本色)，在不同地方多次进行设置，最终选用哪一种样式？此时哪一种样式表的优先级高选用哪一种。
  - # **离元素最近的样式优先级最高**（就近原则）
  - 文档内嵌与外链样式表，优先级一致，看代码书写顺序，后来者居上
  - 浏览器默认样式和继承样式优先级较低
## 四、CSS 选择器
### 1. 作用
匹配文档中的某些元素为其应用样式
### 2. 分类 :
#### 1. 标签选择器
根据标签名匹配文档中所有该元素
语法 :
```css
标签名{
  属性:值;
}
```
#### 2. id选择器
根据元素的 id 属性值匹配文档中惟一的元素，id具有唯一性，不能重复使用
语法 :
```css
  #id属性值{
  
  }
```
注意 :

###   **id属性值自定义,可以由数字，字母，下划线，- 组成，不能以数字开头;**

  尽量见名知意，多个单词组成时，可以使用连接符，下划线，小驼峰表示

#### 3. class选择器/类选择器
根据元素的class属性值匹配相应的元素,class属性值可以重复使用,实现样式的复用
语法 :

```css
.class属性值 {
 	
}
```
特殊用法 :
 1. 类选择器与其他选择器结合使用
      注意标签与类选择器结合时,标签在前,类选择器在后
        	例 : a.c1{ }
 2. class属性值可以写多个,共同应用类选择器的样式
    	例 : 
        	.c1{  }
        	.c2{  }						
  	<p class="c1 c2"></p>
#### 4. 群组选择器
为一组元素统一设置样式
语法 :

```css
selector1,selector2,selector3{	
}
```
#### 5. 后代选择器
匹配满足选择器的所有后代元素(包含直接子元素和间接子元素)
语法 :
```css
selector1 selector2{
}
```
匹配selector1中所有满足selector2的后代元素
#### 6. 子代选择器
匹配满足选择器的所有直接子元素
语法 :
```css
selector1>selector2{
}
```
#### 7. 伪类选择器
为元素的不同状态分别设置样式,必须与基础选择器结合使用
分类 :
```
:link 	 超链接访问前的状态    
:visited 超链接访问后的状态
:hover	 鼠标滑过时的状态
:active  鼠标点按不抬起时的状态(激活)
:focus	 焦点状态(文本框被编辑时就称为获取焦点)
```
使用 :
```css
a:link{
}
a:visited{
}
.c1:hover{ }
```
注意 :
  1. 超链接如果需要为四种状态分别设置样式,必须按照以下顺序书写
  ```css
  :link
  :visited
  :hover
  :active
  ```
  2. 超链接常用设置 :
  ```css
  a{
  	/*统一设置超链接默认样式(不分状态)*/
  }
  a:hover{
  	/*鼠标滑过时改样式*/
  }
  ```
### 3. 选择器的优先级
使用选择器为元素设置样式，发生样式冲突时，主要看选择器的权重，权重越大，优先级越高

| 选择器       | 权重 |
| ------------ | ---- |
| 标签选择器   | 1    |
| (伪)类选择器 | 10   |
| id选择器     | 100  |
| 行内样式     | 1000 |

复杂选择器(后代,子代,伪类)最终的权重为各个选择器权重值之和群组选择器权重以每个选择器单独的权重为准，不进行相加计算
例 :

```css
/*群组选择器之间互相独立，不影响优先级*/
body,h1,p{ /*标签选择器权重为 1 */
 color:red;
}
.c1 a{ /*当前组合选择器权重为 10+1  */
 color:green;
}
#d1>.c2{ /*当前组合选择器权重为 100+10 */
 color:blue;
}
```

## 五、标签分类及嵌套
### 1. 块元素
独占一行,不与元素共行;可以手动设置宽高,默认宽度与与父元素保持一致
例 : body div h1~h6 p ul ol li form table(默认尺寸由内容决定)

### 2. 行内元素
可以与其他元素共行显示;不能手动设置宽高,尺寸由内容决定
例 : span label b strong i s u sub sup a

### 3. 行内块元素
可以与其他元素共行显示,又能手动调整宽高
例 : img input button (表单控件)

### 4. 嵌套原则
1. 块元素中可以嵌套任意类型的元素
    p元素除外,段落标签只能嵌套行内元素,不能嵌套块元素
2. 行内元素中最好只嵌套行内或行内块元素

## 元素的尺寸和颜色

####   1. 元素的尺寸

1. px 像素单位
2. 百分比 % 相对父元素
3. 相对单位 em   1em=16px  通常用于移动端的页面开发  常用1.5em 
4. rpx=小程序页面的单位
5. 当页面元素的内容大小超出了元素的宽度，可以使用 overflow 属性 来解决超出部分的显示方式，建议使用auto;

####   2. 颜色

1. 元素的字体，背景，边框

2. 使用方式 color:red;

   1. 英文单词

   2. rgb:

      1. rgb(0~255),rgb(2,3,5)

      2. # **rgba(0~1),rgba(2,3,5,0.5)**

   3. 16进制

      1. 长的16进制   #ffffff; #000000
      2. 短的16进制   #fff;#000

























  



​				

​							


​			
​			
​		




​			
​			