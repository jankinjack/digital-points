import shutil
import subprocess
from pathlib import Path
from glob import glob
import re
import os

ROOT = Path(__file__).resolve().parent

SERVER_DIR = ROOT / 'server'


def build_server() -> None:
    base_dir = Path(SERVER_DIR)

    # List of all meson cross-files and archs.
    cross_files = glob(str(SERVER_DIR) + '\\cross_*.txt')
    archs = [re.findall(r".*cross_(.*)\.txt", cross_file)[0] for cross_file in cross_files]

    # List of all directories to clean before building
    build_dirs = ['build_' + arch for arch in archs]

    # 1. Clean up old directories.
    for d in build_dirs + ['builds']:
        shutil.rmtree(base_dir / d, ignore_errors=True)

    # 2. Configure meson (meson setup).
    for arch, dir in reversed(list(zip(archs, build_dirs))):
        # Strip the 'cross_' prefix to get the cross-file name.
        cross_file = f"cross_{arch}.txt"

        try:
            subprocess.run([
                    'meson',
                    'setup',
                    dir,
                    '--buildtype=plain',
                    f'--cross-file={cross_file}'
                    ],
                cwd=SERVER_DIR,
                check=True
                )
        except subprocess.CalledProcessError:
            build_dirs.remove(dir)
            archs.remove(arch)

    # 3. Compile meson.
    for dir in build_dirs:
        try:
            subprocess.run([
                'meson',
                'compile',
                '-j 12',
                '-vC',
                dir],
                cwd=SERVER_DIR,
                check=True
                )
        except subprocess.CalledProcessError:
            pass

    # 4. Create the builds directory.
    builds_dir = base_dir / 'builds'
    a_dir = base_dir / 'builds' / 'a'
    lib_dir = base_dir / 'builds' / 'lib'
    dll_dir = base_dir / 'builds' / 'dll'

    builds_dir.mkdir()
    a_dir.mkdir()
    lib_dir.mkdir()
    dll_dir.mkdir()

    # 5. Copy lib files.
    for arch, dir in zip(archs, build_dirs):
        src_a = base_dir / dir / f'libmicrodp_{arch}.a'
        src_dll = base_dir / dir / f'libmicrodp_{arch}.dll'

        if os.path.exists(src_a):
            shutil.copy(src_a, a_dir / f'libmicrodp_{arch}.a')
            shutil.copy(src_a, lib_dir / f'libmicrodp_{arch}.lib')

        if os.path.exists(src_dll):
            shutil.copy(src_dll, dll_dir / f'libmicrodp_{arch}.dll')

    # 6. Clean up directories again.
    for d in build_dirs:
        shutil.rmtree(base_dir / d, ignore_errors=True)

if __name__ == '__main__':
    build_server()

    print('\nBuild `server` completed successfully.')
