#!/bin/bash
# uses curl to only print the http code
curl -so /dev/null -w "%{http_code}" "$1"
