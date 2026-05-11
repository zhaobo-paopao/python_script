import pandas as pd
# 创建学生成绩表
students = pd.DataFrame({
    '学号': ['S001', 'S002', 'S003', 'S004', 'S005'],
    '姓名': ['小明', '小红', '小刚', '小丽', '小华'],
    '数学': [85, 92, 78, 88, 95],
    '英语': [90, 88, 85, 92, 89],
    '物理': [82, 90, 76, 85, 93]
})

# 计算总分和平均分
students['总分'] = students[['数学', '英语', '物理']].sum(axis=1)
students['平均分'] = students['总分'] / 3

# 排名
students['排名'] = students['总分'].rank(ascending=False, method='min').astype(int)

# 分析
print("平均分最高的学生:")
print(students.loc[students['平均分'].idxmax()])

print("\n各科平均分:")
print(students[['数学', '英语', '物理']].mean())

print("\n成绩单:")
print(students.sort_values('排名'))