from pathlib import Path

from build_client import build_client
from build_server import build_server

ROOT = Path(__file__).resolve().parent


if __name__ == '__main__':
    build_server()
    build_client()

    print('\nBuild `all` completed successfully.')
