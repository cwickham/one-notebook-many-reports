## Render with a parameter


```{bash}
quarto render climate.ipynb -P city:Portland 
```


But probably want to give a unique output filename:

```{bash}
quarto render corvallis.qmd -P city:Portland --output portland.pdf
quarto render corvallis.qmd -P city:Eugene --output eugene.pdf
```

