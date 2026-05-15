#!/usr/bin/env python3
"""
每日校招情报推送脚本
为澳门科技大学视觉传达设计2026届应届生推送校园招聘信息
"""

import json
import datetime
import random
import os

# 预设的校招岗位池（模拟实时数据，实际运行时可以通过搜索API更新）
JOB_POOL = [
    {"company": "韶音科技", "position": "视觉设计管培生", "city": "深圳", "salary": "面议", "deadline": "2026-05-04", "url": "https://www.wondercv.com/xiaozhao/shokz-2026-spring-shenzhen-overseas-8359-8aad6b/", "type": "visual", "highlight": "全球运动耳机第一品牌，海外市场"},
    {"company": "诗悦网络", "position": "平面设计 / UI设计", "city": "广州", "salary": "面议", "deadline": "招满即止", "url": "https://www.wondercv.com/xiaozhao/shiyue-network-2026-spring-guangzhou-8810-077eda/", "type": "graphic", "highlight": "游戏大厂，美术设计类多岗位"},
    {"company": "蕉内", "position": "品牌视觉设计师", "city": "上海", "salary": "面议", "deadline": "招满即止", "url": "https://lsdjyw.lnnu.edu.cn/job/view/id/1213747", "type": "brand", "highlight": "新锐服装品牌，视觉传达/服装设计"},
    {"company": "得力集团", "position": "设计管培生", "city": "宁波", "salary": "面议", "deadline": "持续招聘", "url": "https://my.yingjiesheng.com/xjh-006-242-041.html", "type": "brand", "highlight": "国家级工业设计中心，多设计方向"},
    {"company": "千里目教育", "position": "平面设计岗", "city": "未注明", "salary": "8K-13K/月", "deadline": "滚动招聘", "url": "https://jdjyw.jlu.edu.cn/mportal/recruit/details?id=680d1ecc74254ea58d618857c382a3ce", "type": "graphic", "highlight": "品牌视觉体系构建，高薪+年终奖"},
    {"company": "瑞幸咖啡", "position": "AI设计师", "city": "北京", "salary": "面议", "deadline": "尽快投递", "url": "https://m.yingjiesheng.com/h.php?word=视觉传达设计", "type": "brand", "highlight": "咖啡连锁头部品牌，AI辅助设计方向"},
    {"company": "上海禾赛智能", "position": "平面设计师", "city": "上海", "salary": "面议", "deadline": "尽快投递", "url": "https://m.yingjiesheng.com/h.php?word=视觉传达设计", "type": "graphic", "highlight": "激光雷达科技公司，品牌/展会设计"},
    {"company": "深圳酷阳电子", "position": "视觉设计师", "city": "深圳", "salary": "面议", "deadline": "尽快投递", "url": "https://m.yingjiesheng.com/h.php?word=视觉传达设计", "type": "visual", "highlight": "跨境电商视觉设计"},
    {"company": "雷士照明", "position": "研发方向-工业设计", "city": "惠州", "salary": "面议", "deadline": "青苗计划", "url": "https://m.bysjy.com.cn/student/chance/onlinerecruitmentdetail.html?token=yxqqnn2600000011&type=0&recruitment_id=3503848", "type": "brand", "highlight": "青苗计划，面向未来3-5年人才储备"},
    {"company": "飞亚达", "position": "产品设计师", "city": "深圳", "salary": "面议", "deadline": "持续", "url": "https://cug.91wllm.cn/campus/view/id/995051", "type": "brand", "highlight": "国有控股上市公司，工业设计方向"},
    {"company": "华与华", "position": "品牌设计/文案创意", "city": "上海", "salary": "面议", "deadline": "已截止", "url": "https://www.nowcoder.com/enterprise/31834?pageSource=5014&channel=recruitmentSchedule", "type": "brand", "highlight": "顶尖战略营销咨询公司，超级符号方法论"},
    {"company": "洲明科技", "position": "品牌营销/工业设计", "city": "深圳/澳门", "salary": "面议", "deadline": "滚动", "url": "https://unilumin.zhiye.com/Campus", "type": "brand", "highlight": "LED显示屏全球第一，澳门有岗"},
    {"company": "杭州千艺文化", "position": "品牌设计/平面设计", "city": "杭州", "salary": "面议", "deadline": "滚动", "url": "https://m.yingjiesheng.com/h.php?word=视觉传达设计", "type": "brand", "highlight": "文创产业发达"},
    {"company": "武汉智能硬件", "position": "包装设计师", "city": "武汉", "salary": "面议", "deadline": "2026-06-30", "url": "https://www.nowcoder.com/jobs/detail/444336", "type": "package", "highlight": "需作品集，插画+三维造型能力"},
    {"company": "博琭教育", "position": "设计实习生", "city": "上海", "salary": "面议", "deadline": "滚动", "url": "https://m.yingjiesheng.com/h.php?word=视觉传达设计", "type": "graphic", "highlight": "实习可转正，互联网教育"},
    {"company": "瀛海文化", "position": "设计师", "city": "澳门", "salary": "面议", "deadline": "全职", "url": "https://www.must.edu.mo/cecp/student", "type": "graphic", "highlight": "澳门本地，文化公司"},
    {"company": "广东融泰药业", "position": "电商视觉设计实习生", "city": "广州", "salary": "面议", "deadline": "滚动", "url": "https://m.yingjiesheng.com/h.php?word=视觉传达设计", "type": "visual", "highlight": "电商设计方向"},
    {"company": "珠海格力", "position": "工业设计/平面设计", "city": "珠海", "salary": "面议", "deadline": "秋招", "url": "https://www.must.edu.mo/cecp/student", "type": "brand", "highlight": "珠海，世界500强"},
]

