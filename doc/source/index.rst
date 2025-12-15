Managing Native Libraries in Python Wheels
==========================================

A major driving force in Python's explosive popularity is the ease with which it can be integrated with libraries written in lower-level compiled languages.
These `extension modules <https://docs.python.org/3/extending/extending.html>`__ are distributed as shared libraries that are loaded by the Python interpreter at runtime.
While extension modules are a powerful tool for Python developers, they are a common source of frustration when distributing Python packages.
One of the most challenging problems associated with extension modules is how to manage the shared libraries that these extension modules depend on.

Python's package manager, `pip <https://pip.pypa.io/en/stable/>`__, is primarily designed to install pure Python packages, and it struggles with the additional complexities required to produce safe, self-consistent software environments once complex extension modules with complex dependency trees are involved.
Most of these challenges are well documented at `pypackaging-native <https://pypackaging-native.github.io/>`__, so this document will not attempt to duplicate that information.

This package provides a hook-based mechanism to automatically load package-provided dynamic libraries at Python startup, enabling safe sharing of native libraries between Python wheels.
The approach leverages Python's entry point system and ``.pth`` files to preload shared libraries before extension modules are imported, ensuring that dependencies are available when needed.

The documentation provided here focuses on the underlying mechanics of how shared library loading works across different platforms and the various approaches that can be used to solve the library distribution problem.
This technical background is essential for understanding why certain implementation choices were made and how to work effectively with native libraries in Python packages.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   reference/index
