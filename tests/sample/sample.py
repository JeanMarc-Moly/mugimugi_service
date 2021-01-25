from dataclasses import asdict
from pathlib import Path
from typing import Type

from mugimugi.entity.utils.xml import parse

from ..configuration import SAMPLE


class Sample:
    file_path: Path
    object: object
    type: Type

    def test_parsing(self):
        self.maxDiff = None
        path = self.file_path
        self.assertTrue(path.exists())
        with path.open("r") as f:
            self.assertDictEqual(
                asdict(parse(self.type, f.read())),
                asdict(self.object),
                f"Failed to properly parse {path.relative_to(SAMPLE)}",
            )