def generate_daily_report():
    """生成每日校招情报推送"""
    today = datetime.date.today()
    weekday = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"][today.weekday()]
    
    # 随机选择6个岗位作为今日推荐（实际应基于截止时间排序）
    selected = random.sample(JOB_POOL, min(6, len(JOB_POOL)))
    
    # 筛选出大湾区岗位
    gbay_jobs = [j for j in JOB_POOL if j["city"] in ["深圳", "广州", "珠海", "惠州", "东莞", "佛山", "中山", "澳门", "深圳/澳门", "上海/安徽"]]
    
    # 筛选即将截止的岗位
    urgent_jobs = [j for j in JOB_POOL if j["deadline"] not in ["招满即止", "滚动招聘", "持续", "持续招聘", "全职", "秋招", "青苗计划", "已截止"]]
    
    report = f"""🎓 澳科大视传2026届 · 每日校招情报
📅 {today.strftime('%Y年%m月%d日')} {weekday}

━━━━━━━━━━━━━━━━━━━━━━
🔥 今日推荐（{len(selected)}个精选岗位）
"""
    for i, job in enumerate(selected, 1):
        report += f"""
{i}. 【{job['company']}】{job['position']}
   📍 {job['city']}  |  💰 {job['salary']}  |  ⏰ {job['deadline']}
   💡 {job['highlight']}
   👉 {job['url']}
"""
    
    report += f"""
━━━━━━━━━━━━━━━━━━━━━━
🌉 大湾区专场（{len(gbay_jobs)}家企业）
"""
    for job in gbay_jobs[:5]:
        report += f"• {job['company']} · {job['position']} · {job['city']}\n"
    
    if urgent_jobs:
        report += f"""
━━━━━━━━━━━━━━━━━━━━━━
⏰ 截止提醒（{len(urgent_jobs)}个）
"""
        for job in urgent_jobs:
            report += f"• {job['company']} · 截止 {job['deadline']}\n"
    
    report += """
━━━━━━━━━━━━━━━━━━━━━━
💡 今日求职提示
"""
    tips = [
        "简历文件名格式：姓名_学校_岗位_作品集.pdf",
        "作品集首屏放最强项目，控制在20页以内",
        "投递前确认毕业时间符合要求（2025.9-2026.7）",
        "设计岗务必附作品集链接或附件",
        "关注企业公众号获取校招最新动态",
        "港澳学生可关注横琴粤澳合作区岗位",
    ]
    report += random.choice(tips)
    
    report += """
━━━━━━━━━━━━━━━━━━━━━━
📬 投递平台推荐
① 应届生求职网 yingjiesheng.com
② 牛客网 nowcoder.com
③ 智联招聘 zhaopin.com
④ 猎聘 liepin.com
⑤ 澳科大就业网 must.edu.mo/cecp/student

📊 数据仅供参考，请以企业官网为准
💻 完整岗位列表：https://校招情报站（本地网站）
"""
    return report

def save_report():
    """保存报告到文件"""
    report = generate_daily_report()
    today_str = datetime.date.today().strftime("%Y%m%d")
    
    # 保存到文件
    report_dir = "/root/.openclaw/workspace/校招情报站/reports"
    os.makedirs(report_dir, exist_ok=True)
    
    filepath = os.path.join(report_dir, f"report_{today_str}.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report)
    
    # 同时保存为最新报告
    latest_path = os.path.join(report_dir, "latest.txt")
    with open(latest_path, "w", encoding="utf-8") as f:
        f.write(report)
    
    print(f"报告已保存: {filepath}")
    return report

if __name__ == "__main__":
    report = save_report()
    print("\n" + "="*50)
    print(report)
    print("="*50)
