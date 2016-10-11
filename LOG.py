import logging
import logging.config


class LOG(object):
    def __init__(self,conf,logger):
        self.conf=conf
        logging.config.fileConfig(self.conf)
        self.logger = logging.getLogger(logger)

    def DEBUG(self,mes):
        self.logger.debug(mes)

    def INFO(self,mes):
        self.logger.info(mes)

    def WARN(self,mes):
        self.logger.warn(mes)

    def ERROR(self,mes):
        self.logger.error(mes)

    def CRITICAL(self,mes):
        self.logger.critical(mes)
