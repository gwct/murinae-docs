############################################################
# For rodent web, 11.19
# This generates the file "index.html"
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
                <center><h1>{page_title}</h1></center>
                <img class="pure-img" id="logo_main" src="img/5oldworldmice.jpg">
                <center><a href="http://dailymammal.com/murines-five-ways/">http://dailymammal.com/murines-five-ways/</a></center>
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
pagefile = "index.html";
print("Generating " + pagefile + "...");
title = "Murinae"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

page_title = "Murine molecular evolution";

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, page_title=page_title, footer=footer));