# MkPaper v0.2
Python library for compiling a PDF or Word doc of Figures.

LaTeX option assumes pdf figures and word doc assumes png figures.

Installation
============                     

```bash
git clone https://github.com/chrisb13/mkpaper.git
```
Dependencies
============                                                                                                                         
* python                   
* pdflatex (optional)
* python-docx (optional)

Without pdflatex, the package still works (you can create the tex file and not compile). Requires figures to be in pdf format.

To create a word doc you need [python-docx](https://python-docx.readthedocs.org/en/latest/) (installable with [Anaconda](https://www.continuum.io/downloads))

Usage
============
## Examples
Working examples (just change variable(s) in INIT box):

```bash
python examples/example_mkpaper_pdf.py
python examples/example_mkpaper_doc.py
```

## PDFLATEX
In summary, from the example (examples/example_mkpaper_pdf.py):

```python
import mkpaper as mp

#get a list of your figures in PDF format...
import glob
ifiles=sorted(glob.glob('/path/to/plots/' + '*.pdf' ))
assert(ifiles!=[]),"glob didn't find anything!"

#instantiate LatexFigureDoc class:
#arguments are: path/to/put/figuredocs and name of figure doc..
figobj=mp.LatexFigureDoc('/home/nfs/username/examplemkpaper/','testname')

#for each figure pass the path and a caption
figobj.add_figure(ifiles[0],'fig1')
figobj.add_figure(ifiles[1],'fig2')
figobj.add_figure(ifiles[2],'fig3')
#etc

#insert the tail of the doc
figobj.end_tex()

#send build command to pdflatex, this step actually requires pdflatex on the machine
figobj.build_tex()
```
## Word doc
Requires python-docx
```python
import mkpaper as mp

#get a list of your figures in PNG format...
import glob
ifiles=sorted(glob.glob(path_to_pngplots + '*.png' ))
assert(ifiles!=[]),"glob didn't find anything!"

#alternatively, we could be more explicit
#ifile[0]=path_to_doc+'penguin1.png'
#ifile[1]=path_to_doc+'penguin2.png'

#instantiate WordFigureDoc class:
#arguments are: path/to/put/figuredocs and name of figure doc..
figobj=mp.WordFigureDoc(path_to_doc,'penguinfigs')
figobj.add_figure(ifiles[0],'first penguin')
figobj.add_figure(ifiles[1],'second penguin')
#etc

#insert the tail of the doc
figobj.end_doc()
```

Acknowledgements
================

The code was written by Christopher Bull.

Contact
=======

Christopher Bull.                                                               
Affiliation: Climate Change Research Centre and ARC Centre of Excellence for Climate Sys    tem Science.
     Level 4, Mathews Building                                        
     University of New South Wales                                    
     Sydney, NSW, Australia, 2052                                     
Contact: z3457920@student.unsw.edu.au                                         
www:     christopherbull.com.au                                               
twitter: @ChrisBullOceanO                
