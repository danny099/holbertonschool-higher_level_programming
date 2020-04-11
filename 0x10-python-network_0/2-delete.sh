#!/bin/bash
#sends a DELETE request to the URL and displays the body of the response
curl -s -XDELETE "$1"
