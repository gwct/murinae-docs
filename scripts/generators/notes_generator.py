############################################################
# For rodent web, 11.19
# This generates the file "notes.html"
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
                <div class="banner">Meeting at LSU, 11.12.2019</div>

                <h4><a href="notes/11.12.2019-je-kcr.docx" download>Download raw notes</a></h4>

                <h4><a href="samples.html">Sampling</a> was discussed in detail.</h4>
                <h4>The plan:</h4>
                <ol>
                    <li>
                        Carl and Gregg will combine exome data and work on the best assembly/mapping method. Carl will focus on assembly with Spades,
                        while Gregg will develop an iterative mapping approach. We will need to figure out a way to assess and compare approaches. 
                        Gregg will set up a Box folder.
                    </li>
                    </br>
                    <li>
                        Gregg wants to set up a single, unified location for all raw sequence data (Box folder?), with the top directory being the three
                        folders <em>exon-capture</em>, <em>exomes</em>, and <em>genomes</em>, and sub-folders for each species that would contain reads,
                        mappings, assemblies, etc.
                        </br>
                        Jake points out that there are some restrictions to Box, such as a 15GB single file size limit and only 4 nested folders. If these
                        aren't a problem then it should be ok. Gregg will keep this in mind while compiling the data.
                    </li>
                    </br>
                    <li>
                        For exomes, we are freezing the sampling at what was discussed today. Kevin will send libraries of all the Bunomys clade members to
                        Montana for sequencing.
                    </li>
                    </br>
                    <li>
                        Gregg will use only a few of the Pseudomys exomes from the 48 Carl is using so the sampling is not too heavy from that single division.
                        Carl and Gregg can discuss which ones would be best to use.
                    </li>
                    </br>
                    <li>
                        For whole genome sequencing, we are proposing to sequence:
                        <ul>
                            <li>Phloeomys, Musseromys, Papagomys, and Komodomys for body size/longevity contrasts</li>
                            <li>Crossomys and Waiomys for amphibiousness convergence along with Pseudohydromys and Gracilimus for non-convergent sister species. Kevin notes that
                                Hydromys chrysogaster would be another interesting sample to compare montane and amphbiousness.
                            </li>
                            <li>Paucidentomys for worm-sucking convergence (Rhyncomys already sequenced) along with Gracilimus and Apomys for non-convergent sister species.</li>
                        </ul>

                        Sequencing of Notomys was also mentioned, and Kevin notes that there is draft sequence data, possibly from HiSeq 2000.
                    </li>
                    </br>
                    <li>
                        Whole genome sequencing will be simple shotgun sequencing.
                    </li>
                    </br>
                    <li>
                        Gregg will write an NIH NRSA to support the whole genome sequencing. The aims of this grant will focus on phylogenetic discordance, molecular evolution/rate variation,
                        and molecular convergence. For all of these aims, both exomes and genomes will be used to compare these sequencing strategies.
                    </li>
                    </br>
                    <li>
                        <b>We will have a Skype call on Tuesday, November 26 to follow up.</b>
                    </li>
                </ol>
                </br></br>

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
pagefile = "notes.html";
print("Generating " + pagefile + "...");
title = "Notes"

head = RC.readHead(title);
nav = RC.readNav(pagefile);
footer = RC.readFooter();

outfilename = "../../" + pagefile;

with open(outfilename, "w") as outfile:
    outfile.write(html_template.format(head=head, nav=nav, footer=footer));