############################################################
# For i5k web development, 9.17
# This generates the file "node_table.html"
############################################################

import sys, os

######################
# HTML template
######################

html_template = """
<!doctype html>
	<head>
		<title>Murinae</title>
		<meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
		<meta name="viewport" content="width=device-width, initial-scale=1">	
		<link type="text/css" rel="stylesheet" href="css/pure.css"  media="screen,projection" />
		<link type="text/css" rel="stylesheet" href="css/global.css"  media="screen,projection" />
        <link type="text/css" rel="stylesheet" href="css/tables.css"  media="screen,projection" />
		<link rel='shortcut icon' href='img/favicon.png' type='image/x-icon'/ >
	</head>

<body>
	<div class="pure-g" id="desktop_nav">
        <div class="pure-u-7-24" id="margin"></div>
        <div class="pure-u-2-24" id="nav_link_cell"><a href="summary.html" class="nav_link">Summary</a></div>
		<div class="pure-u-2-24" id="nav_link_cell"><a href="samples.html" class="nav_link">Samples</a></div>
		<!-- <div class="pure-u-2-24" id="nav_link_cell"><a href="scores.html" class="nav_link">Sequencing</a></div> -->
		<div class="pure-u-2-24" id="nav_link_cell"><a href="workflows.html" class="nav_link">Workflows</a></div>
        <div class="pure-u-2-24" id="nav_link_cell"><a href="notes.html" class="nav_link">Notes</a></div>
        <div class="pure-u-2-24" id="nav_link_cell"><a href="people.html" class="nav_link">People</a></div>
		<div class="pure-u-7-24" id="margin"></div>
	</div>

	<div class="pure-g" id="mobile_nav">
		<div class="pure-u-24-24 dropdown" id="nav_link_cell">
			<a href="#" class="nav_link"><img class="pure_img" id="mobile_logo_nav" src="img/mobile-nav.png"></a>
			<div class="dropdown_container mobile_drop">
				<ul class="pure-menu-list">
					<li><a href="summary.html" id="mobile_nav_link">Summary</a></li>
					<li><a href="samples.html" id="mobile_nav_link">Sample</a></li>
					<li><a href="workflows.html" id="mobile_nav_link">Workflows</a></li>
					<li><a href="notes.html" id="mobile_nav_link">Notes</a></li>	
					<li><a href="people.html" id="mobile_nav_link">People</a></li>
				</ul>
			</div>
		</div>
	</div>
	<div class="pure-g"><div class="pure-u-1" id="divider_row"></div></div>

	<div class="pure-g" id="main_row">
		<div class="pure-u-24-24" id="main_col">
			<div id="main_content">

                <div id="node_links_cont">
                    <center>
                    <table id="node_links_table">
                        <tr><td>Complete Murine sampling<td></tr>
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

	</div>

	<div class="pure-g"><div class="pure-u-1" id="divider_row"></div></div>
	<div class="pure-g" id="footer">
		<div class="pure-u-1">
			<div id="footer_text">
				<center>Site designed and maintained by <a href="https://gwct.github.io/index.html" target="_blank">Gregg Thomas</a> | Some of the CSS used to design
					this site is from the <a href="https://purecss.io/" target="_blank">Pure CSS</a> project.</center>
			</div>
		</div>
	</div>

</body>
"""


######################
# Main block
######################
print("Generating samples.html...");


infilename = "../data/2019-Muridae-NSF-Genomics-Status-11.19.19.csv";
outfilename = "../samples.html";

first = True;
node_table = "";
include_col = ["Subfamily", "Tribe", "Division", "Genus", "Species", "Geographic Region", "Exons", "Exons Status", "Exome",  "Exome Status", "Genome", "Genome Status"];
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
node_table += "\t\t</table>\n";
with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(node_table=node_table, csvdatafile=infilename));

print("EXONS  : " + str(exons));
print("EXOMES : " + str(exomes));
print("GENOMES: " + str(genomes));