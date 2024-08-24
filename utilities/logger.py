import logging
import os

def logger() -> bool:
    if os.path.exists("../saveData/player_data.xml"):
        logging.info("player_data.xml found")
        return True
    else:
        logging.warning("player_data.xml missing")
        return False
