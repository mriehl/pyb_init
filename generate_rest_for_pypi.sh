#!/bin/bash
command -v pandoc >>/dev/null|| sudo apt-get install pandoc
pandoc README.md -o README -w rst