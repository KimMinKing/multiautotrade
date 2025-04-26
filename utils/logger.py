import logging
import sys
from colorlog import ColoredFormatter

logger = logging.getLogger('autotrade')
logger.setLevel(logging.DEBUG)  # 디버그부터 다 보기

# 포맷 설정 (컬러)
formatter = ColoredFormatter(
    "%(log_color)s%(asctime)s [%(levelname)s] %(name)s: %(message)s",
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG':    'cyan',
        'INFO':     'green',
        'WARNING':  'yellow',
        'ERROR':    'red',
        'CRITICAL': 'bold_red',
    }
)

# 콘솔 핸들러
ch = logging.StreamHandler(sys.stdout)
ch.setFormatter(formatter)
logger.addHandler(ch)

# (선택) 파일 핸들러 추가하고 싶으면 아래 주석 해제
# fh = logging.FileHandler('autotrade.log')
# fh.setFormatter(logging.Formatter(
#     fmt='%(asctime)s [%(levelname)s] %(name)s: %(message)s',
#     datefmt='%Y-%m-%d %H:%M:%S'
# ))
# logger.addHandler(fh)
