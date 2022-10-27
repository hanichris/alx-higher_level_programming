#!/bin/bash
#Script that sends the header `X-School-User-Id: 98` with the GET request.
curl -sH "X-School-User-Id: 98" "$1"
