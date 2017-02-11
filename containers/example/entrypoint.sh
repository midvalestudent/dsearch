#!/bin/bash

# set up the user
USER_ID=${LOCAL_USER_ID:-9001}

echo "Starting package $PACKAGE with UID=$USER_ID in PWD=$PWD"
useradd --shell /bin/bash -u $USER_ID -o -c "" -m localuser

# install the main package
PACKAGE_NAME=${PACKAGE}

PKG_DIR=/usr/src/app/packages/$PACKAGE_NAME
pip install -e $PKG_DIR

# run the command
exec /usr/local/bin/gosu localuser python -m $PACKAGE_NAME "$@"
