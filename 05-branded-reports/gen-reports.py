#!/usr/bin/env python

from quarto import render 
import polars as pl

cities = pl.read_csv("data/cities.csv")
cities = cities.with_columns([
    pl.col("city")
      .str.strip_chars()
      .str.replace_all(" ", "_")
      .str.to_lowercase()
      .alias("filename")
      ])

cities = cities.with_columns([      
  (pl.col("filename") + pl.lit(".pdf")).alias("output_file")
])

for row in cities.iter_rows(named=True):
    # `render()` is just calling `quarto render` via `subprocess.run()`
    render(
        "climate.qmd",
        execute_params={"city": row["city"]},
        output_file=row["output_file"],
    )

