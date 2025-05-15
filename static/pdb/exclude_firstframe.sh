#!/bin/bash

for file in ./*.pdb; do
  if [[ -f $file ]]; then
    input_file="$file"
    awk '
    /MODEL      0/,/ENDMDL/ { next }  # Skip lines from "MODEL 0" to "ENDMDL"
    { print }                    # Print all other lines
    ' "$input_file" > "$input_file.tmp"
    echo "Processed $input_file"
    break
  fi
done
