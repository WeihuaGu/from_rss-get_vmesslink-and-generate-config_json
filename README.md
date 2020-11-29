# from_rss-get_vmesslink-and-generate-config_json
从一个RSS源，或者包含vmess链接的文本文件中，获取里面相应的vmess链接，然后生成配置json

## 只支持linux，且需要安装python
## 使用方法
### 我有一个RSS源，里面包含vmess链接
- 新建一个名为RSS_URL的文件，内容为RSS 地址
- `./makevmess2json`
### 我有一个包含vmess链接的文件
`cat 包含链接的文本文件 |  ./getvmessjson | ./gentarjson > config.json`
### 我想修改默认的本地端口
直接修改template下的basejson.py
