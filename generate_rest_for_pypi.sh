#!/bin/bash
command -v pandoc >>/dev/null|| sudo apt-get install pandoc
pandoc README.md -r markdown -o README -w rst
