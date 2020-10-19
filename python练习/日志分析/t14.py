from pathlib import Path

def load(*paths,encoding='utf-8',ext=('*.log',)):
    for p in paths:
        path = Path(p)
        if path.is_dir():
            for e in ext:
                logs = path.glob(e) #匹配所有符合条件的文件，并将其以列表的形式返回
                #print(list(logs),'~~~~~~')
                for log in logs:
                    print(log)
                    with log.open(encoding=encoding) as f:
                        for line in f:
                            print(line)
        elif path.is_file():
            pass
print(load('.'))