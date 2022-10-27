#!/bin/bash
#Script to display all the methods a server accepts
curl -sI "$1" | grep Allow | cut -d " " -f 2-
