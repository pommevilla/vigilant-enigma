library(flexdashboard)
library(tidyverse)
library(ggtext)
library(glue)
library(shiny)
library(shinyWidgets)
library(gt)
library(DT)
library(plotly)
library(mongolite)

readRenviron(".env")

connection_string <- Sys.getenv("MONGODB_URI")
all_blast_results_collection <- mongo(
  db = "blast_results",
  collection = "all_blast_results",
  url = connection_string
)

blast_results <- all_blast_results_collection$find() %>% 
  as_tibble() %>% 
  mutate(across(
    pident:bitscore,
    ~ as.numeric(.)
  )) 

blast_column_names <- c(
  "qseqid",
  "sseqid",
  "pident",
  "length",
  "mismatch",
  "gapopen",
  "qstart",
  "qend",
  "sstart",
  "send", 
  "evalue",
  "bitscore"
)