from typing import List
from dotenv import dotenv_values
import pymongo


config = dotenv_values(".env")
MONGODB_PASSWORD = config["MONGODB_PASSWORD"]
MONGODB_URI = config["MONGODB_URI"]

client = pymongo.MongoClient(MONGODB_URI)
db = client.blast_results
all_blast_results = db["all_blast_results"]


this_file = "data/blastn_WisConreferecore_FD-GUOC.fasta_2_0.96_AOB_DB.m8"

blast_output_columns = [
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
    "bitscore",
]


def create_mongodb_entry_from_line(
    blast_result_line, column_names=blast_output_columns
):
    return {k: v for k, v in zip(column_names, blast_result_line)}


with open(this_file) as fin:
    for line in fin:
        line = line.strip().split()
        new_mongo_entry = create_mongodb_entry_from_line(line)
        all_blast_results.insert_one(new_mongo_entry)
