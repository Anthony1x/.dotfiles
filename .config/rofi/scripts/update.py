from dotenv import set_key
from pathlib import Path
import sys

index = int(sys.argv[1]) - 1

env = Path('/home/anthony/.config/qtile/.env')

set_key(dotenv_path=env, key_to_set="FAKE_SCREEN_INDEX", value_to_set=str(index))
