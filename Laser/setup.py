"""
create executable app.
"""

from cx_Freeze import setup, Executable

setup(name="Musquans GUI",
      version="0",
      description="test",
      executables=[Executable("main.py")])
