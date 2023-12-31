#!/bin/bash
# Create the Downloads directory if it doesn't exist
mkdir -p Downloads

# Read the CSV file line by line
cat Top2000-2022.csv | xargs -n 4 -P 4 -I {} bash -c 'IFS="," read -ra ADDR <<< "{}"; curl -L -o "Downloads/Dec${ADDR[0]}-$(printf "%02d" ${ADDR[1]})00-$(printf "%02d" ${ADDR[2]})00.mp3" "${ADDR[3]}"'