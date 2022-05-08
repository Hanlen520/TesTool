# TesTool

## 简介

基于PyTest+Requests+Allure+Jenkins的接口自动化测试框架。欢迎star:star:支持。

## 环境配置

```
pip install -r requirements.txt
```

## 目录结构

- api ==> 接口封装层，如封装HTTP接口
- common ==> 各种工具类
- config ==> 配置文件
- core ==> requests请求方法封装、关键字返回结果类
- data ==> 数据驱动，测试数据管理
- log ==> 日志记录文件
- operation ==> 关键字封装层，把多个Python接口封装为关键字
- testcases ==> 测试用例
- pytest.ini ==> pytest配置文件


## 测试数据

本框架采用CSV来存放测试数据，为了适配自定义的csv解析器，请务必对测试数据携带表头。


## 感谢贡献

[wintests-pytestDemo](https://github.com/wintests/pytestDemo)
