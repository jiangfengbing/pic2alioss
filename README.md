# pic2alioss

pic2alioss 是一个快捷上传图片到阿里云 OSS 的 Alfred 插件。

适用于使用 Markdown 或者 ReStructedText 书写博客的朋友，快速上传
图片并得到图片 URL。

## 安装

先给系统的 python3 安装 oss 包

```
/usr/bin/pip3 install oss2 --user
```

下载 `Pic2AliOSS.alfredworkflow`，双击该文件进行安装.

## 配置

呼出 Alfred，输入关键词：`alioss-config`, 选择打开: `阿里云图床配置`

按提示输入:

- bucket
- accessKeyId
- accessKeySecret
- urlPrefix

### 注意

不建议在 urlPrefix 直接暴露 OSS 的 URL, 避免 OSS 被攻击产生不必要的费用。

个人网站可以开通 CDN 服务，将 OSS 的 bucket 设为源站，同时 bucket 不需要设为公共读。

在 CDN 服务中限制，带宽峰值，设置防盗链。买一个 CDN 流量包。

点击 <https://www.aliyun.com/minisite/goods?userCode=rroeunf7> 领取最高￥ 2000 云产品通用代金券.

## 使用

### 日常使用

在 Finder 中选中一张图片，切出 Alfred，输入关键词 ossup 回车，开始上传图片。

上传成功后会将图片的 URL 保存到剪贴板，同时有系统通知弹出。

如果上传失败，系统通知会显示失败的原因。

### 获得最后一次的 URL

关键词`uposs-url`呼出执行: `阿里云图床URL`，最后一次成功上传的图片 URL 将保存到剪切板。
