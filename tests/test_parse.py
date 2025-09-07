import pathlib
import sys

sys.path.append(str(pathlib.Path(__file__).resolve().parents[1]))

from hera_app.manager import parse_apt


def test_parse_apt_extracts_packages():
    sample = (
        "Inst bash [5.0] (5.1 Ubuntu)\n"
        "Inst coreutils [8.30] (8.32 Ubuntu)\n"
    )
    assert parse_apt(sample) == ["bash", "coreutils"]
