Regexp conversions
```




\\begin\{figure\}(?:\[\w\]|)
\\begin\{center\}
\\scalebox\{.\d*\}\{\\includegraphics\{([\w.]*).pdf\}\}
.?\\caption\{(.*)\}
\\end\{center\}
\\end\{figure\}

```{figure} _static/plots/$1.png
:name: $1

$2

\\begin\{figure\}(?:\[\w\]|)
\\begin\{center\}
\\scalebox\{.\d*\}\{\\includegraphics\{([\w.]*).pdf\}\}
\\end\{center\}
\\caption\{(.*)\}
\\end\{figure\}
```{figure} _static/plots/$1.png
:name: $1

$2

\\begin\{figure\}(?:\[\w\]|)
\\begin\{center\}
\\scalebox\{.\d*\}\{\\includegraphics\{(.*).pdf\}\}
\\end\{center\}
\\end\{figure\}
```{figure} _static/plots/$1.png
:name: $1


\\begin\{figure\}(?:\[\w\]|)
\\begin\{center\}
\\scalebox\{.\d*\}\{\\input\{(.*).pdf_t\}\}
(?:\\caption\{(.*)\}|)
\\end\{center\}
\\end\{figure\}
```{figure} _static/plots/$1.png
:name: $1

$2


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


DEFINITION
```{admonition} Definition
:class: caution





\\begin\{equation\*?\}((.|\n)*?)\\end\{equation\*?\}
\$$ $1 \$$
%
afterwards replace
\$$
$$

()$$
((.|\n)*?)\\end\{equation\*?\}
\$$ $1 \$$




```

# Convert pdf figures to png
sips -s format png _static/plots/*.pdf --out _static/plots/
sips -s format png *.pdf --out .
