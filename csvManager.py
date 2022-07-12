import csv


def getData(path, *keys):
    file = open(path, 'r', newline='')
    read = csv.DictReader(file, restval='')
    result = []
    if keys:
        keys = list(set(keys))
        read.fieldnames = [x.strip() for x in read.fieldnames]
        popData(keys, read.fieldnames)
        for row in read:
            dic = {}
            for key in keys:
                dic[key] = row[key]
            result.append(dic)
    else:
        for row in read:
            result.append(row)
    return result, read.fieldnames


def popData(keys, read):
    i = 0
    while i < len(keys):
        key = keys[i]
        if key in read:
            i += 1
        else:
            print(f"Attention, la clé {key} n'existe pas")
            keys.pop(i)
    return keys