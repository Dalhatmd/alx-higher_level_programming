#!/bin/bash
# lists the HTTP methods applicable
curl -sI "$1" | grep -i "allow" | awk -F ': ' '{print $2}'
