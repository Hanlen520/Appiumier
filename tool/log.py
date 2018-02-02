# coding:utf-8
from config import AppiumierLogConfig
import logging
import logging.handlers


class LOG:
    logger = None

    @staticmethod
    def get_logger():
        if LOG.logger is not None:
            return LOG.logger
        LOG.logger = logging.getLogger()
        LOG.logger.setLevel(AppiumierLogConfig.LOG_LEVEL)
        rotating_handler = logging.handlers.RotatingFileHandler(
            AppiumierLogConfig.LOG_FILE_PATH,
            maxBytes=AppiumierLogConfig.LOG_MAX_SIZE,
            backupCount=AppiumierLogConfig.LOG_BACKUP_COUNT,
        )
        stream_handler = logging.StreamHandler()
        # formatter = logging.Formatter('%(asctime)s-[%(levelname)s][%(module)s][%(funcName)s]-[%(lineno)d]-%(message)s')
        formatter = logging.Formatter('%(asctime)s-[%(levelname)s]-%(message)s')
        rotating_handler.setFormatter(formatter)
        stream_handler.setFormatter(formatter)
        rotating_handler.setLevel(AppiumierLogConfig.FILE_LOG_LEVEL)
        stream_handler.setLevel(AppiumierLogConfig.STREAM_LOG_LEVEL)
        LOG.logger.addHandler(rotating_handler)
        LOG.logger.addHandler(stream_handler)

        return LOG.logger


logger = LOG.get_logger()
