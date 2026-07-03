
import locale
import os
import sys
from pathlib import Path

from PySide6.QtCore import Qt, QCoreApplication
from PySide6.QtGui import QOffscreenSurface, QOpenGLContext

from digital_points import DigitalPoints

import pyqtgraph as pg

FULL_PATH = Path(__file__).parent


def is_opengl_available() -> bool:
    """
    Synchronously checks if a valid, hardware-accelerated
    OpenGL context can be created.
    """

    # Create an offscreen surface to perform headless checks without
    # spawning a visible window or requiring an active event loop.
    surface = QOffscreenSurface()
    surface.create()

    if not surface.isValid():
        return False

    # Initialize the OpenGL context using Qt's underlying platform plugin.
    ctx = QOpenGLContext()

    if not ctx.create():
        return False

    # Bind the context to our offscreen surface.
    # All subsequent OpenGL API calls require an active context.
    if not ctx.makeCurrent(surface):
        return False

    try:
        # Import PyOpenGL dynamically to prevent hard crashes 
        # if the package is missing in the current environment.
        from OpenGL.GL import glGetString, GL_VENDOR, GL_RENDERER, GL_VERSION

        # Query standard OpenGL strings to verify
        # the context is fully functional.
        vendor = glGetString(GL_VENDOR)
        renderer = glGetString(GL_RENDERER)
        version = glGetString(GL_VERSION)

        # If any string is None, the context creation silently failed
        # or returned an incomplete/invalid state.
        if not (vendor and renderer and version):
            return False

        # Filter out software renderers.
        # Fallbacks like Mesa llvmpipe will return valid GL strings,
        # but they are far too slow for heavy GUI frameworks like pyqtgraph.
        renderer_str = renderer.decode().lower()
        software_renderers = (
            'llvmpipe',
            'swrast',
            'softpipe',
            'microsoft basic render',
            )

        if any(sw in renderer_str for sw in software_renderers):
            return False

        return True

    except Exception:
        # Catch ImportError (missing PyOpenGL) or OpenGL errors.
        # Fallback to False to ensure the app still starts safely.
        return False

    finally:
        # Unbind the context and release native windowing system resources.
        ctx.doneCurrent()
        surface.destroy()


if __name__ == '__main__':
    # Fix problem for high DPI and scale above 100%.
    os.environ['QT_ENABLE_HIGHDPI_SCALING'] = '1'
    os.environ['QT_FONT_DPI'] = '96'
    QCoreApplication.setAttribute(Qt.AA_Use96Dpi, True)

    # Use EN_US locale.
    locale.setlocale(locale.LC_ALL, 'en_US.utf8')

    pg.setConfigOption('antialias', True)

    dp = DigitalPoints(sys.argv)

    # Enable OpenGL.
    if is_opengl_available():
        pg.setConfigOption('enableExperimental', True)
        pg.setConfigOption('useOpenGL', True)
        pg.setConfigOption('leftButtonPan', False)

    # Run the app.
    sys.exit(dp.exec())
