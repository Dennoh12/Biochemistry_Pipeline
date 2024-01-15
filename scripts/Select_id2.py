import sys
import random
from Bio import SeqIO
from celery import Celery

app = Celery('select_ids', broker='pyamqp://guest:guest@localhost//')

"""
usage: python select_ids.py INPUT.fasta 2000
"""

def read_input(file):
    """
    Function reads a fasta formatted file of protein sequences
    """
    # print("READING FASTA FILES")
    ids = []
    for record in SeqIO.parse(file, "fasta"):
        ids.append(record.id)
    return ids

@app.task
def select_random_ids(file, num_selected):
    """
    Select a random subset of protein IDs from the input file
    """
    ids = read_input(file)
    rand_list = random.sample(ids, int(num_selected))
    return rand_list

if __name__ == "__main__":
    selected_ids = select_random_ids.delay(sys.argv[1], sys.argv[2]).get()
    for selected_id in selected_ids:
        print(selected_id)
