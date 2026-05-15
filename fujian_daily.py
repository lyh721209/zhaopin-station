#!/usr/bin/env python3
"""
福建省每日校招情报推送脚本
聚焦：央国企、事业单位、大型上市公司、新特精企业
地区：福建省（厦门、福州、泉州为重点）
目标：2026届视觉传达设计专业本科应届生
推送时间：每天上午8点前
"""

import datetime
import random
import os
import json

# 福建省重点招聘企业岗位池（央国企/事业单位/上市公司/新特精）
FUJIAN_JOB_POOL = [
    # ===== 央国企 =====
    {"company": "福建广电网络集团", "position": "展馆设计/视觉传达设计", "city": "福州", "type": "国企", "salary": "面议", "deadline": "2026校招", "url": "https://www.zhaopin.com/zhaopin/ed390918e5dd4ede86a5608c22f1a462/", "source": "智联招聘", "highlight": "省属国企，展馆设计方向，编制机会"},
    {"company": "厦门银行", "position": "2026届春季校园招聘（品牌/设计方向）", "city": "厦门", "type": "国企", "salary": "面议", "deadline": "2026春招", "url": "https://www.nowcoder.com/discuss/591630986299858944", "source": "牛客网", "highlight": "国有股份制银行，厦门本地，福利完善"},
    {"company": "华润万家", "position": "UI设计管理培训生", "city": "厦门", "type": "央企", "salary": "面议", "deadline": "2026春招", "url": "https://www.wondercv.com/xiaozhao/china-resources-2026-spring-shenzhen-5994-04a2bc/", "source": "WonderCV", "highlight": "央企华润旗下，大型零售品牌体系"},
    {"company": "中国电信（厦门）", "position": "客户经营/视觉设计", "city": "厦门", "type": "央企", "salary": "面议", "deadline": "滚动", "url": "https://www.liepin.com/city-xiamen/", "source": "猎聘", "highlight": "央企背景，通信行业稳定"},
    {"company": "中国海峡人才市场", "position": "事业单位招聘综合服务", "city": "福州/厦门", "type": "事业单位", "salary": "面议", "deadline": "持续", "url": "https://www.hxrc.com/", "source": "海峡人才网", "highlight": "事业单位平台，福建招聘权威渠道"},
    
    # ===== 大型上市公司 =====
    {"company": "厦门飞鱼科技", "position": "UI设计（2026校招·游戏界面）", "city": "厦门", "type": "上市公司", "salary": "面议", "deadline": "2026校招", "url": "https://www.shushuqiuzhi.com/position/88872", "source": "智聘鼠", "highlight": "厦门知名游戏公司，UI/视觉方向"},
    {"company": "4399游戏", "position": "创意视觉设计师（校招）", "city": "厦门", "type": "上市公司", "salary": "面议", "deadline": "校招进行中", "url": "https://www.nowcoder.com/jobs/detail/406336", "source": "牛客网", "highlight": "网页游戏头部企业，创意视觉方向"},
    {"company": "厦门亿联网络", "position": "视觉设计师（校招）", "city": "厦门", "type": "上市公司", "salary": "15-30K/月", "deadline": "校招进行中", "url": "https://www.shushuqiuzhi.com/position/85727", "source": "智聘鼠", "highlight": "通信设备上市公司，视觉设计岗"},
    {"company": "宝宝巴士", "position": "资深平面设计师（实体产品）", "city": "福州", "type": "上市公司", "salary": "10-20K·13薪", "deadline": "经验不限", "url": "https://www.liepin.com/city-fuzhou/zpshejipingmianshejishi/", "source": "猎聘", "highlight": "C轮文创教育头部企业，产品平面设计"},
    {"company": "清源科技", "position": "平面设计师", "city": "厦门", "type": "上市公司", "salary": "7-10K", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "新能源上市公司，品牌设计方向"},
    {"company": "九牧王", "position": "平面设计师", "city": "厦门", "type": "上市公司", "salary": "12-15K·14薪", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "男装上市公司，品牌视觉体系"},
    {"company": "九牧厨卫", "position": "平面设计专员", "city": "厦门", "type": "上市公司", "salary": "8-13K", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "卫浴龙头上市公司，品牌设计"},
    
    # ===== 新特精/专精特新企业 =====
    {"company": "厦门斯巴特科技", "position": "高级平面设计师", "city": "厦门", "type": "专精特新", "salary": "15-25K·13薪", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "专精特新企业，贸易/进出口领域"},
    {"company": "和新科技", "position": "电商平面设计", "city": "厦门", "type": "专精特新", "salary": "8-12K·13薪", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "A轮科技企业，电商设计方向"},
    {"company": "厦门澜天电子", "position": "平面设计师", "city": "厦门", "type": "专精特新", "salary": "10-15K", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "电子科技领域，设计需求稳定"},
    {"company": "华稻夫数智咨询", "position": "平面设计&三维仿真顾问", "city": "厦门", "type": "专精特新", "salary": "10-15K·14薪", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "三维仿真+平面设计复合岗位"},
    {"company": "厦门赫彦网络", "position": "平面设计", "city": "厦门", "type": "专精特新", "salary": "10-18K", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "软件科技公司，设计岗薪资优"},
    {"company": "厦门万仟堂艺术品", "position": "资深平面设计师", "city": "厦门", "type": "专精特新", "salary": "10-15K", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "艺术品/工艺品领域，文创设计方向"},
    
    # ===== 福州/泉州本地企业 =====
    {"company": "福州久诚广告传媒", "position": "平面设计师（应届生/实习生）", "city": "福州", "type": "民企", "salary": "5-8K", "deadline": "经验不限", "url": "https://www.liepin.com/city-fuzhou/zpshejipingmianshejishi/", "source": "猎聘", "highlight": "广告传媒公司，接受应届生"},
    {"company": "福建乐达城轨传媒", "position": "平面设计师（校招）", "city": "福州", "type": "国企关联", "salary": "4-8K", "deadline": "2026校招", "url": "https://www.liepin.com/city-fuzhou/zpshejipingmianshejishi/", "source": "猎聘", "highlight": "城轨传媒领域，国企关联背景"},
    {"company": "红星中源集团", "position": "高级品牌视觉设计师（可远程）", "city": "福州", "type": "大型民企", "salary": "10-14K·13薪", "deadline": "2年以上", "url": "https://www.liepin.com/city-fuzhou/zpuisjsjs/", "source": "猎聘", "highlight": "5000-10000人大型集团，可远程办公"},
    {"company": "福州飞特瑞网络", "position": "跨境电商视觉设计师", "city": "福州", "type": "专精特新", "salary": "5-9K", "deadline": "1-3年", "url": "https://www.liepin.com/city-fuzhou/zpuisjsjs/", "source": "猎聘", "highlight": "跨境电商视觉，发展空间大"},
    {"company": "名游互动（福州）", "position": "游戏UI界面设计师", "city": "福州", "type": "专精特新", "salary": "7-9K", "deadline": "1-3年", "url": "https://www.liepin.com/city-fuzhou/zpuisjsjs/", "source": "猎聘", "highlight": "游戏公司，UI设计方向"},
    {"company": "福州礼好文化", "position": "视觉设计师", "city": "福州", "type": "文创", "salary": "10-15K", "deadline": "3-5年", "url": "https://www.liepin.com/city-fuzhou/zpuisjsjs/", "source": "猎聘", "highlight": "广播影视/文创领域"},
    {"company": "泉州市广播电视台", "position": "融媒体宣传设计实习生（可转正）", "city": "泉州", "type": "事业单位", "salary": "面议", "deadline": "滚动招聘", "url": "https://www.must.edu.mo/cecp/student", "source": "澳科大就业网", "highlight": "泉州本地，实习转正通道"},
    {"company": "泉州宣传部融媒体中心", "position": "宣传设计实习生", "city": "泉州", "type": "事业单位", "salary": "面议", "deadline": "滚动", "url": "https://www.must.edu.mo/cecp/student", "source": "澳科大就业网", "highlight": "政府宣传部门，积累经验"},
]

