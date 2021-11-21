# alphafold_coloring

alphafold_coloring.py is a script that can be implemented in PyMOL to color [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk) predictive models by their per-residue confidence score (pLDDT).

More information about AlphaFold and the pLDDT score can be found [here:](https://www.nature.com/articles/s41586-021-03819-2)


## Implementation

There are two ways you can use alphafold_coloring.py.

1. Drag the alphafold_coloring.py file into your PyMOL instance. By default, this will run the script on all atoms in the PyMOL session.

2. Begin a new PyMOL session and open alphafold_coloring.py by clicking File-->open in the PyMOL menu bar. Load your PDB. To run the function within the script, type:
```
  PyMOL> color_plddt
```

## Color only select atoms by pLDDT

By default, color_plddt will select all atoms for coloring. The following two PyMOL commands are equivalent:
```
  PyMOL> color_plddt
  PyMOL> color_plddt(selection="all")
```

To specify which atoms to apply AlphaFold coloring, first create an object or a selection of atoms which you wish to color. Then run the color_plddt function with the selection specified:
```
  PyMOL> color_plddt(selection="my_object")
```

This example shows how only chain A of the NifH dimer is colored by pLDDT. Chain A was created as the object, "chainA". The coloring was then applied by:
```
  PyMOL> color_plddt(selection="chainA")
```
![example image](https://github.com/ailienamaggiolo/alphafold_coloring/blob/main/nifH_dimer_example_v3.png)

## Additional notes

The [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk/) implements a 3D viewer which displays the predicted structures colored by 4 confidence intervals:

```
[Dark Blue]   Very high (pLDDT > 90)
[Light Blue]  Confident (90 > pLDDT > 70)
[Yellow]      Low (70 > pLDDT > 50)
[Orange]      Very low (pLDDT < 50)
```

Note that the coloring scheme defined by AlphaFold ranges from pLDDT values of 0 to 100 at uneven intervals. The color scheme used by color_plddt matches that used by AlphaFold Protein Structure Database.


## Comments about ColabFold coloring

[ColabFold](https://github.com/sokrypton/ColabFold) coloring is different than the coloring used by [AlphaFold Protein Structure Database](https://alphafold.ebi.ac.uk). ColabFold notebooks appear to use a rainbow coloring scheme, although the mathematical function for this colormap is not explicitly given.

The best I could do to recapitulate ColabFold's coloring scheme was to implement spectrum in PyMOL by:
```
  PyMOL> spectrum b, rainbow_rev, minimum=0, maximum=100
```
although this does not perfectly match what is displayed in the ColabFold notebooks.

Since the full color bar is not specified in the ColabFold notebooks, the interpretation of the level of confidence in a given region in a predictive model using this coloring scheme can be misleading. Given this and [additional problems that arise with the use of rainbow coloring schemes](https://www.biorxiv.org/content/10.1101/2020.09.22.308593v1), using the AlphaFold Structure Database coloring is recommended. Of course, the exact pLDDT values for a given atom can always be found in the B-factor column of the predicted structure PDB file.


## Inspiration

This script is a modified version of the color by sequence conservation output script generated from [ConSurf](https://consurf.tau.ac.il).
