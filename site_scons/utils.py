#Distributed under the MIT licesnse.
#Copyright (c) 2013 Cospan Design (dave.mccoy@cospandesign.com)

#Permission is hereby granted, free of charge, to any person obtaining a copy of
#this software and associated documentation files (the "Software"), to deal in
#the Software without restriction, including without limitation the rights to
#use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies
#of the Software, and to permit persons to whom the Software is furnished to do
#so, subject to the following conditions:
#
#The above copyright notice and this permission notice shall be included in all
#copies or substantial portions of the Software.
#
#THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
#IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
#FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
#AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
#LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
#OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
#SOFTWARE.


import os
import json
import platform
import glob
import re


PROJECT_BASE = os.path.abspath(
                    os.path.join(os.path.dirname(__file__), os.pardir))

DEFAULT_BUILD_DIR = "build"

class ConfigurationError(Exception):
    """
    Errors associated with configuration:
        getting the configuration file for the project
    """
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)


def initialize_build():
    create_build_directory()

def create_bin_name(name):
    return os.path.join(get_build_directory(True), name)

def get_project_base():
    """
    Returns the project base directory

    Args:
        Nothing

    Returns:
        Path (String) to base directory

    Raises:
        Nothing
    """
    return PROJECT_BASE

def create_build_directory():
    """
    Reads in a config dictionary and creates a output build directory

    Args:
        config: Config dictionary

    Return:
        Nothing

    Raises:
        Nothing
    """
    build_dir = DEFAULT_BUILD_DIR
    build_dir = os.path.join(get_project_base(), build_dir)
    if not os.path.exists(build_dir):
        os.makedirs(build_dir)

    return build_dir

def get_build_directory(absolute = False):
    """Returns the project output directory location

    Args:
        absolute (boolean):
            False (default): Relative to project base
            True: Absolute

    Returns:
        (string): strin representation of the path to the output

    Raises:
        Nothing
    """
    build_dir = DEFAULT_BUILD_DIR
    if absolute:
        build_dir = os.path.join(get_project_base(), build_dir)

    return build_dir

def get_source_list(base = "src", recursive = False):
    """Returns a list of the source files to build
    """
    path = os.path.join(PROJECT_BASE,  base)
    path = os.path.abspath(path)
    file_list = []
    if os.path.isfile(base):
        #This is just one file to build, return it
        file_list.append(base)

    else:
        if recursive:
            file_list = list(set(_get_sources(path)))
        else:
            search_path = os.path.join(path, "*.c")
            p = glob.glob(search_path)
            file_list.extend(p)
            search_path = os.path.join(path, "*.cpp")
            p = glob.glob(search_path)
            file_list.extend(p)

    return file_list

def _get_sources(path):
    """Recursive inner loop"""
    file_path = []
    for base, dirs, _ in os.walk(path):
        for d in dirs:
            p = os.path.join(base, d)
            file_path.extend(_get_sources(p))

    search_path = os.path.join(path, "*.c")
    p = glob.glob(search_path)
    file_path.extend(p)
    search_path = os.path.join(path, "*.cpp")
    p = glob.glob(search_path)
    file_path.extend(p)
    return file_path
