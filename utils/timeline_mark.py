import json

t = ["3:8.1","3:8.9","3:9.7","3:10.5","3:11.3","3:12.2","3:12.9","3:13.8","3:14.6","3:15.3","3:17.5","3:18.3","3:19.2","3:19.9","3:20.7","3:22.3","3:22.9","3:23.6","3:24.4","3:25.2","3:26.1","3:27.0","3:27.8","3:28.8","3:29.7","3:30.5","3:31.3","3:32.1","3:32.8","3:33.7","3:34.6","3:35.4","3:36.3","3:37.0","3:37.8","3:38.7","3:39.6","3:40.5","3:41.3","3:42.1","3:42.9","3:43.8","3:44.5","3:45.4","3:46.2","3:47.1","3:47.8","3:48.6","3:49.4","3:50.2","3:51.1","3:52.0","3:52.8","3:53.6","3:54.5","3:55.3","3:56.0","3:56.8","3:57.7","3:58.6","3:59.3","4:0.2","4:1.1","4:1.9","4:2.7","4:3.7","4:4.5","4:5.2","4:6.1","4:7.0","4:7.9","4:8.7","4:9.7","4:10.5","4:11.3","4:12.1","4:13.1","4:13.9","4:14.9","4:15.6"]
with open("data/dictionarys/ㄇ.json", "r+", encoding="utf-8") as f:
    d = json.load(f)
    cnt = 0
    for word, time in d.items():
        d[word] = t[cnt]
        cnt += 1
    json.dump(d, f, ensure_ascii=False)
