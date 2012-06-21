#!/bin/bash

2to3 -j `grep -c processor /proc/cpuinfo` *.py
nosetests
