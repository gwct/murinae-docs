############################################################
# For rodent web, 11.19
# This generates the file "summary.html"
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

                <div id="node_links_cont">
                    <center>
                    <table id="node_links_table">
                        <tr><td>{page_title}<td></tr>
                        <tr><td id="node_link_btn"><a href="{csvdatafile}">Download CSV table</a></td></tr>
                    </table>
                    </center>
                </div>

                <div id="node_table_cont">
                    <table id="node_table">
                        {node_table}
                    </table>
                </div>

                
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
pagefile = "summary.html";
print("Generating " + pagefile + "...");
title = "Murine sample summary"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

page_title = "Summary of Murine sampling"

infilename = "../../data/sample-summary.csv";
outfilename = "../../" + pagefile;

first = True;
node_table = "";
for line in open(infilename):
    #print line;
    line = line.strip().split(",");
    if first:
        node_table += "\t\t\t\t<thead>\n\t\t\t\t\t";
    else:
        node_table += "\t\t\t<tr>";

    for x in range(len(line)):
        if first:
            node_table += "<th>" + line[x] + "</th>";
        else:
            if line[x] != "NA":
                node_table += "<td>" + line[x] + "</td>";
            else:
                node_table += "<td></td>";

    if first:
        node_table += "\t\t\t\t</thead>\n";
        first = False;
    else:
        node_table += "</tr>\n";
node_table += "\t\t</table>\n";
with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, node_table=node_table, page_title=page_title, csvdatafile=infilename, footer=footer));
