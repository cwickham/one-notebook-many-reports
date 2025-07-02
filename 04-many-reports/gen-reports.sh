#!/bin/bash

while IFS=',' read -r city filename; do
    echo "Rendering for city: $city "
    
    quarto render "climate.qmd" \
        -P city:"$city" \
        --output "$filename.pdf"
done < "data/cities.csv"