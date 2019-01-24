ns = globals()

with open(".env", "r", encoding="UTF-8") as f:
    for i in f:
        key, value = i.rstrip().split("=", 1)
        ns[key.upper()] = value
