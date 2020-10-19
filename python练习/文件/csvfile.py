test = """123.125.71.36 - - [06/Apr/2017:18:09:25 +0800] \
    "GET / HTTP/1.1" 200 8642 \
    "-" "Mozilla/5.0 (compatible; Baiduspider/2.0; +http://www.baidu.com/search/spider.html)"""""
def makekey(line:str, CHARS = set(""" []"'""")):
    start = 0
    length = len(test)
    for i, c in enumerate(test):
        if c in CHARS:
            if start == i:
                start = i +1
                continue
            yield test[start:i]
            start = i + 1
    else:
        if start < length:
            yield test[start:]
print(list(makekey(test)))