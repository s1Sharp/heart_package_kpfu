import logging
import sys

file_handler = logging.FileHandler(filename='/tmp/pytest_log_tmp.log', mode='w')
stdout_handler = logging.StreamHandler(stream=sys.stdout)
handlers = [file_handler, stdout_handler]

logging.basicConfig(
    level=logging.DEBUG,
    format='[%(asctime)s] {%(filename)s:%(lineno)d} %(levelname)s - %(message)s',
    handlers=handlers
)


def get_logger(loggername: str = None) -> logging.Logger:
    if loggername is None:
        raise RuntimeError("specify logger name first")
    return logging.getLogger(loggername)
