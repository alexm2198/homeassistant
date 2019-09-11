#!/usr/bin/python3
import subprocess
from os import getcwd


# opens a new process and runs the script given

def call_script(script_name):
    path = getcwd() + rf"/{script_name}"
    proc = subprocess.Popen([path], shell=True)
    return proc
