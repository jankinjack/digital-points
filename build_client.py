import subprocess
from pathlib import Path
import shutil

from client import info
from build_server import SERVER_DIR

ROOT = Path(__file__).resolve().parent
CLIENT_DIR = ROOT / 'client'
MAIN_DIST = ROOT / 'build' / 'main.dist'
OUTPUT_DIR = ROOT / 'output'

PYTHON_CMD = 'python'


def prepare_dist() -> None:
    shutil.rmtree(MAIN_DIST / 'libmicrodp', ignore_errors=True)
    shutil.rmtree(MAIN_DIST / 'translations', ignore_errors=True)
    shutil.rmtree(OUTPUT_DIR, ignore_errors=True)

    shutil.copytree(SERVER_DIR / 'builds', MAIN_DIST / 'libmicrodp')
    shutil.copytree(CLIENT_DIR / 'translations', MAIN_DIST / 'translations')

    shutil.copy(
        SERVER_DIR / 'inc' / 'micro_dp_extern.h',
        MAIN_DIST / 'libmicrodp',
    )

    release_dir = OUTPUT_DIR / f"Digital Points v{info.__version__}"

    shutil.copytree(MAIN_DIST, release_dir)
    shutil.make_archive(str(release_dir), 'zip', OUTPUT_DIR)


def build_client() -> None:
    subprocess.run([
        PYTHON_CMD,
        '-m',
        'nuitka',
        str(CLIENT_DIR / 'main.py'),
        '--output-filename=Digital Points.exe',
        '--file-description=Digital Points',
        f'--file-version={info.__version__}',
        '--output-dir=build',
        '--msvc=latest',
        '--standalone',
        '--windows-console-mode=disable',
        '--include-windows-runtime-dlls=yes',
        '--enable-plugin=pyside6',
        '--include-module=PySide6.QtOpenGL',
        f"--windows-icon-from-ico={CLIENT_DIR / 'view' / 'images' / 'logo_small_circle.ico'}",
    ], check=True)

    prepare_dist()

if __name__ == '__main__':
    build_client()

    print('\nBuild `client` completed successfully.')
