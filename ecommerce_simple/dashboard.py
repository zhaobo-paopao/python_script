# dashboard.py
import random
import threading
import time
from collections import defaultdict, deque
from datetime import datetime

from config import *
from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

# 存储实时数据
realtime_data = {
    "total_orders": 0,
    "total_revenue": 0,
    "recent_orders": deque(maxlen=20),
    "product_stats": defaultdict(int),
    "city_stats": defaultdict(int),
    "category_stats": defaultdict(int),
    "payment_stats": defaultdict(int),
    "status_stats": defaultdict(int),
    "update_time": datetime.now(),
}


def consume_kafka_simple():
    """简单的Kafka消费者（用于演示）"""
    print("启动Kafka消费者线程...")

    # 这里简化处理，实际应该用Kafka消费者
    # 为了演示，我们模拟消费数据
    while True:
        time.sleep(5)
        # 模拟数据更新
        realtime_data["total_orders"] += 1
        realtime_data["total_revenue"] += random.randint(100, 10000)
        realtime_data["update_time"] = datetime.now()


@app.route("/")
def index():
    """仪表盘主页"""
    html_template = """
    <!DOCTYPE html>
    <html>
    <head>
        <title>电商实时监控仪表盘</title>
        <meta charset="utf-8">
        <meta name="viewport" content="width=device-width, initial-scale=1">
        <style>
            * { margin: 0; padding: 0; box-sizing: border-box; }
            body { 
                font-family: 'Segoe UI', Arial, sans-serif; 
                background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                min-height: 100vh;
                padding: 20px;
                color: #333;
            }
            .container {
                max-width: 1400px;
                margin: 0 auto;
            }
            .header {
                text-align: center;
                color: white;
                margin-bottom: 30px;
                padding: 25px;
                background: rgba(255, 255, 255, 0.1);
                border-radius: 15px;
                backdrop-filter: blur(10px);
                box-shadow: 0 8px 32px rgba(0, 0, 0, 0.1);
            }
            .header h1 { 
                font-size: 2.8em; 
                margin-bottom: 10px;
                text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
            }
            .header p { 
                font-size: 1.2em; 
                opacity: 0.9;
            }
            .stats-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }
            .stat-card {
                background: white;
                padding: 25px;
                border-radius: 12px;
                box-shadow: 0 6px 20px rgba(0,0,0,0.1);
                transition: transform 0.3s ease, box-shadow 0.3s ease;
                display: flex;
                align-items: center;
                gap: 20px;
            }
            .stat-card:hover {
                transform: translateY(-5px);
                box-shadow: 0 12px 24px rgba(0,0,0,0.15);
            }
            .stat-icon {
                font-size: 2.5em;
                width: 70px;
                height: 70px;
                border-radius: 50%;
                display: flex;
                align-items: center;
                justify-content: center;
            }
            .stat-content {
                flex: 1;
            }
            .stat-label {
                color: #666;
                font-size: 1em;
                margin-bottom: 5px;
            }
            .stat-value {
                font-size: 2.2em;
                font-weight: bold;
                color: #2c3e50;
                margin: 5px 0;
            }
            .stat-change {
                font-size: 0.9em;
                color: #666;
            }
            .positive { color: #10b981; }
            .negative { color: #ef4444; }
            .charts-grid {
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(600px, 1fr));
                gap: 20px;
                margin-bottom: 30px;
            }
            .chart-card {
                background: white;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 6px 20px rgba(0,0,0,0.1);
            }
            .chart-card h3 {
                color: #333;
                margin-bottom: 20px;
                font-size: 1.4em;
                border-bottom: 2px solid #f0f0f0;
                padding-bottom: 10px;
            }
            .chart-container {
                height: 300px;
                width: 100%;
            }
            .table-container {
                background: white;
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 6px 20px rgba(0,0,0,0.1);
                margin-bottom: 30px;
            }
            table {
                width: 100%;
                border-collapse: collapse;
            }
            th, td {
                border: 1px solid #e0e0e0;
                padding: 12px 15px;
                text-align: left;
            }
            th {
                background-color: #f8f9fa;
                font-weight: 600;
                color: #495057;
            }
            tr:nth-child(even) {
                background-color: #f8f9fa;
            }
            tr:hover {
                background-color: #e9ecef;
            }
            .status-bar {
                display: flex;
                justify-content: space-between;
                align-items: center;
                background: rgba(255, 255, 255, 0.9);
                padding: 15px 25px;
                border-radius: 12px;
                margin-top: 20px;
            }
            .status-item {
                display: flex;
                align-items: center;
                gap: 10px;
            }
            .status-indicator {
                width: 12px;
                height: 12px;
                border-radius: 50%;
            }
            .status-good { background: #10b981; }
            .status-warning { background: #f59e0b; }
            .timestamp {
                color: #666;
                font-size: 0.9em;
            }
            @media (max-width: 768px) {
                .charts-grid {
                    grid-template-columns: 1fr;
                }
                .chart-card {
                    padding: 15px;
                }
            }
        </style>
    </head>
    <body>
        <div class="container">
            <div class="header">
                <h1>📊 电商实时监控仪表盘</h1>
                <p>实时监控订单、销售额、用户行为等关键指标</p>
            </div>
            
            <div class="stats-grid" id="stats-grid">
                <!-- 由JavaScript动态填充 -->
            </div>
            
            <div class="charts-grid">
                <div class="chart-card">
                    <h3>📈 实时销售额趋势</h3>
                    <div id="salesChart" class="chart-container"></div>
                </div>
                <div class="chart-card">
                    <h3>📊 产品类别分布</h3>
                    <div id="categoryChart" class="chart-container"></div>
                </div>
            </div>
            
            <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 20px;">
                <div class="table-container">
                    <h3>🏆 热销产品 Top 10</h3>
                    <table id="product-table">
                        <thead>
                            <tr><th>产品</th><th>销量</th><th>销售额</th></tr>
                        </thead>
                        <tbody></tbody>
                    </table>
                </div>
                <div class="table-container">
                    <h3>🌍 城市销售排名</h3>
                    <table id="city-table">
                        <thead>
                            <tr><th>城市</th><th>订单数</th><th>销售额</th></tr>
                        </thead>
                        <tbody></tbody>
                    </table>
                </div>
            </div>
            
            <div class="status-bar" id="status-bar">
                <!-- 状态信息由JavaScript动态更新 -->
            </div>
        </div>
        
        <script>
            // 初始化ECharts图表
            function initCharts() {
                // 销售额趋势图
                const salesChart = echarts.init(document.getElementById('salesChart'));
                salesChart.setOption({
                    title: { text: '最近1小时销售额', left: 'center' },
                    tooltip: { trigger: 'axis' },
                    xAxis: { type: 'category', data: [] },
                    yAxis: { type: 'value', name: '销售额(元)' },
                    series: [{ 
                        name: '销售额', 
                        type: 'line', 
                        data: [],
                        smooth: true,
                        areaStyle: { opacity: 0.3 },
                        lineStyle: { width: 3 }
                    }]
                });
                
                // 产品类别分布图
                const categoryChart = echarts.init(document.getElementById('categoryChart'));
                categoryChart.setOption({
                    title: { text: '产品类别分布', left: 'center' },
                    tooltip: { trigger: 'item', formatter: '{a} <br/>{b}: {c} ({d}%)' },
                    series: [{
                        name: '类别分布',
                        type: 'pie',
                        radius: ['40%', '70%'],
                        data: [],
                        emphasis: { itemStyle: { shadowBlur: 10, shadowOffsetX: 0, shadowColor: 'rgba(0, 0, 0, 0.5)' } }
                    }]
                });
                
                return { salesChart, categoryChart };
            }
            
            // 更新仪表盘数据
            function updateDashboard() {
                fetch('/api/metrics')
                    .then(response => response.json())
                    .then(data => {
                        // 更新统计卡片
                        document.getElementById('stats-grid').innerHTML = `
                            <div class="stat-card">
                                <div class="stat-icon" style="background: #e3f2fd; color: #1976d2;">💰</div>
                                <div class="stat-content">
                                    <div class="stat-label">总销售额</div>
                                    <div class="stat-value">¥${data.total_revenue.toLocaleString()}</div>
                                    <div class="stat-change positive">较昨日: +12.5%</div>
                                </div>
                            </div>
                            <div class="stat-card">
                                <div class="stat-icon" style="background: #f3e5f5; color: #7b1fa2;">📦</div>
                                <div class="stat-content">
                                    <div class="stat-label">总订单数</div>
                                    <div class="stat-value">${data.total_orders.toLocaleString()}</div>
                                    <div class="stat-change positive">较昨日: +8.3%</div>
                                </div>
                            </div>
                            <div class="stat-card">
                                <div class="stat-icon" style="background: #e8f5e8; color: #388e3c;">👥</div>
                                <div class="stat-content">
                                    <div class="stat-label">活跃客户</div>
                                    <div class="stat-value">${data.unique_customers || 85}</div>
                                    <div class="stat-change positive">较昨日: +5.2%</div>
                                </div>
                            </div>
                            <div class="stat-card">
                                <div class="stat-icon" style="background: #fff3e0; color: #f57c00;">📊</div>
                                <div class="stat-content">
                                    <div class="stat-label">客单价</div>
                                    <div class="stat-value">¥${data.avg_order_value || 256.8}</div>
                                    <div class="stat-change positive">较昨日: +3.7%</div>
                                </div>
                            </div>
                        `;
                        
                        // 更新状态栏
                        const now = new Date();
                        document.getElementById('status-bar').innerHTML = `
                            <div class="status-item">
                                <div class="status-indicator status-good"></div>
                                <span>系统状态: 运行正常</span>
                            </div>
                            <div class="status-item">
                                <div class="status-indicator status-good"></div>
                                <span>数据延迟: < 5秒</span>
                            </div>
                            <div class="status-item">
                                <div class="status-indicator status-good"></div>
                                <span>数据处理: 实时流</span>
                            </div>
                            <div class="timestamp">
                                最后更新: ${now.toLocaleTimeString()}
                            </div>
                        `;
                    });
            }
            
            // 页面加载完成后初始化
            window.onload = function() {
                // 加载ECharts
                const script = document.createElement('script');
                script.src = 'https://cdn.jsdelivr.net/npm/echarts@5.4.3/dist/echarts.min.js';
                script.onload = function() {
                    initCharts();
                    updateDashboard();
                    
                    // 每5秒更新一次
                    setInterval(updateDashboard, 5000);
                };
                document.head.appendChild(script);
            };
            
            // 窗口大小变化时重绘图表
            window.onresize = function() {
                if (typeof echarts !== 'undefined') {
                    Object.values(echarts.getInstance()).forEach(chart => chart.resize());
                }
            };
        </script>
    </body>
    </html>
    """
    return render_template_string(html_template)


@app.route("/api/metrics")
def get_metrics():
    """获取实时指标API"""
    return jsonify(
        {
            "total_orders": realtime_data["total_orders"],
            "total_revenue": realtime_data["total_revenue"],
            "avg_order_value": realtime_data["total_revenue"]
            / max(realtime_data["total_orders"], 1),
            "unique_customers": 85,  # 模拟数据
            "update_time": realtime_data["update_time"].isoformat(),
        }
    )


def start_dashboard():
    """启动Web仪表盘"""
    print("=" * 60)
    print("🌐 启动Web仪表盘...")
    print(f"访问地址: http://{WEB_HOST}:{WEB_PORT}")
    print("=" * 60)

    # 启动Kafka消费者线程
    kafka_thread = threading.Thread(target=consume_kafka_simple, daemon=True)
    kafka_thread.start()

    app.run(host=WEB_HOST, port=WEB_PORT, debug=False, use_reloader=False)


if __name__ == "__main__":
    start_dashboard()
