#!/bin/bash

set -e

mkdir external
cd external
wget -qO- https://github.com/biolab/orange3/archive/stable.tar.gz | tar -zxf -
mv orange3-stable orange3
wget -qO- https://github.com/quasars/orange-spectroscopy/archive/master.tar.gz | tar -zxf -
mv orange-spectroscopy-master orange-spectroscopy
wget -qO- https://github.com/biolab/orange3-text/archive/master.tar.gz | tar -zxf -
mv orange3-text-master orange3-text
wget -qO- https://github.com/biolab/orange3-bioinformatics/archive/master.tar.gz | tar -zxf -
mv orange3-bioinformatics-master orange3-bioinformatics
wget -qO- https://github.com/biolab/orange3-single-cell/archive/master.tar.gz | tar -zxf -
mv orange3-single-cell-master orange3-single-cell
wget -qO- https://github.com/biolab/orange3-imageanalytics/archive/master.tar.gz | tar -zxf -
mv orange3-imageanalytics-master orange3-imageanalytics
wget -qO- https://github.com/biolab/orange3-network/archive/master.tar.gz | tar -zxf -
mv orange3-network-master orange3-network
wget -qO- https://github.com/biolab/orange3-geo/archive/master.tar.gz | tar -zxf -
mv orange3-geo-master orange3-geo
wget -qO- https://github.com/biolab/orange3-educational/archive/master.tar.gz | tar -zxf -
mv orange3-educational-master orange3-educational
wget -qO- https://github.com/biolab/orange3-timeseries/archive/master.tar.gz | tar -zxf -
mv orange3-timeseries-master orange3-timeseries
wget -qO- https://github.com/biolab/orange3-associate/archive/master.tar.gz | tar -zxf -
mv orange3-associate-master orange3-associate
cd ..

# Screen must be 24bpp lest pyqt5 crashes, see pytest-dev/pytest-qt/35
XVFBARGS="-screen 0 1280x1024x24"

catchsegv xvfb-run -a -s "$XVFBARGS" python scripts/copy_docs.py \
  external/orange3/doc/ \
  external/orange-spectroscopy/doc/ \
  external/orange3-text/doc/ \
  external/orange3-bioinformatics/doc/ \
  external/orange3-single-cell/doc/ \
  external/orange3-imageanalytics/doc/ \
  external/orange3-network/doc/ \
  external/orange3-geo/doc/ \
  external/orange3-educational/doc/ \
  external/orange3-timeseries/doc/ \
  external/orange3-associate/doc/
