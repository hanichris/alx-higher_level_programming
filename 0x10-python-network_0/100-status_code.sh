#!/bin/bash
#Display only the status code of a response without using pipes or redirections
#nor using `;` or `&&`
curl -so /dev/null -w "%{http_code}" "$1"
