#!/usr/bin/env python

from quarto import render
import polars as pl

cities = (
    pl.read_csv("data/cities.csv")
    .with_columns(
        [
            pl.col("city")
            .str.strip_chars()
            .str.replace_all(" ", "_")
            .str.replace_all("\\.", "")
            .str.to_lowercase()
            .alias("filename")
        ]
    )
    .with_columns(
        (pl.col("filename") + pl.lit(".pdf")).alias(
            "output_file"
        )
    )
)

for city, output_file in zip(
    cities["city"], cities["output_file"]
):
    render(
        "climate.qmd",
        execute_params={"city": city},
        output_file=output_file,
    )
