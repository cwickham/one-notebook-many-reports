#!/usr/bin/env python

import papermill as pm
import polars as pl

cities = (
    pl.read_csv("data/cities.csv")
    .with_columns(
        pl.col("city")
        .str.strip_chars()
        .str.replace_all(" ", "_")
        .str.replace_all("\\.", "")
        .str.to_lowercase()
        .alias("filename")
    )
    .with_columns(
        (
            pl.lit("reports/")
            + pl.col("filename")
            + pl.lit(".ipynb")
        ).alias("output_file")
    )
)


for row in cities.iter_rows(named=True):
    pm.execute_notebook(
        "_climate.ipynb",
        row["output_file"],
        parameters=dict(city=row["city"]),
        prepare_only=True,
    )
