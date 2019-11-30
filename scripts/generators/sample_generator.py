############################################################
# For rodent web, 11.19
# This generates the file "samples.html"
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
		<div class="pure-u-24-24" id="main_col">
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

    {footer}
</body>
"""


######################
# Main block
######################
######################
pagefile = "samples.html";
print("Generating " + pagefile + "...");
title = "Murine sampling"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

page_title = "Complete Murine sampling"

infilename = "../../data/2019-Muridae-NSF-Genomics-Status-11.19.19.csv";
outfilename = "../../" + pagefile;

first = True;
node_table = "";
include_col = ["Tribe", "Division", "Genus", "Species", "Geographic Region", "Exons", "Exons Status", "Exome",  "Exome Status", "Genome", "Genome Status"];
include_ind = [];

exons, exomes, genomes = 0,0,0;
for line in open(infilename):
    #print line;
    line = line.strip().split(",");
    if first:
        node_table += "\t\t\t\t<thead>\n\t\t\t\t\t";
        for col in line:
            #print(col);
            if col in include_col:
                include_ind.append(line.index(col));
        #print include_col;
        #print(include_ind);
    else:
        node_table += "\t\t\t<tr>";

    for x in range(len(line)):
        if x not in include_ind:
            continue;

        line[x] = line[x].strip();

        if include_col[include_ind.index(x)] == "Exons" and line[x] in ["Y", "y", "Yes", "YES", "yes"]:
            exons += 1;
        if include_col[include_ind.index(x)] == "Exome" and line[x] in ["Y", "y", "Yes", "YES", "yes"]:
            exomes += 1;
        if include_col[include_ind.index(x)] == "Genome" and line[x] != "":
            genomes += 1;

        if first:
            node_table += "<th>" + line[x] + "</th>";
        else:
            if include_col[include_ind.index(x)] == "Geographic Region":
                node_table += "<td>" + line[x].title() + "</td>";
            else:
                node_table += "<td>" + line[x] + "</td>";

    if first:
        node_table += "\t\t\t\t</thead>\n";
        first = False;
    else:
        node_table += "</tr>\n";
with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, node_table=node_table, page_title=page_title, csvdatafile=infilename, footer=footer));

print("EXONS  : " + str(exons));
print("EXOMES : " + str(exomes));
print("GENOMES: " + str(genomes));