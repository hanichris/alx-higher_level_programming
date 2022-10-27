#!/bin/bash
#Script to display the size of the response message body
curl -sI "$1" | grep "Content-Length" | cut -d " " -f2
