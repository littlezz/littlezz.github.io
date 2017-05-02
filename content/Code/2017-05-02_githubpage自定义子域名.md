Title: Github Page 自定义子域名  
tags: 小结, 小技巧

目标：设置域名

```
xxx.github.io --> blog.xxx.com
```
  

- 首先在 github page 上面的项目里添加一个文件`CNAME`, 内容是目标站点`blog.xxx.com`

- 之后， 在 DNS advance 上面增加一条CNAME记录， 如果要使用`blog.xxx.com`那么 `host` 的值填 `blog`而不是`blog.xxx.com`， value 填`xxx.github.io`  

- 如果你的 github page 是一个不断更新的博客， 必须在渲染时增加 CNAME 记录。  我是用的是 pelican， 设置方法是在`pelicanconf.py` 中设置

```python
EXTRA_PATH_METADATA = {
    'static/CNAME':{'path':'CNAME'},
}

STATIC_PATHS = ['images', 
                'static']
``` 

之后就是等待 dns 的刷新了


###小结
CNAME 设置是 `blog`， 而不`blog.xxx.com`, 不然域名会解析到`blog.xxx.com.xxx.com`

另外， pelican 默认只听是 googleapi 上面的， 虽然据说可能大概好像也许， 在北京有服务器， 但是我这里还是很慢， 于是我把字体的 url 改成了中科大的。  

方法：
在主题里的 templates 目录的`base.html`中

```html
<!--<link href='//fonts.googleapis.com/css?family=Source+Sans+Pro:300,400,700,400italic' rel='stylesheet' type='text/css'>-->
<link href='//fonts.proxy.ustclug.org/css?family=Source+Sans+Pro:300,400,700,400italic' rel='stylesheet' type='text/css'>

```

