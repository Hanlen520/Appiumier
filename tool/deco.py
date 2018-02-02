# coding:utf-8
from tool.log import logger
import time


def exe_deco(func):
    def wrapper(*args):
        try:
            start_time = time.time()
            ret = func(*args)
            end_time = time.time()
            use_time = str(round(end_time - start_time, 3))
            logger.info(func.__name__ + "测试通过,用时:" + use_time)
            return ret
        except Exception as e:
            logger.info(func.__name__ + "测试失败,原因:" + str(e))

    return wrapper
