############################################################
# For i5k web development, 9.17
# This generates the file "node_table.html"
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
        <div class="pure-u-1-24" id="margin"></div>
		<div class="pure-u-22-24" id="main_col">
			<div id="main_content">

                <div id="node_links_cont">
                    <h1>{page_title}</h1>

                    MultiQC reports
                    <ul>
                        <li><a href="data/multiqc/nextseq-single-1.html" target="_blank">NextSeq single run 1</a></li>
                        <li><a href="data/multiqc/nextseq-single-2.html" target="_blank">NextSeq single run 2</a></li>
                        <li><a href="data/multiqc/nextseq-paired-1.html" target="_blank">NextSeq paired run 1</a></li>
                        <li><a href="data/multiqc/nextseq-paired-2.html" target="_blank">NextSeq paired run 2</a></li>
                        <li><a href="data/multiqc/miseq-paired.html" target="_blank">MiSeq paired</a></li>
                        <li><a href="data/multiqc/hiseq-paired.html" target="_blank">HiSeq paired</a></li>
                        <li><a href="data/multiqc/hiseq2500-paired.html" target="_blank">HiSeq2500 paired</a></li>
                    </ul>
                    <p><h4><a href="assembly_stats.html">Assembly with Abyss and Spades</a></h4></p>
                    <p><h4><a href="mapping_stats.html">Mapping to Mouse and Rat reference genomes</a></p></h4>

                    <h2>Sample summary table</h2>
                    

                    <center>
                    <table id="node_links_table">
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
		<div class="pure-u-1-24" id="margin"></div>
	</div>

    {footer}
</body>
"""

######################
# Main block
######################
pagefile = "summary_48.html";
print("Generating " + pagefile + "...");
title = "48 exome summary"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

page_title = "Summary of 48 exome samples"

infilename = "../../data/summary-48-exomes.csv";
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