#!/bin/bash
# Update, generate and publish the network diagrams
echo "Python version: $(python3 --version)"
git pull
python3 network.py