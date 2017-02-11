#!/bin/bash

# install the main package
PKG_DIR=/usr/src/app/packages/example
pip install -e $PKG_DIR

# build the protobufs
cd $PKG_DIR/example && \
    protoc --python3_out=. messages.proto && \
    echo "done building protobufs" && \
    cd -

# run any additional commands
exec $*
