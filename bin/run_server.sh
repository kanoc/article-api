#!/usr/bin/env bash

export $(grep -v '^#' .env | xargs)

python ./api/web/server.py
