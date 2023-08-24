Regexp conversions
```


\\Eg (.*)

```{admonition} Example
:class: tip

$1

\\Egs (.*)

```{admonition} Example
:class: tip

$1


\\Facts? (.*)
```{admonition} Fact
:class: important

$1
```




```

# Convert pdf figures to png
sips -s format png _static/plots/*.pdf --out _static/plots/
sips -s format png *.pdf --out .
