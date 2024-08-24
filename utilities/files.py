import os
import shutil
import logger
import sys

xml = """
<?xml version="1.0" encoding="UTF-8"?>

<player>
 <name></name>
 <age></age>
 <position></position>
 <attributes>
  <weakfoot></weakfoot>
  <attacking></attacking>
  <defending></defending>
  <positioning></positioning>
 </attributes>
</player>
"""

def createFiles(*args):
    if not logger.logger():
        with open("../saveData/player_data.xml", "w") as f:
            f.writelines(xml)

if __name__ == "__main__":
    createFiles(sys.argv)
