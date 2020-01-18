#!/bin/bash

for file in "$1/"*.txt; do
    grep -nH "Number of cases this gen" "$file" | tail -1
done
