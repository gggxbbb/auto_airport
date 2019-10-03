# AutoAirport
A simple script for automatic check-in.  
一个用于机场批量签到的简易脚本.  

## 使用方法
1. 安装 `Git`
2. 安装 `Python3`
3. 执行命令, 克隆源码
   ```
   git clone https://github.com/gggxbbb/auto_airport.git
   cd auto_airport
   ```
4. 执行命令, 安装依赖
   ```
   pip3 install PyYaml
   pip3 install requests
   ```
5. 在 `run.py` 同级目录下创建文件 `data.yml`
6. 在 `data.yml` 下输入如下的内容
   ```yaml
    airport:
      - https://xxx.xxx
      - https://xxxx.xx

    user:
      - mail: 1001@qq.com
        passwd: acb
      - mail: 100@qq.com
        passwd: aad
   ```
   将会尝试在每个提供的机场地址尝试使用每个账号进行签到.
   1. 机场部分
      ```yaml
      airport:
        - https://xxx.xxx
        - https://xxxx.xx
      ```
      请输入包含 `http://` 或 `https://` , 不包含最末尾的 `\` 的 机场地址
   2. 账号密码
      ```yaml
        user:
          - mail: 1001@qq.com
            passwd: acb
          - mail: 100@qq.com
            passwd: aad
      ```
      请输入您的 邮箱地址 和 密码, 暂不支持其他登录方式和两步验证.
7. 执行命令 `python3 run.py`