############################################################
# For rodent web, 11.19
# This generates the file "wgs.html"
############################################################


import sys, os
sys.path.append('..')
import lib.read_chunks as RC

######################
# HTML template
######################

html_template = """
<!doctype html>
    {head}

<body>
    {nav}

	<div class="pure-g" id="main_row">
		<div class="pure-u-3-24" id="margin"></div>
		<div class="pure-u-18-24" id="main_col">
			<div id="main_content">
                <h1>{page_title}</h1>
                
                <img class="pure-img" id="logo_main" src="figs/nih-fig2.png">
                <center>Bold text indicates proposed species for WGS. Clade colors represent geographical regions (see Kevin's map).</center>
			</div>
		</div>
		<div class="pure-u-3-24" id="margin"></div>
	</div>

    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "wgs.html";
print("Generating " + pagefile + "...");
title = "WGS"
page_title = "Proposed WGS"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, page_title=page_title, footer=footer));