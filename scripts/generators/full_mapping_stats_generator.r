############################################################
# For rodent web, 01.20
# This generates the file "full_mapping_stats.html"
############################################################


cat("Rendering full_mapping_stats.rmd/html\n")
Sys.setenv(RSTUDIO_PANDOC="C:/Program Files/RStudio/bin/pandoc/")
library(rmarkdown)
setwd("C:/bin/murinae-docs/scripts/generators/")
output_dir = "../.."
render("../markdown/full_mapping_stats.rmd", output_dir = output_dir, params = list(output_dir = output_dir), quiet = TRUE)