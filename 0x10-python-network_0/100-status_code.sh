#!/bin/bash
# uses curl to only print the http code
curl -o /dev/null -s -w "%{http_code}" "$1"
