<!--
SPDX-FileCopyrightText: Copyright (c) 2024 NVIDIA CORPORATION & AFFILIATES.
SPDX-License-Identifier: Apache-2.0

Modified from original source to remove implementation-specific references.
-->

# Library Design

Here we discuss design considerations for tools implementing these concepts.
Tools implementing these concepts take the information from the [](#solutions) page but make opinionated choices about how to leverage them.
This page aims to explain those choices, as well as provide context on how to safely deviate from those choices on a case-by-case basis.
The discussion here assumes the library loading approach proposed in [](#solutions) (Option 3e).

One architectural approach assumes that the package containing a library includes Python code to expose that library.
The benefit of this approach is that the package can then provide a uniform interface regardless of how the files in the package are rearranged, and consumers can interact with this solely in Python.
However, it is equally viable to put the onus on consumers to determine how the library should be loaded.
In that case, the library wheel can be packaged essentially as-is.
Consuming wheels would be responsible for performing the `ctypes` calls themselves.
The primary downside of this approach is that the same logic has to be duplicated in many places.
The benefit is that the library wheel can be packaged essentially as-is, particularly if the approach taken is a simple binary repackaging.
