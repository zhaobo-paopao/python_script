import random
import time
from collections import defaultdict

# --------------- 1. 生成 100万行模拟数据 ---------------
words_pool = ["hadoop", "mapreduce", "spark", "flink", "data", "python", "java", "big", "ai"]
print("正在生成 100万行文本...")

start = time.time()
data = []
for _ in range(1000000):
    line = " ".join(random.choices(words_pool, k=random.randint(3, 8)))
    data.append(line)
print(f"生成完成，耗时 {time.time() - start:.2f}s\n")

# --------------- 2. Map 阶段：一行 → 多个 (word, 1) ---------------
def map_phase(lines):
    mapped = []
    for line in lines:
        for word in line.split():
            mapped.append((word, 1))
    return mapped

# --------------- 3. Shuffle 阶段：按 key 分组 ---------------
def shuffle_phase(mapped):
    grouped = defaultdict(list)
    for word, count in mapped:
        grouped[word].append(count)
    return grouped

# --------------- 4. Reduce 阶段：求和 ---------------
def reduce_phase(grouped):
    result = {}
    for word, counts in grouped.items():
        result[word] = sum(counts)
    return result

# --------------- 执行 ---------------
start = time.time()

mapped = map_phase(data)
grouped = shuffle_phase(mapped)
result = reduce_phase(grouped)

print("单词统计结果：")
for word, cnt in sorted(result.items(), key=lambda x: x[1], reverse=True):
    print(f"{word:12} {cnt}")

print(f"\n总耗时：{time.time() - start:.2f} 秒")