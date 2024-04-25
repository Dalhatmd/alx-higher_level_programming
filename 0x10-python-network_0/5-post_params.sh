#!/bin/bash
# Sends a post request with parameters
email="test@gmail.com"
subject="I will always be here for PLD"
post_data="email=$email&subject=$(echo "$subject" | sed 's/ /%20/g')"
curl -sX POST -d "email"=$email "subject"=$subject "$1"
