import sys, os, argparse

print()
print("###### Build site pages ######");
print("PYTHON VERSION: " + ".".join(map(str, sys.version_info[:3])))
print("# Script call: " + " ".join(sys.argv) + "\n----------");

parser = argparse.ArgumentParser(description="Gets stats from a bunch of abyss assemblies.");
parser.add_argument("--all", dest="all", help="Build all pages", action="store_true", default=False);
parser.add_argument("--index", dest="index", help="Without --all: build index.html. With --all: exlude index.html", action="store_true", default=False);
parser.add_argument("--notes", dest="notes", help="Without --all: build notes.html. With --all: exlude notes.html", action="store_true", default=False);
parser.add_argument("--people", dest="people", help="Without --all: build people.html. With --all: exlude people.html", action="store_true", default=False);
parser.add_argument("--samples", dest="samples", help="Without --all: build samples.html. With --all: exlude samples.html", action="store_true", default=False);
parser.add_argument("--summary", dest="summary", help="Without --all: build summary.html. With --all: exlude summary.html", action="store_true", default=False);
parser.add_argument("--summary48", dest="summary48", help="Without --all: build summary_48.html. With --all: exlude summary_48.html", action="store_true", default=False);
parser.add_argument("--summary62", dest="summary62", help="Without --all: build summary_62.html. With --all: exlude summary_62.html", action="store_true", default=False);
parser.add_argument("--workflows", dest="workflows", help="Without --all: build workflows.html. With --all: exlude workflows.html", action="store_true", default=False);
parser.add_argument("--wgs", dest="wgs", help="Without --all: build wgs.html. With --all: exlude wgs.html", action="store_true", default=False);
parser.add_argument("--assemblystats", dest="assemblystats", help="Without --all: build assembly_stats.html. With --all: exlude assembly_stats.html", action="store_true", default=False);
parser.add_argument("--mappingstats", dest="mappingstats", help="Without --all: build mapping_stats.html. With --all: exlude mapping_stats.html", action="store_true", default=False);
args = parser.parse_args();
# Input options.

#cwd = os.getcwd();
os.chdir("generators");

pages = {
    'index' : args.index,
    'notes' : args.notes,
    'people' : args.people,
    'samples' : args.samples,
    'summary' : args.summary,
    'summary48' : args.summary48,
    'summary62' : args.summary62,
    'workflows' : args.workflows,
    'wgs' : args.wgs,
    'assemblystats' : args.assemblystats,
    'mappingstats' : args.mappingstats
}

if args.all:
    pages = { page : False if pages[page] == True else True for page in pages };

if pages['index']:
    os.system("python index_generator.py");

if pages['notes']:
    os.system("python notes_generator.py");

if pages['people']:
    os.system("python people_generator.py");

if pages['samples']:
    os.system("python sample_generator.py");

if pages['summary']:
    os.system("python sample_summary_generator.py");

if pages['summary48']:
    os.system("python summary_48_generator.py");

if pages['summary62']:
    os.system("python summary_62_generator.py");

if pages['workflows']:
    os.system("python workflows_generator.py");

if pages['wgs']:
    os.system("python wgs_generator.py");

if pages['assemblystats']:
    os.system("Rscript assembly_stats_generator.r");

if pages['mappingstats']:
    os.system("Rscript mapping_stats_generator.r");

print("----------\nDone!");


