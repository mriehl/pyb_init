#!/bin/bash
command -v pandoc >>/dev/null|| sudo apt-get install pandoc
pandoc -o README.rst README.md