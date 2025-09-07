from __future__ import annotations

import subprocess
from dataclasses import dataclass, field
from typing import List


@dataclass
class ServerStatus:
    """Represents the update status of a server."""

    host: str
    packages: List[str] = field(default_factory=list)

    @property
    def pending(self) -> int:
        """Number of pending package updates."""
        return len(self.packages)


def run_command(host: str, command: str) -> str:
    """Run a command on a remote host via SSH and return stdout.

    The function assumes that passwordless SSH access is configured for the
    current user. The command is executed using the system ``ssh`` binary so no
    additional Python dependencies are required.
    """
    result = subprocess.run(
        ["ssh", host, command], capture_output=True, text=True, check=False
    )
    return result.stdout


def parse_apt(output: str) -> List[str]:
    """Parse ``apt-get -s upgrade`` output into a list of packages.

    The simulated upgrade output contains lines starting with ``Inst`` for each
    package that would be upgraded. This function extracts the package names
    from those lines.
    """
    packages: List[str] = []
    for line in output.splitlines():
        line = line.strip()
        if line.startswith("Inst "):
            parts = line.split()
            if len(parts) >= 2:
                packages.append(parts[1])
    return packages


def check_updates(host: str) -> ServerStatus:
    """Check a server for pending package updates using ``apt``."""
    output = run_command(host, "sudo apt-get -s upgrade")
    packages = parse_apt(output)
    return ServerStatus(host=host, packages=packages)


def apply_updates(host: str) -> None:
    """Apply outstanding package updates on the specified host."""
    run_command(host, "sudo apt-get upgrade -y")
