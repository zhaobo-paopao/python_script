# import psycopg2

# try:
#     # 连接到PostgreSQL数据库
#     connection = psycopg2.connect(
#         database="postgres",  # 替换为你的数据库名称
#         user="postgres",           # 替换为你的数据库用户名
#         password="2008bjAY",       # 替换为你的数据库密码
#         host="127.0.0.1",               # 替换为你的数据库主机地址，默认是localhost
#         port="5432"                # 替换为你的数据库端口，默认是5432
#     )

#     # 创建一个cursor对象
#     cursor = connection.cursor()

#     # 执行SQL查询（例如，选择PostgreSQL版本）
#     #cursor.execute("SELECT version();")
#     cursor.execute(" select  * from father_table;")


#     # 获取查询结果
#     #db_version = cursor.fetchone()
#     db_result = cursor.fetchone()

#     #print("Connected to PostgreSQL version:", db_version)
#     print("表查询结果为:", db_result)


#     # 关闭cursor和connection
#     cursor.close()
#     connection.close()

# except (Exception, psycopg2.Error) as error:
#  print("Error while connecting to PostgreSQL", error)


import psycopg2

# 配置数据库连接参数
conn_params = {
    "dbname": "postgres",
    "user": "postgres",
    "password": "2008bjAY",
    "host": "127.0.0.1",
    "port": "5432",
}

# 连接到数据库
conn = psycopg2.connect(**conn_params)

# 创建一个游标对象
cur = conn.cursor()

# 编写SQL查询
sql = "SELECT * FROM father_table;"

# 执行SQL查询
cur.execute(sql)

# 获取查询结果
rows = cur.fetchall()

# 打印结果
for row in rows:
    print(row)

# 关闭游标和连接
cur.close()
conn.close()
