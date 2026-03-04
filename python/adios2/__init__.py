"""The ADIOS2 high-level API module
License:
  Distributed under the OSI-approved Apache License, Version 2.0.  See
  accompanying file Copyright.txt for details.
"""

# pylint: disable=wrong-import-position

import sys

if sys.platform == "win32":
    import os
    from pathlib import Path

    # os.add_dll_directory() covers Python's own loader (level-1 deps of the .pyd).
    # Transitive dependencies (DLLs loaded by those DLLs) use the standard Windows
    # search order, which includes PATH at every depth.  Adding the DLL dirs to PATH
    # ensures adios2_core.dll → adios2_evpath.dll → adios2_ffs.dll etc. are all found.
    _dll_dir_handles = []
    for _dll_dir in (
        Path(__file__).parent,  # pip: adios2/ alongside __init__.py
        Path(__file__).parent.parent / "bin",  # pip: site-packages/bin/
        Path(__file__).parent / "bindings",  # pip: site-packages/adios2/bindings
    ):
        if _dll_dir.is_dir():
            _dll_dir_handles.append(os.add_dll_directory(str(_dll_dir)))
            os.environ["PATH"] = str(_dll_dir) + os.pathsep + os.environ["PATH"]

import adios2.bindings

from adios2.adios import *
from adios2.attribute import *
from adios2.engine import *
from adios2.io import *
from adios2.operator import *
from adios2.stream import *
from adios2.variable import *
from adios2.file_reader import *
from adios2.bindings import (
    LocalValueDim,
    Mode,
    ShapeID,
    StepMode,
    StepStatus,
    DerivedVarType,
    Accuracy,
)

__license__ = "Apache-2.0"
__version__ = adios2.bindings.__version__
is_built_with_mpi = adios2.bindings.is_built_with_mpi

# JoinedDim = 2**64 - 2
JoinedDim = 18446744073709551614
