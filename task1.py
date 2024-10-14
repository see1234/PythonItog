import logging

logger = logging.getLogger("my_app")
logger.setLevel(logging.DEBUG)

debug_info_handler = logging.FileHandler('debug_info.log')
debug_info_handler.setLevel(logging.INFO)

warnings_errors_handler = logging.FileHandler('warnings_errors.log')
warnings_errors_handler.setLevel(logging.WARNING)

formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

debug_info_handler.setFormatter(formatter)
warnings_errors_handler.setFormatter(formatter)

logger.addHandler(debug_info_handler)
logger.addHandler(warnings_errors_handler)

logger.debug('Это отладочное сообщение.')
logger.info('Это информационное сообщение.')
logger.warning('Это предупреждающее сообщение.')
logger.error('Это сообщение об ошибке.')
logger.critical('Это критическое сообщение.')
