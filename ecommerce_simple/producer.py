# producer.py
import json
import random
import time
from datetime import datetime

from config import *
from confluent_kafka import Producer


class OrderProducer:
    def __init__(self):
        """初始化Kafka生产者"""
        self.producer = Producer(
            {
                "bootstrap.servers": KAFKA_BRKOER,
                "client.id": "ecommerce-order-producer",
                "acks": "all",
                "retries": 3,
            }
        )
        self.order_id = 10000
        self.customers = [f"customer_{i:03d}" for i in range(1, 101)]

    def generate_order(self):
        """生成模拟订单数据"""
        self.order_id += 1
        customer = random.choice(self.customers)
        product = random.choice(PRODUCTS)
        price = random.randint(1000, 15000)
        quantity = random.randint(1, 3)
        total = price * quantity

        return {
            "order_id": self.order_id,
            "customer_id": customer,
            "product": product,
            "category": random.choice(CATEGORIES),
            "price": price,
            "quantity": quantity,
            "total_amount": total,
            "city": random.choice(CITIES),
            "payment_method": random.choice(["支付宝", "微信支付", "信用卡", "银联"]),
            "order_status": random.choice(["pending", "paid", "shipped", "completed"]),
            "order_time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "timestamp": int(time.time() * 1000),  # 毫秒时间戳
        }

    def delivery_report(self, err, msg):
        """消息发送回调"""
        if err:
            print(f"❌ 发送失败: {err}")
        else:
            print(
                f"✅ 发送成功: {msg.topic()}[{msg.partition()}] offset={msg.offset()}"
            )

    def start_producing(self, interval=2):
        """开始生产订单数据"""
        print("=" * 60)
        print("📦 电商订单数据生产者")
        print("=" * 60)
        print(f"Kafka服务器: {KAFKA_BRKOER}")
        print(f"主题: {KAFKA_TOPIC}")
        print(f"生成间隔: {interval}秒/条")
        print("按 Ctrl+C 停止生产")
        print("-" * 60)

        try:
            while True:
                # 生成订单
                order = self.generate_order()
                order_json = json.dumps(order, ensure_ascii=False)

                # 发送到Kafka
                self.producer.produce(
                    KAFKA_TOPIC,
                    key=str(order["order_id"]),  # 用order_id作为key保证顺序
                    value=order_json,
                    callback=self.delivery_report,
                )

                # 打印订单信息
                print(
                    f"[{order['order_time']}] #{order['order_id']} {order['customer_id']} 购买了 {order['product']} × {order['quantity']} = ¥{order['total_amount']}"
                )

                # 刷新并等待
                self.producer.poll(0)
                time.sleep(interval)

        except KeyboardInterrupt:
            print("\n🛑 停止生产者...")
        finally:
            # 确保所有消息都发送完成
            self.producer.flush()
            print("生产者已关闭")


if __name__ == "__main__":
    producer = OrderProducer()
    producer.start_producing(interval=3)  # 每3秒一条
