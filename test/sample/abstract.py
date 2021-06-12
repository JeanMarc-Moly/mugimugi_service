from dataclasses import dataclass
from pathlib import Path
from test.configuration import SAMPLE
from typing import Type

from mugimugi.entity.utils.xml import parse


class Sample:
    file_path: Path
    object: dataclass
    type: Type

    def test_parsing(self):
        path = self.file_path
        self.assertTrue(path.exists())
        with path.open("r") as f:
            self.assertDictEqual(
                parse(self.type, f.read()).asdict(),
                self.object.asdict(),
                f"Failed to properly parse {path.relative_to(SAMPLE)}",
            )
