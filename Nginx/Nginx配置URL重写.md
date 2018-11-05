URL重写是指通过配置conf文件，以让网站的URL中达到某种状态时则定向/跳转到某个规则，比如常见的伪静态、301重定向、浏览器定向等。
Nginx允许使用正则表达式重写URI（需PCRE库），并且可以根据相关变量重定向和选择不同的配置。


如果这个指令在server段中指定，那么将在被请求的location确定之前执行，如果在指令执行后所选择的location中有其他的重写规则，那么它们也被执行。
如果在location中执行这个指令产生了新的URI，那么location又一次确定了新的URI。这样的循环可以最多执行10次，超过以后nginx将返回500错误。

## rewrite
```
server {
    rewrite 规则 定向路径 重写类型;
}
```
- 规则：可以是字符串或者正则来表示想匹配的目标url
- 定向路径：表示匹配到规则后要定向的路径，如果规则里有正则，则可以使用 $index 来表示正则里的捕获分组
- 重写类型：
 - last ：相当于Apache里德(L)标记，表示完成rewrite，浏览器地址栏URL地址不变。
 - break：本条规则匹配完成后，终止匹配，不再匹配后面的规则，浏览器地址栏URL地址不变。
 - redirect：返回302临时重定向，浏览器地址会显示跳转后的URL地址。

## return
```
return code
```
return指令结束执行配置语句并为客户端返回状态代码，可以使用下列的值：204，400，402-406，408，410, 411, 413, 416与500-504；默认返回None。此外，非标准代码444将关闭连接并且不发送任何的头部。
因为301和302不能简单的只返回状态码，必须有重定向的URL，所以return指令无法返回301,302。

## 例1
```
    server {
        listen 8899;
        server_name localhost;
        root /Users/bowen/python/pages;

        # 访问test1.html时，页面重定向到last.html中，浏览器地址不变
        rewrite /test1.html /last.html last;

        # 访问test2.html时，页面重定向到break.html中，浏览器地址不变
        rewrite /test2.html /break.html break;

        # 访问test3.html时，返回302临时重定向，浏览器地址变为跳转后的地址
        rewrite /test3.html /redirect.html redirect;

        # 访问test4.html时，返回301永久重定向，浏览器地址变为跳转后的地址
        rewrite /test4.html /permanent.html permanent;

        location / {
            # last会继续匹配，返回400错误码
            rewrite /last/ /400.html last;

            # break会直接生效，并停止后续匹配
            rewrite /break/ /400.html break;

        }

        location = /400.html {
            return 400;
        }
    }
```

## last和break的区别
- last一般写在server和if中，而break一般使用在location中
- last不终止重写后的url匹配，即新的url会再从server走一遍匹配流程，而break终止重写后的匹配
- break和last都能组织继续执行后面的rewrite指令
- 在 location 里一旦返回 break 则直接生效并停止后续的匹配 location
- 如果一个重定向是相对的（没有主机名部分），nginx将在重定向的过程中使用匹配server_name指令。

## if判断
```
if (表达式) {
}
```

- 当表达式只是一个变量时，如果值为空或任何以0开头的字符串都会当做false
- 直接比较变量和内容时，使用=或!=
~正则表达式匹配，~*不区分大小写的匹配，!~区分大小写的不匹配
一些内置的条件判断：
- -f和!-f用来判断是否存在文件
- -d和!-d用来判断是否存在目录
- -e和!-e用来判断是否存在文件或目录
- -x和!-x用来判断文件是否可执行

##s et
```
set 变量名 值
```
使用set定义一个新的变量，但是不能使用set设置$http_xxx头部变量的值。

## 内置的全局变量
```
$args ：这个变量等于请求行中的参数，同$query_string
$content_length ： 请求头中的Content-length字段。
$content_type ： 请求头中的Content-Type字段。
$document_root ： 当前请求在root指令中指定的值。
$host ： 请求主机头字段，否则为服务器名称。
$http_user_agent ： 客户端agent信息
$http_cookie ： 客户端cookie信息
$limit_rate ： 这个变量可以限制连接速率。
$request_method ： 客户端请求的动作，通常为GET或POST。
$remote_addr ： 客户端的IP地址。
$remote_port ： 客户端的端口。
$remote_user ： 已经经过Auth Basic Module验证的用户名。
$request_filename ： 当前请求的文件路径，由root或alias指令与URI请求生成。
$scheme ： HTTP方法（如http，https）。
$server_protocol ： 请求使用的协议，通常是HTTP/1.0或HTTP/1.1。
$server_addr ： 服务器地址，在完成一次系统调用后可以确定这个值。
$server_name ： 服务器名称。
$server_port ： 请求到达服务器的端口号。
$request_uri ： 包含请求参数的原始URI，不包含主机名，如：”/foo/bar.php?arg=baz”。
$uri ： 不带请求参数的当前URI，$uri不包含主机名，如”/foo/bar.html”。
$document_uri ： 与$uri相同。
```

## 例2
```
    location = /test_if.html {
        # 默认值为test
        set $name test;

        # 重写一个带参数的URL
        # 如果参数中有 name=xx，则使用该值
        if ($args ~* name=(\w+?)(&|$)) {
            set $name $1;
        }

        # 301
        rewrite ^ /$name.html permanent;
    }
```
上面配置的访问情况：
- /test_if.html =>/test.html
- /test_if.html?name=ok => /ok.html?name=ok

## 参考
- [深入理解Nginx](https://s.click.taobao.com/lMHywKw)
