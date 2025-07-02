Starting from `02-one-qmd`

## Extract out a variable to become a parameter

````
```{python}
city = "Corvallis"
```
````

1.  Re-write code to use the variable:

    1.  Filter step:
        ```{python}
        # ...
        tmean = tmean_oregon.filter(
            pl.col("city") == city,
        )
        ```

    2.  Plot step:

        ```{python}
        # ...
        + labs(title = f"{city}, OR", x="", y="Mean Temperature (°C)")
        # ...
        ```

2. Re-write markdown to use the variable:

````
```{python}
Markdown(f"# {city}")
```
````

3.  Double-check by trying a different city:

    ````
    ```{python}
    city = "Portland"
    ``` 
    ````   

## Identify the variable as a parameter

Add `[parameter]` to `tags`

````
```{python}
#| tags: [parameters]

city = "Corvallis"
```
````

## Render with a parameter


```{bash}
quarto render corvallis.qmd -P city:Portland 
```


But probably want to give a unique output filename:

```{bash}
quarto render corvallis.qmd -P city:Portland --output portland.pdf
quarto render corvallis.qmd -P city:Eugene --output eugene.pdf
```

