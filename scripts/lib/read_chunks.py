############################################################
# For murine web development, 11.17
# Functions to read static html chunks
############################################################

def readHead(title):
    headfile = "../html-chunks/head.html";
    return open(headfile, "r").read().replace("TMPTITLE", title);

def readNav():
    navfile = "../html-chunks/nav.html";
    return open(navfile, "r").read();

def readFooter():
    import time, subprocess
    from datetime import datetime
    footerfile = "../html-chunks/footer.html";
    now = datetime.now().strftime("%m/%d/%Y %H:%M:%S");
    zone = subprocess.check_output("date +%Z").decode().strip();
    return open(footerfile, "r").read().replace("DATETIME", now + " " + zone);