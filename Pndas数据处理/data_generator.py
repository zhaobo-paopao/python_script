# 模拟实时数据生成
# data_generator.py
import json
import random
import time
from datetime import datetime

from kafka import KafkaProducer


class ClickStreamGenerator:
    """模拟电商点击流数据生成器"""

    def __init__(self, kafka_server="localhost:9092", topic="click-stream"):
        self.producer = KafkaProducer(
            bootstrap_servers=kafka_server,
            value_serializer=lambda v: json.dumps(v).encode("utf-8"),
        )
        self.topic = topic

        # 模拟数据
        self.users = [f"user_{i:03d}" for i in range(1, 101)]  # 100个用户
        self.products = [
            {
                "id": "P001",
                "name": "iPhone 15",
                "category": "Electronics",
                "price": 7999,
            },
            {"id": "P002", "name": "Laptop", "category": "Electronics", "price": 5999},
            {"id": "P003", "name": "T-Shirt", "category": "Clothing", "price": 199},
            {"id": "P004", "name": "Coffee Maker", "category": "Home", "price": 499},
            {"id": "P005", "name": "Book", "category": "Books", "price": 59},
        ]
        self.actions = ["view", "click", "add_to_cart", "purchase"]

    def generate_click_event(self):
        """生成单个点击事件"""
        user = random.choice(self.users)
        product = random.choice(self.products)
        action = random.choices(
            self.actions,
            weights=[0.5, 0.3, 0.15, 0.05],  # 不同行为的概率
        )[0]

        event = {
            "event_id": f"EV{int(time.time() * 1000)}",
            "user_id": user,
            "product_id": product["id"],
            "product_name": product["name"],
            "category": product["category"],
            "price": product["price"],
            "action": action,
            "timestamp": datetime.now().isoformat(),
            "session_id": f"SESS{random.randint(1000, 9999)}",
            "click_duration": random.uniform(0.5, 30.0),  # 停留时间(秒)
            "page_location": f"/product/{product['id']}",
        }
        return event

    def start_streaming(self, interval=0.1):
        """开始生成数据流"""
        print(f"开始生成点击流数据，频率: {1 / interval:.1f} 事件/秒")

        count = 0
        try:
            while True:
                event = self.generate_click_event()

                # 发送到Kafka
                self.producer.send(self.topic, event)

                count += 1
                if count % 100 == 0:
                    print(
                        f"已生成 {count} 个事件，最新事件: {event['user_id']} {event['action']} {event['product_name']}"
                    )

                time.sleep(interval)  # 控制生成速度

        except KeyboardInterrupt:
            print("\n停止数据生成")
        finally:
            self.producer.flush()
            self.producer.close()


# 运行数据生成器
if __name__ == "__main__":
    generator = ClickStreamGenerator()
    generator.start_streaming(interval=0.05)  # 每秒约20个事件
