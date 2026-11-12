import os
import signal
import subprocess
from pathlib import Path

MAX_OUT = 4000


def run_command(cmd: str, timeout: int = 5) -> str:
    """
    recebe o comando e o timeout (tempo limite de execução de código)
    executa o comando e retorna o return do código exectado
    """
    if not cmd.strip():
        return ""

    process:subprocess.Popen = subprocess.Popen(
        ["/bin/sh", "-c", cmd],
        cwd=Path.home(),
        stdin=subprocess.DEVNULL,
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        text=True,
        start_new_session=True
    )

    try:
        output, _ = process.communicate(timeout=timeout)

    except subprocess.TimeoutExpired:
        try:
            os.killpg(process.pid, signal.SIGKILL)
        except ProcessLookupError:
            pass

        output, _ = process.communicate()
        return f"Timeout ({timeout}s)"

    output = (output or "").strip()

    return output[:MAX_OUT] or f"(exit {process.returncode})"

