import logging

def get_logger(log_format=None):
    log_level = logging.DEBUG

    if log_format is None:
        log_format = '[%(levelname)s]\t%(asctime)s.%(msecs)dZ\t%(aws_request_id)s\t[%(filename)s:%(lineno)d]\t%(message)s\n'

    logger = logging.getLogger()
    logger.setLevel(log_level)
    logger_handler = None

    for h in logger.handlers:
        handler_class_name = h.__class__.__name__
        if handler_class_name == "LambdaLoggerHandler":
            logger_handler = h
            logger.removeHandler(h)
            break

    # If this is not a LambdaLoggerHandler
    if logger_handler is None:
        log_format = '[%(levelname)s]\t%(asctime)s.%(msecs)dZ\t[%(filename)s:%(lineno)d]\t%(message)s\n'
        logger_handler = logging.StreamHandler()
        logger_handler.setLevel(log_level)

    formatter = logging.Formatter(log_format, '%Y-%m-%dT%H:%M:%S')
    logger_handler.setFormatter(formatter)
    logger.addHandler(logger_handler)

    return logger