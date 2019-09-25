#!/bin/bash

set -e

mkdir external
cd external
wget -qO- https://github.com/biolab/orange3/archive/master.tar.gz | tar -zxf -
mv orange3-master orange3
cd ..

# Screen must be 24bpp lest pyqt5 crashes, see pytest-dev/pytest-qt/35
XVFBARGS="-screen 0 1280x1024x24"

catchsegv xvfb-run -a -s "$XVFBARGS" python scripts/copy_docs.py external/orange3/doc/