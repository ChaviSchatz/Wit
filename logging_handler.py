import logging

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

fh = logging.FileHandler(rf"wit_logging.log")
fh.setLevel(logging.DEBUG)

# Create a console handler
# ch = logging.StreamHandler()
# ch.setLevel(logging.INFO)

# Create a formatter
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
# ch.setFormatter(formatter)

# Add handlers to the logger
logger.addHandler(fh)
# logger.addHandler(ch)