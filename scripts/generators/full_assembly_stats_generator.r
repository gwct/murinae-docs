############################################################
# For rodent web, 11.19
# This generates the file "full_assembly_stats.html"
############################################################


cat("Rendering full_assembly_stats.rmd/html\n")
Sys.setenv(RSTUDIO_PANDOC="C:/Program Files/RStudio/bin/pandoc/")
library(rmarkdown)
setwd("C:/bin/murinae-docs/scripts/generators/")
output_dir = "../.."
render("../markdown/full_assembly_stats.rmd", output_dir = output_dir, params = list(output_dir = output_dir), quiet = TRUE)