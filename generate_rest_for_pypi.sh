#!/bin/bash
command -v pandoc >>/dev/null|| sudo apt-get install pandoc
pandoc README.md -r markdown-implicit_figures -o README -w rst
