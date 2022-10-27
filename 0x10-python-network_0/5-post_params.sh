#!/bin/bash
#Script to send a POST request to a server
curl -sX POST -d "email=test@gmail.com&subject=I+will+always+be+here+for+PLD" "$1"
