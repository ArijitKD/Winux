import sys
from cx_Freeze import setup, Executable
import os

# Dependencies are automatically detected, but it might need find tuning
build_exe_options = {"packages": ["tkinter", "ctypes", "os", "sys"], "include_files": ["assets\\"]}

setup  (name = "Microsoft® Windows® Operating System",
        version = "10.0.19041.3758",
        description = "Windows User Experience",
        options = {"build_exe": build_exe_options},
        executables = [Executable(script="winuxcore.py", base="Win32GUI", target_name = "winuxcore", copyright = "© Microsoft Corporation. All Rights Reserved.")])
