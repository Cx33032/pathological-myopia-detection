import json

# Reference output to the gradio
def load_reference_list(language):
    with open(f"./reference/reference_{language}.json", "r", encoding="utf-8") as f:
        refer_list = json.load(f)
    return refer_list

class Refer:
    def __init__(self, language):
        self.reference = load_reference_list(language)

    def __call__(self, key):
        return self.reference.get(key, key)