# 推荐搜索平台链接
SEARCH_LINKS = {
    "应届生求职网-福建": "https://www.yingjiesheng.com/",
    "智联招聘-福建": "https://www.zhaopin.com/fujian/",
    "猎聘-厦门": "https://www.liepin.com/city-xiamen/",
    "猎聘-福州": "https://www.liepin.com/city-fuzhou/",
    "牛客网校招": "https://www.nowcoder.com/jobs",
    "厦门人才网": "https://www.xmrc.com.cn/",
    "中国海峡人才网": "https://www.hxrc.com/",
    "福建国聘": "https://www.guopin.com/fujian/",
    "福建省事业单位公开招聘": "http://rst.fujian.gov.cn/zw/ztzl/zxzt/sydwrczp/",
    "大学生求职神器": "（微信小程序搜索）",
}

def generate_fujian_report():
    """生成福建省每日校招情报报告"""
    today = datetime.date.today()
    weekday = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"][today.weekday()]
    
    # 分类筛选
    state_owned = [j for j in FUJIAN_JOB_POOL if j["type"] in ["国企", "央企", "事业单位", "国企关联"]]
    listed = [j for j in FUJIAN_JOB_POOL if j["type"] == "上市公司"]
    xinte = [j for j in FUJIAN_JOB_POOL if j["type"] in ["专精特新", "文创"]]
    xiamen = [j for j in FUJIAN_JOB_POOL if j["city"] in ["厦门", "厦门/多城市", "福州/厦门"]]
    fuzhou = [j for j in FUJIAN_JOB_POOL if j["city"] in ["福州", "福州/厦门"]]
    quanzhou = [j for j in FUJIAN_JOB_POOL if j["city"] == "泉州"]
    
    report = f"""🎯 福建省校招情报 · 2026届视觉传达设计
📅 {today.strftime('%Y年%m月%d日')} {weekday} | ⏰ 每日8点前推送

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 重点地区：厦门 · 福州 · 泉州
🎓 目标人群：2026届视觉传达设计本科应届生
🏢 企业类型：央国企 | 事业单位 | 上市公司 | 新特精企业
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━

🏛️ 【央国企/事业单位】（{len(state_owned)}家）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for job in state_owned:
        report += f"""
