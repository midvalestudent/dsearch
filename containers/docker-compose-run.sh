#!/bin/bash

# let docker know who started docker-compose
exec docker-compose run -e LOCAL_USER_ID=`id -u $USER` "$@"
