
import json
# value_serializer=lambda v: json.dumps(v).encode('utf-8')
# 这一行代码是一个Kafka生产者的序列化器，用于将Python对象转换为Kafka可以传输的字节流（bytes）。它完成了两个主要功能：
#   Python对象（字典/列表等） → JSON字符串 → UTF-8字节流 → Kafka消息
# json.dumps(v)
# 将Python对象转换为JSON字符串

'''
lambda 参数: 表达式
•
lambda：Python的匿名函数关键字
•
v：函数参数，代表要序列化的值
•
:：分隔符
•
json.dumps(v).encode('utf-8')：函数体，返回表达式的结果
'''
# python_dict={'user':'张三','age':'25'}
# json_string=json.dumps(python_dict)
# byte_data=json_string.encode('utf-8')
# serializer=lambda v: json.dumps(v).encode('utf-8')
#生产端序列化
event={'user_id':'user_001','action':'click','timestamp':'2024-11-15T10:30:00'}
v_event=lambda v_event: json.dumps(event).encode('utf-8')
text='你好'
byte_data=text.encode('utf-8')

# print(python_dict)
# print(json_string)
# print(byte_data)
# print(serializer(python_dict))
print(v_event(event))
print(byte_data)

# 消费端(反序列化)

# 接收到的字节数据
received_bytes = b'{"user_id": "user_001", "product": "iPhone 15", "price": 7999}'
# receiver_bates= b'{''user_id'':''user_001'',''product'':''iPhone'',''price'':7999}'
json_str=received_bytes.decode('utf-8')
event1=json.loads(json_str)
# 反序列化
received_str=lambda r: json.loads(r.decode('utf-8')) 
print(json_str)
print(event1)
print(received_str(received_bytes))


# 选项1：JSON（本代码使用）
value_serializer=lambda v: json.dumps(v).encode('utf-8')

# 选项2：Pickle（Python专用）
value_serializer=lambda v: pickle.dumps(v)

# 选项3：Avro/Protobuf（高性能）
value_serializer=lambda v: avro_serializer.serialize(v)

# 选项4：纯字符串
value_serializer=lambda v: str(v).encode('utf-8')