▸ {job['company']}
  岗位：{job['position']}
  城市：{job['city']}  |  薪资：{job['salary']}  |  截止：{job['deadline']}
  亮点：{job['highlight']}
  投递：{job['url']}
  来源：{job['source']}
"""
    
    report += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📈 【大型上市公司】（{len(listed)}家）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for job in listed:
        report += f"""
▸ {job['company']}
  岗位：{job['position']}
  城市：{job['city']}  |  薪资：{job['salary']}  |  截止：{job['deadline']}
  亮点：{job['highlight']}
  投递：{job['url']}
  来源：{job['source']}
"""
    
    report += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔬 【新特精/专精特新企业】（{len(xinte)}家）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for job in xinte:
        report += f"""
▸ {job['company']}
  岗位：{job['position']}
  城市：{job['city']}  |  薪资：{job['salary']}  |  截止：{job['deadline']}
  亮点：{job['highlight']}
  投递：{job['url']}
  来源：{job['source']}
"""
    
    report += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌊 【厦门专场】（{len(xiamen)}家）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for job in xiamen:
        report += f"• {job['company']} · {job['position']} · {job['salary']}\n"
    
    report += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏛️ 【福州专场】（{len(fuzhou)}家）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for job in fuzhou:
        report += f"• {job['company']} · {job['position']} · {job['salary']}\n"
    
    report += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏘️ 【泉州专场】（{len(quanzhou)}家）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for job in quanzhou:
        report += f"• {job['company']} · {job['position']} · {job['salary']}\n"
    
    report += """
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🔍 【推荐搜索平台】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for name, url in SEARCH_LINKS.items():
        report += f"• {name}：{url}\n"
    
    # 求职提示
    tips = [
        "央国企/事业单位岗位：关注福建省人社厅官网 rst.fujian.gov.cn 的招聘公告",
        "厦门地区重点：厦门人才网 xmrc.com.cn 每周更新事业单位和国企岗位",
        "福州地区重点：中国海峡人才网 hxrc.com 是福建权威招聘平台",
        "上市公司校招：优先关注牛客网和WonderCV的校招日历",
        "专精特新企业：猎聘网筛选'高新技术企业'标签",
        "简历命名格式：姓名_澳科大_视觉传达_应聘岗位.pdf",
        "福建国企普遍要求：本科学历+作品集+面试",
        "泉州本地机会：关注泉州市人社局和澳科大就业网联动岗位",
    ]
    
    report += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
💡 【今日求职提示】
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
{random.choice(tips)}

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⚠️ 声明：以上信息仅供参考，请以企业官方招聘公告为准。
📊 数据来源：智联招聘、猎聘、牛客网、应届生求职网、厦门人才网、海峡人才网
🔄 更新时间：每天上午8:00前自动推送
"""
    return report

def save_fujian_report():
    """保存报告到文件"""
    report = generate_fujian_report()
    today_str = datetime.date.today().strftime("%Y%m%d")
    
    report_dir = "/root/.openclaw/workspace/校招情报站/reports"
    os.makedirs(report_dir, exist_ok=True)
    
    # 每日存档
    filepath = os.path.join(report_dir, f"fujian_report_{today_str}.txt")
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(report)
    
    # 最新报告
    latest_path = os.path.join(report_dir, "fujian_latest.txt")
    with open(latest_path, "w", encoding="utf-8") as f:
        f.write(report)
    
    # 同时更新到HTML网页的福建板块（简化版JSON数据）
    json_path = os.path.join(report_dir, "fujian_jobs.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "date": today_str,
            "update_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "jobs": FUJIAN_JOB_POOL,
            "summary": {
                "state_owned": len([j for j in FUJIAN_JOB_POOL if j["type"] in ["国企", "央企", "事业单位", "国企关联"]]),
                "listed": len([j for j in FUJIAN_JOB_POOL if j["type"] == "上市公司"]),
                "xinte": len([j for j in FUJIAN_JOB_POOL if j["type"] in ["专精特新", "文创"]]),
                "xiamen": len([j for j in FUJIAN_JOB_POOL if "厦门" in j["city"]]),
                "fuzhou": len([j for j in FUJIAN_JOB_POOL if "福州" in j["city"]]),
                "quanzhou": len([j for j in FUJIAN_JOB_POOL if j["city"] == "泉州"]),
            }
        }, f, ensure_ascii=False, indent=2)
    
    print(f"福建省报告已保存: {filepath}")
    print(f"JSON数据已更新: {json_path}")
    return report

if __name__ == "__main__":
    report = save_fujian_report()
    print("\n" + "="*60)
    print(report)
    print("="*60)
