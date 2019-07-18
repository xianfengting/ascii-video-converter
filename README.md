
# ascii-video-converter

# 简介
[ascii-video-converter](https://github.com/xianfengting/ascii-video-converter) 是一个字符画视频转换工具\.该工具使用 ```Python 3``` 编写,视频的拆分与合成使用外部程序 ```ffmpeg``` \.

# 安装说明

1. 使用 ```git``` 克隆本仓库\.

```
$ git clone https://github.com/xianfengting/ascii-video-converter.git
```

2. 确保电脑上已安装 ```ffmpeg``` \.若未安装,以下两种安装方法任选其一:

    - 执行命令:
    ```
    $ sudo apt-get install ffmpeg
    ```
    - 从[官网](https://ffmpeg.org)下载安装包/源码进行安装\.

3. 使用 ```pip``` 安装需求文件\.
```
$ pip3 install -r requirements.txt
```

# 使用说明

程序运行命令:

```
$ python3 run.py <input_file> -o/--output <output_file>
```

参数说明:

- input_file - 要转换成字符画视频的文件路径\(含文件名\)\.
- output_file - 输出文件名称\(含文件名\)\.

# 许可证

本项目使用 ```MIT License``` 开源协议授权\.协议内容请见 [LICENSE](LICENSE) 文件\.
