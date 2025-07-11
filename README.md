

## Abstract

## Abstract

Would you rather read a “Climate summary” or a “Climate summary for
*exactly where you live*”? Producing documents that tailor your
scientific results to an individual or their situation increases
understanding, engagement, and connection. But, producing many reports
can be onerous.

If you are looking for a way to automate producing many reports, or you
produce reports like this but find yourself in copy-and-paste hell, come
along to learn how Quarto solves this problem with parameterized
reports - you create a single Python notebook, but you generate many
beautiful customized PDFs.

## Description

This talk describes Quarto parameterized reports, a powerful tool for
automating the creation of customized, publication-ready documents from
Python notebooks. Data professionals can streamline their workflows and
enhance scientific communication by generating multiple personalized
reports from a single source, such as risk summaries for different zip
codes or individualized soil health reports for farmers.

The talk will walk through a practical example of taking a notebook that
produces a single report, to a workflow that generates many customized
reports. Attendees will learn how to:

- Add parameters to a notebook so Quarto recognizes them
- Use parameters in their code cells (spoiler: just use them like any
  other variable)
- Render to an output format with specific parameter values
- Automate rendering many reports over a set of parameter values

I’ll also touch on how to customize style to match organizational
branding guidelines.

This talk is for data professionals that need to communicate their
results to multiple stakeholders. It will give them a tool to take the
code they already have to produce values, tables, and plots, and turn it
into a set of customized reports. I’ll assume no prior Quarto knowledge.

## Links

- Quarto CLI https://github.com/quarto-dev/quarto-cli/
- Parameters - Quarto
  https://quarto.org/docs/computations/parameters.html​​

## Examples

The subfolders contain examples for each section of the talk

## Requirements

For running the examples, you need to install the following Python
packages (e.g. in a virtual environment with `uv`):

    uv venv
    uv pip install quarto-cli jupyter polars plotnine pyarrow papermill quarto brand_yml pyfonts geopandas pyhere 
