jquery对 ajax 的支持

#### 1.$obj.load()

​		作用：载入远程的HTML文件到指定的元素中

```javascript
$obj.load(url,data,callback)
	$obj:显示响应内容的jq元素
	url:请求地址
	data:请求参数(可省略)
		方式1:字符串传参
		"key1=value1&key2=value2"
		注：此种传参会使用 get 方式发送请求
        
		方式2:使用JS对象传参
		{
   		 key1:"value1",
         key2:"value2"
		}
		注：此种传参会使用 post 方式发送请求
        		默认不传参时，发get请求。
	   callback:响应成功后的回调函数(可省略)

```

#### 注意：

```
请求：
GET请求的请求头没有Content-Type
POST请求的请求头一定有Content-Type
$obj.load触发post	请求 的时候，Content-Type为表单头application/x-www-form-urlencoded

响应：
响应头中一定有Content-Type，具体内容具体分析

403错误表示禁止访问。(csrf)

当访问远程页面（就是指跟当前域不同的地址），请求可以发送，但是浏览器将此次请求响应进行拦截
控制台显示：
已拦截跨源请求：同源策略禁止读取位于 http://www.taobao.com/ 的远程资源。（原因：CORS 头缺少 'Access-Control-Allow-Origin'）。
已拦截跨源请求：同源策略禁止读取位于 http://www.taobao.com/ 的远程资源。（原因：CORS 请求未能成功）。

```



#### 2.$.get() 和 $.post()

​		作用：通过get方式异步的向远程地址发送请求

```javascript
$.get(url,data,callback,type)
		url:请求地址
		data:传递到服务器端的参数
		可以是字符串 ："name=sf.zh&age=18"
		也可以是js对象:
			{
				name:"sf.zh",
				age:18
			}
		callback:响应成功后的回调函数
        ex: function(data){
           console.log(data)
        }
		type:响应回来的数据的格式
			取值如下:
			1.html : 响应回来的文本是html文本
			2.text : 响应回来的文本是text文本
			3.script : 响应回来的文本是js执行脚本
			4.json : 响应回来的文本是json格式的文本
```

​	示例

```javascript
jquery_get.html
def jquery_get(request)
def jquery_get_server(request)

jquery_post.html
def jquery_post(request)
def jquery_post_server(request)
```

#### 3. $.ajax({url:xxx,type:'get',data})

```javascript
参数对象中的属性：
	1.url : 字符串，表示异步请求的地址
	2.type : 字符串，请求方式，get 或 post
	3.data : 传递到服务器端的参数
		可以是字符串 ："name=sf.zh&age=18"
		也可以是js对象:
			{
				name:"sf.zh",
				age:18
			}
	4.dataType : 字符串，响应回来的数据的格式
		1.'html'
		2.'xml'
		3.'text' 
		4.'script'
		5.'json'
		6.'jsonp' : 有关跨域的响应格式
	5.success:回调函数，请求和响应成功时回来执行的操作
	6.error : 回调函数，请求或响应失败时回来执行的操作
	7.beforeSend : 回调函数，发送ajax请求之前执行的操作，如果return false，则终止请求
    8. async:是否为异步请求，true 为异步请求，false为同步请求。
```

示例

```javascript
jquery_ajax.html
def jquery_ajax(request)
def jquery_ajax_server(request)
```

## 跨域

#### 1，什么是跨域

​	跨域：非同源的网页，相互发送请求的过程，就是跨域

```
浏览器的同源策略：
同源：多个地址中，相同协议，相同域名，相同端口被视为是"同源"
在HTTP中，必须是同源地址才能互相发送请求，非同源拒绝请求(<script>和<img>除外)。

http://www.tedu.cn/a.html
http://www.tedu.cn/b.html
以上地址是 "同源"

http://www.tedu.cn/a.html
https://www.tedu.cn/b.html
由于 协议不同 ，所以不是"同源"

http://localhost/a.html
http://127.0.0.1/a.html
由于 域名不同 ，所以不是"同源"

http://www.tedu.cn:80/a.html
http://www.tedu.cn:8080/b.html
由于端口不同 ， 所以不是"同源"
```

#### 2，解决方案

通过 script标签 src 向服务器资源发送请求
由服务器资源指定前端页面的哪个方法来执行响应的数据

#### 3,   jquery 的跨域

jsonp - json with padding
用户传递一个callback参数给服务端，然后服务端返回数据时会将这个callback参数作为函数名来包裹住JSON数据

ex:
	当前地址： http://127.0.0.1:8000/index
    欲访问地址： http://localhost:8000/data?callback=xxx

```javascript
$.ajax({
	url:'xxx',
	type:'get',
	dataType:'jsonp',//指定为跨域访问
	jsonp:'callback',//定义了callback的参数名，以便获取callback传递过去的函数名
	jsonpCallback:'xxx' //定义jsonp的回调函数名
});


//超简版本
$.ajax({
	url:'xxx',
	type:'get',
	dataType:'jsonp',//指定为跨域访问
	success: function(data){
        console.log(data);       
    }
});

注意：jsonp模式只支持get请求。
```

示例

```javascript
def cross(request):
def cross_server(request):
def cross_server_json(request):
cross.html
```

补充：

虚拟环境

```linux
安装：
tarena@tarena:~$ pip3 install virtualenv
Collecting virtualenv
  Downloading https://files.pythonhosted.org/packages/f7/69/1ad2d17560c4fc60170056dcd0a568b83f3453a2ac91155af746bcdb9a07/virtualenv-16.7.4-py2.py3-none-any.whl (3.3MB)
    100% |████████████████████████████████| 3.3MB 235kB/s 
Installing collected packages: virtualenv
Successfully installed virtualenv-16.7.4

创建环境：
tarena@tarena:~$ virtualenv  virtual
tarena@tarena:~/1905/month03/project03/projectb$ virtualenv virtual

Using base prefix '/usr'
New python executable in /home/tarena/virtual/bin/python3
Also creating executable in /home/tarena/virtual/bin/python
Installing setuptools, pip, wheel...
done.


激活：
tarena@tarena:~$ source virtual/bin/activate
(virtual) tarena@tarena:~$ 

关闭：
deactivate

删除：
tarena@tarena:~/1905/month03/project03/projectb$ rm -R virtual


安装：virtualenvwrapper
tarena@tarena:~$ pip3 install virtualenvwrapper
subl .bashrc

workon 切换虚拟环境：


export WORKON_HOME=~/my_env
export　VIRTUALENVWRAPPER_PYTHON=/usr/bin/python3
source
/usr/local/bin/virtualenvwrapper.sh



source .bashrc
tarena@tarena:~$ which python3
/usr/bin/python3

gedit　.txt　打开文件
```

