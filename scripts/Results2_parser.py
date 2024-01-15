from Bio import SearchIO
import numpy as np
from scipy.stats import gmean
from celery import Celery

app = Celery('hhr_parse', broker='pyamqp://guest:guest@localhost//')

@app.task
def parse_hhsearch_output(hhr_file):
    best_hit = []
    best_score = 0
    good_hit_scores = []
    query_id = ''

    for result in SearchIO.parse(hhr_file, 'hhsuite3-text'):
        query_id = result.id
        for hit in result.hits:
            if hit.score >= best_score:
                best_score = hit.score
                best_hit = [hit.id, hit.evalue, hit.score]
            if hit.evalue < 1.e-5:
                good_hit_scores.append(hit.score)

    mean = format(np.mean(good_hit_scores), ".2f")
    std = format(np.std(good_hit_scores), ".2f")
    g_mean = format(gmean(good_hit_scores), ".2f")

    result_dict = {
        'query_id': query_id,
        'best_hit': best_hit[0],
        'best_evalue': best_hit[1],
        'best_score': best_hit[2],
        'score_mean': mean,
        'score_std': std,
        'score_gmean': g_mean
    }

    return result_dict

if __name__ == "__main__":
    result = parse_hhsearch_output.delay('tmp.hhr').get()

    with open("hhr_parse.out", "w") as fhOut:
        fhOut.write("query_id,best_hit,best_evalue,best_score,score_mean,score_std,score_gmean\n")
        fhOut.write(f"{result['query_id']},{result['best_hit']},{result['best_evalue']},{result['best_score']},{result['score_mean']},{result['score_std']},{result['score_gmean']}\n")
