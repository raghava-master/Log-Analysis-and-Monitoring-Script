import logging
import time
import random
import os
import signal
import sys

# Configure logging
logging.basicConfig(level=logging.DEBUG) # Set the root logger level to DEBUG
logger = logging.getLogger(__name__)

# Define log message formats
formats = {
    logging.INFO: "INFO message",
    logging.DEBUG: "DEBUG message",
    logging.ERROR: "ERROR message"
}

# Define log levels to cycle through
log_levels = [logging.INFO, logging.DEBUG, logging.ERROR]

# Function to handle signal interrupt
def signal_handler(sig, frame):
    print("\nMonitoring interrupted. Exiting.")
    sys.exit(0)

# Register the signal handler
signal.signal(signal.SIGINT, signal_handler)

# Main loop to log messages
while True:
    try:
        # Randomly select a log level
        log_level = random.choice(log_levels)
        # Get the log message format for the selected log level
        log_message = formats[log_level]
        # Log the message
        logger.log(log_level, log_message)

        # Sleep for a short interval
        time.sleep(1)
    except Exception as e:
        logger.error(f"An error occurred: {e}")
