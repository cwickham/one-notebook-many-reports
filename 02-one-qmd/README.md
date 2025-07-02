# Quarto document `*.qmd*`

```{.bash}
quarto convert corvallis.ipynb 
```

## Plain text

Easy copy-paste, easier version control.

Raw and markdown cells become unadorned text

Code cells are surrounded by triple backticks, e.g. 

````
```{python}
this_month = date(2025, 5, 1)
highlight_color = "#FF5733" 
```
````

## Preview/Render work the same

```{.bash}
quarto preview corvallis.qmd
```

