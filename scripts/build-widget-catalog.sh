#!/bin/bash

set -e

mkdir external
cd external
wget -qO- https://github.com/biolab/orange3/archive/master.tar.gz | tar -zxvf -
mv orange3-master orange3
cd ..

python scripts/copy_docs.py external/orange3/doc/