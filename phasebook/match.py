import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

   #using time.perf_counter() provides a more precise timer for measuring short durations.
    start_time = time.perf_counter()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    elapsed_time = time.perf_counter() - start_time

    return {"message": msg, "elapsedTime": elapsed_time}, 200

def is_match(fave_numbers_1, fave_numbers_2):
    #fave_numbers_1 is converted to a set fave_numbers_set, making the membership check inside is_match much faster.
    fave_numbers_set = set(fave_numbers_1)
    return all(number in fave_numbers_set for number in fave_numbers_2)
