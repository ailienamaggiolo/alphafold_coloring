###########################################################################
#
# Color AlphaFold Protein Structure Database predictive models by their
# per-residue confidence score (pLDDT).
#
# Note: The coloring of models in the 3D viewer on the AlphaFold Protein
# Structure Database is different than the coloring used in the ColabFold
# notebooks. For comment on ColabFold coloring, see README.md.
#
# This script is a modified version of the color by conservation output
# script generated from ConSurf (https://consurf.tau.ac.il).
#
#                                                 Ailiena Maggiolo 11/16/21
#
###########################################################################


# Define a Python subroutine to color atoms by B-factor, using predefined
# intervals

def color_plddt(selection="all"):

	# Define the pLDDT bind boundaries
	bin_lower = [
	0,
	50,
	70,
	90 ]

	bin_upper = [
	50,
	70,
	90,
	100 ]

	n_colors = 4
	colors = [
	[0.8784,0.5059,0.3333],
	[0.9765,0.8627,0.3020],
	[0.4980,0.7843,0.9294],
	[0.2157,0.3373,0.6157] ]


	# Loop through color intervals
	for i in range(n_colors):

		lower = bin_lower[i]
		upper = bin_upper[i]
		color = colors[i]

		# Define a unique name for the atoms which fall into this group
		group = selection + "_plDDT_" + str(lower) + "_to_" + str(upper)

		# Compose a selection command which will select all atoms which are
		#	a) in the original selection, AND
		#	b) have B factor in range lower <= b < upper
		sel_string = selection + " & ! b < " + str(lower)

		if(i < n_colors - 1):
			sel_string += " & b < " + str(upper)
		else:
			sel_string += " & ! b > " + str(upper)

		# Select the atoms in bin
		cmd.select(group, sel_string)

		# Create a name for the color
		color_name = "color_" + str(i+1)
		cmd.set_color(color_name, color)

		# Color the atoms in the selected group
		cmd.color(color_name, group)

# This is required to make command available in PyMOL
cmd.extend("color_plddt", color_plddt)

color_plddt()
