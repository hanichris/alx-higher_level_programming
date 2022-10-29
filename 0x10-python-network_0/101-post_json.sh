#!/bin/bash
#Upload a json file to a server
curl -sX POST "$1" -H "Content-Type: application/json" -d@"$2"
