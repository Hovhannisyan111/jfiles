import logging
import time

logging.basicConfig(filename='output.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def main():
    logging.info("Script started.")
    print("Performing some operations...")
    time.sleep(2)
    logging.info("Operation 1 completed.")
    time.sleep(2)
    logging.info("Operation 2 completed.")
    print("All operations completed.")
    logging.info("Script finished.")

if __name__ == "__main__":
    main()
