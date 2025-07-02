# Quarto 

A command line tool to render notebooks to publication-ready documents.

```{.bash}
quarto preview corvallis.ipynb
```

```{.bash}
quarto preview corvallis.ipynb --to typst
```

```{.bash}
quarto render corvallis.ipynb --to typst
```

## Add document options

In a raw (or markdown cell) at the top of the notebook, inside `---`, add options as YAML.

E.g. set a default output format:

```yaml
format: typst
```


E.g. set `echo: false` to hide code in the rendered document:

```yaml
---
echo: false
---
```


## Add code cell options

At top of code cell after special `#|` comment as YAML.

E.g. Don't show anything from this cell in the rendered document:

```python
#| include: false

tmean.head()
```

