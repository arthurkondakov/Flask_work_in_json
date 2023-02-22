import json

def data_candidates():
    with open ("candidates.json", "r", encoding='utf-8') as file:
        data = json.load(file)
        candidates = {}
        for i in data:
            candidates[i["id"]] = i
        return candidates
