import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(levelname)s: %(message)s',  # 格式
)

logging.debug(123)
logging.info("user created")
logging.warning("invalid input")
logging.error("file not found")