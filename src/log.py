import logging

class LogEngine():

    def __init__(self, runner):
        self.runner = runner

        self.setupLogging()


    def setupLogging(self):
        #create logger
        logging.basicConfig(level = logging.DEBUG, format = "%(asctime)s - %(name)s - %(levelname)s - %(message)s", datefmt = "%d/%m/%Y %H:%M:%S")
        logger = logging.getLogger(__name__)

        file_handler = logging.FileHandler('../log/stats.log')
        file_handler.setLevel(logging.WARNING)
        formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
        file_handler.setFormatter(formatter)

        logger.addHandler(file_handler)
        #logging.debug('Does this shit work?')
        self.logger = logger


    def logInfoMessage(self, message: str):
        self.logger.info(f"Runner {self.runner.name} - {message}")


    def logWarningMessage(self, message: str):
        self.logger.warning(f"Runner {self.runner.name} - {message}")
