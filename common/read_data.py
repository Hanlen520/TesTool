import json
import csv
from typing import List

import yaml

from configparser import ConfigParser
from common.logger import logger


class MyConfigParser(ConfigParser):
    # 重写 configparser 中的 optionxform 函数，解决 .ini 文件中的 键option 自动转为小写的问题
    def __init__(self, defaults=None):
        ConfigParser.__init__(self, defaults=defaults)

    def optionxform(self, optionstr):
        return optionstr


class DataLoader(object):

    def __init__(self):
        pass

    @staticmethod
    def load_yaml(file_path):
        logger.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = yaml.safe_load(f)
        logger.info("读到数据 ==>>  {} ".format(data))
        return data

    @staticmethod
    def load_json(file_path):
        logger.info("加载 {} 文件......".format(file_path))
        with open(file_path, encoding='utf-8') as f:
            data = json.load(f)
        logger.info("读到数据 ==>>  {} ".format(data))
        return data

    @staticmethod
    def load_ini(file_path):
        logger.info("加载 {} 文件......".format(file_path))
        config = MyConfigParser()
        config.read(file_path, encoding="UTF-8")
        data = dict(config._sections)
        # print("读到数据 ==>>  {} ".format(data))
        return data

    @staticmethod
    def load_csv(file_path: str, header=False) -> List:
        mylist = []
        with open(file_path, 'r', encoding='utf8') as f:
            data = csv.reader(f)
            for i in data:
                mylist.append(i)
            if not header:
                del mylist[0]  # 删除标题行的数据
        return mylist

