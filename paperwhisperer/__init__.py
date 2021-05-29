import os
from pathlib import Path

from dotenv import load_dotenv


CONFIG_DATA_PATH = os.path.join(Path(__file__).parent, "config.env")

# load environment variables saved in config.env
load_dotenv(dotenv_path=CONFIG_DATA_PATH)

