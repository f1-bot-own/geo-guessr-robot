# -*- coding: utf-8 -*-
from collections import Counter
from gamedata.zakovat_data import (
    ZAKOVAT_QUESTIONS,
    ZAKOVAT_BY_ID,
    ZAKOVAT_BY_TYPE,
    get_zakovat_counts,
    get_zakovat_question_by_id,
    get_random_zakovat_questions,
    search_zakovat_by_alias
)

print(f"Total questions: {len(ZAKOVAT_QUESTIONS)}")
assert len(ZAKOVAT_QUESTIONS) == 500, f"Expected 500, got {len(ZAKOVAT_QUESTIONS)}"

counts = get_zakovat_counts()
print("Category counts:", counts)
assert counts['black_box'] == 125
assert counts['deduction'] == 125
assert counts['world_intellect'] == 125
assert counts['blitz'] == 125

seen_ids = set()
correct_index_dist = Counter()

for i, q in enumerate(ZAKOVAT_QUESTIONS):
    expected_id = f"zakovat_{i+1:03d}"
    assert q["id"] == expected_id, f"Question {i} ID expected {expected_id}, got {q['id']}"
    assert q["id"] not in seen_ids, f"Duplicate ID {q['id']}"
    seen_ids.add(q["id"])

    assert q["type"] in {"black_box", "deduction", "world_intellect", "blitz"}, f"{q['id']} invalid type"

    ci = q["correct_index"]
    assert ci in (0, 1, 2, 3), f"{q['id']} invalid correct_index {ci}"
    correct_index_dist[ci] += 1

    for lang in ("uz", "ru", "en"):
        assert lang in q["question"] and q["question"][lang].strip(), f"{q['id']} question {lang} empty"
        assert lang in q["options"], f"{q['id']} options {lang} missing"
        opts = q["options"][lang]
        assert len(opts) == 4, f"{q['id']} options {lang} len != 4"
        assert len(set(opts)) == 4, f"{q['id']} options {lang} has duplicates: {opts}"
        assert lang in q["correct_answer"], f"{q['id']} correct_answer {lang} missing"
        assert opts[ci] == q["correct_answer"][lang], f"{q['id']} {lang} answer mismatch"
        assert lang in q["fun_fact"] and q["fun_fact"][lang].strip(), f"{q['id']} fun_fact {lang} empty"

    assert isinstance(q["aliases"], list) and len(q["aliases"]) > 0, f"{q['id']} aliases empty"

    if q["type"] == "black_box":
        assert q["image_url"] and q["image_url"].startswith("http"), f"{q['id']} missing image_url"

print("Correct index distribution across 500 items:", sorted(correct_index_dist.items()))
# Ensure balanced distribution: each index 0,1,2,3 has ~125
for ci, cnt in correct_index_dist.items():
    assert 120 <= cnt <= 130, f"Index {ci} not balanced: {cnt}"

# Test helper functions
q_sample = get_zakovat_question_by_id("zakovat_042")
assert q_sample is not None and q_sample["id"] == "zakovat_042"

rnd_all = get_random_zakovat_questions(10)
assert len(rnd_all) == 10

rnd_bb = get_random_zakovat_questions(5, category="black_box")
assert len(rnd_bb) == 5 and all(x["type"] == "black_box" for x in rnd_bb)

search_res = search_zakovat_by_alias("kompas")
assert len(search_res) > 0, "Failed to find 'kompas' by alias"

print("ALL 500 QUESTIONS STRICTLY VALIDATED AND BALANCED! ALL CHECKS PASSED!")
