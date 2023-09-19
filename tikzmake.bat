@echo off

REM Run Python script
python %1.py

REM Compile LaTeX file
pdflatex %1.tex

REM Remove auxiliary files
@REM del *.aux *.log *.vscodeLog

REM REM Remove TeX file
@REM del %1.tex
ping 127.0.0.1 -n 2 > nul
REM Open PDF file
start "" %1.pdf