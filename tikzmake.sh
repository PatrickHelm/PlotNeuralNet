#!/bin/bash


python $1.py 
pdflatex $1.tex

rm *.aux *.log *.vscodeLog
rm *.tex

cp  $1.pdf ~/master-thesis/paper/images/$1.pdf
if [[ "$OSTYPE" == "darwin"* ]]; then
    open $1.pdf
else
    xdg-open $1.pdf
fi
