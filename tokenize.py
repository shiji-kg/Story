import re
with open("verdict.txt", "r", encoding="utf-8") as f:
  raw_text = f.read()
print("Total number of characters:", len(raw_text))

preprocessed = re.split(r'([,.:;?_!"()\'|--|\s)',raw_text)
preprocessed = [item.strip() for item in preprocessed if item.strip()]
print(preprocessed[:30])
print(len(preprocessed))
