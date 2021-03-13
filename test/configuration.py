from os.path import realpath
from pathlib import Path

RESOURCES = (Path(realpath(__file__)).parent / "../resources").absolute()
XML = RESOURCES / "xml"
SAMPLE = XML / "sample"
