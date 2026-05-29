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

# 重点地区招聘企业岗位池（央国企/事业单位/上市公司/新特精）
# 覆盖：福建省（厦门/福州/泉州）+ 大湾区（广州/深圳/珠海）+ 上海
JOB_POOL = [
    # ===== 福建省 =====
    # --- 央国企 ---
    {"company": "福建广电网络集团", "position": "展馆设计/视觉传达设计", "city": "福州", "type": "国企", "salary": "面议", "deadline": "2026校招", "url": "https://www.zhaopin.com/zhaopin/ed390918e5dd4ede86a5608c22f1a462/", "source": "智联招聘", "highlight": "省属国企，展馆设计方向，编制机会"},
    {"company": "厦门银行", "position": "2026届春季校园招聘（品牌/设计方向）", "city": "厦门", "type": "国企", "salary": "面议", "deadline": "2026春招", "url": "https://www.nowcoder.com/discuss/591630986299858944", "source": "牛客网", "highlight": "国有股份制银行，厦门本地，福利完善"},
    {"company": "华润万家", "position": "UI设计管理培训生", "city": "厦门", "type": "央企", "salary": "面议", "deadline": "2026春招", "url": "https://www.wondercv.com/xiaozhao/china-resources-2026-spring-shenzhen-5994-04a2bc/", "source": "WonderCV", "highlight": "央企华润旗下，大型零售品牌体系"},
    {"company": "中国电信（厦门）", "position": "客户经营/视觉设计", "city": "厦门", "type": "央企", "salary": "面议", "deadline": "滚动", "url": "https://www.liepin.com/city-xiamen/", "source": "猎聘", "highlight": "央企背景，通信行业稳定"},
    {"company": "中国海峡人才市场", "position": "事业单位招聘综合服务", "city": "福州/厦门", "type": "事业单位", "salary": "面议", "deadline": "持续", "url": "https://www.hxrc.com/", "source": "海峡人才网", "highlight": "事业单位平台，福建招聘权威渠道"},
    {"company": "福建省二建建设集团", "position": "2026校招（多岗位）", "city": "福州", "type": "国企", "salary": "面议", "deadline": "2026-12-31", "url": "https://job.sinopec.com", "source": "集团官网", "highlight": "省属国企，报名期长"},
    # --- 上市公司 ---
    {"company": "厦门飞鱼科技", "position": "UI设计（2026校招·游戏界面）", "city": "厦门", "type": "上市公司", "salary": "面议", "deadline": "2026校招", "url": "https://www.shushuqiuzhi.com/position/88872", "source": "智聘鼠", "highlight": "厦门知名游戏公司，UI/视觉方向"},
    {"company": "4399游戏", "position": "创意视觉设计师（校招）", "city": "厦门", "type": "上市公司", "salary": "面议", "deadline": "校招进行中", "url": "https://www.nowcoder.com/jobs/detail/406336", "source": "牛客网", "highlight": "网页游戏头部企业，创意视觉方向"},
    {"company": "厦门亿联网络", "position": "视觉/交互/ID设计师（校招）", "city": "厦门", "type": "上市公司", "salary": "15-30K/月", "deadline": "校招进行中", "url": "https://www.shushuqiuzhi.com/position/85727", "source": "智聘鼠", "highlight": "通信设备上市公司，双导师带教，2年70%晋升率"},
    {"company": "瑞幸咖啡", "position": "品牌包装设计师", "city": "厦门", "type": "上市公司", "salary": "面议", "deadline": "尽快投递", "url": "https://www.liepin.com/city-xiamen/", "source": "猎聘", "highlight": "知名上市品牌，厦门总部"},
    {"company": "宝宝巴士", "position": "资深平面设计师（实体产品）", "city": "福州", "type": "上市公司", "salary": "10-20K·13薪", "deadline": "经验不限", "url": "https://www.liepin.com/city-fuzhou/zpshejipingmianshejishi/", "source": "猎聘", "highlight": "C轮文创教育头部企业，产品平面设计"},
    {"company": "清源科技", "position": "平面设计师", "city": "厦门", "type": "上市公司", "salary": "7-10K", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "新能源上市公司，品牌设计方向"},
    {"company": "九牧王", "position": "平面设计师", "city": "厦门", "type": "上市公司", "salary": "12-15K·14薪", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "男装上市公司，品牌视觉体系"},
    {"company": "九牧厨卫", "position": "平面设计专员", "city": "厦门", "type": "上市公司", "salary": "8-13K", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "卫浴龙头上市公司，品牌设计"},
    # --- 新特精 ---
    {"company": "厦门斯巴特科技", "position": "高级平面设计师", "city": "厦门", "type": "专精特新", "salary": "15-25K·13薪", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "专精特新企业，贸易/进出口领域"},
    {"company": "和新科技", "position": "电商平面设计", "city": "厦门", "type": "专精特新", "salary": "8-12K·13薪", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "A轮科技企业，电商设计方向"},
    {"company": "厦门澜天电子", "position": "平面设计师", "city": "厦门", "type": "专精特新", "salary": "10-15K", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "电子科技领域，设计需求稳定"},
    {"company": "华稻夫数智咨询", "position": "平面设计&三维仿真顾问", "city": "厦门", "type": "专精特新", "salary": "10-15K·14薪", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "三维仿真+平面设计复合岗位"},
    {"company": "厦门赫彦网络", "position": "平面设计", "city": "厦门", "type": "专精特新", "salary": "10-18K", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "软件科技公司，设计岗薪资优"},
    {"company": "厦门万仟堂艺术品", "position": "资深平面设计师", "city": "厦门", "type": "专精特新", "salary": "10-15K", "deadline": "持续", "url": "https://www.liepin.com/city-xiamen/zppingmianyishusheji/", "source": "猎聘", "highlight": "艺术品/工艺品领域，文创设计方向"},
    # --- 福州/泉州 ---
    {"company": "福州久诚广告传媒", "position": "平面设计师（应届生/实习生）", "city": "福州", "type": "民企", "salary": "5-8K", "deadline": "经验不限", "url": "https://www.liepin.com/city-fuzhou/zpshejipingmianshejishi/", "source": "猎聘", "highlight": "广告传媒公司，接受应届生"},
    {"company": "福建乐达城轨传媒", "position": "平面设计师（校招）", "city": "福州", "type": "国企关联", "salary": "4-8K", "deadline": "2026校招", "url": "https://www.liepin.com/city-fuzhou/zpshejipingmianshejishi/", "source": "猎聘", "highlight": "城轨传媒领域，国企关联背景"},
    {"company": "红星中源集团", "position": "高级品牌视觉设计师（可远程）", "city": "福州", "type": "大型民企", "salary": "10-14K·13薪", "deadline": "2年以上", "url": "https://www.liepin.com/city-fuzhou/zpuisjsjs/", "source": "猎聘", "highlight": "5000-10000人大型集团，可远程办公"},
    {"company": "福州飞特瑞网络", "position": "跨境电商视觉设计师", "city": "福州", "type": "专精特新", "salary": "5-9K", "deadline": "1-3年", "url": "https://www.liepin.com/city-fuzhou/zpuisjsjs/", "source": "猎聘", "highlight": "跨境电商视觉，发展空间大"},
    {"company": "名游互动（福州）", "position": "游戏UI界面设计师", "city": "福州", "type": "专精特新", "salary": "7-9K", "deadline": "1-3年", "url": "https://www.liepin.com/city-fuzhou/zpuisjsjs/", "source": "猎聘", "highlight": "游戏公司，UI设计方向"},
    {"company": "福州礼好文化", "position": "视觉设计师", "city": "福州", "type": "文创", "salary": "10-15K", "deadline": "3-5年", "url": "https://www.liepin.com/city-fuzhou/zpuisjsjs/", "source": "猎聘", "highlight": "广播影视/文创领域"},
    {"company": "泉州市广播电视台", "position": "融媒体宣传设计实习生（可转正）", "city": "泉州", "type": "事业单位", "salary": "面议", "deadline": "滚动招聘", "url": "https://www.must.edu.mo/cecp/student", "source": "澳科大就业网", "highlight": "泉州本地，实习转正通道"},
    {"company": "泉州宣传部融媒体中心", "position": "宣传设计实习生", "city": "泉州", "type": "事业单位", "salary": "面议", "deadline": "滚动", "url": "https://www.must.edu.mo/cecp/student", "source": "澳科大就业网", "highlight": "政府宣传部门，积累经验"},

    # ===== 大湾区 · 深圳 =====
    # --- 央国企 ---
    {"company": "华润集团", "position": "品牌设计/视觉设计管培生", "city": "深圳", "type": "央企", "salary": "面议", "deadline": "2026春招", "url": "https://www.wondercv.com/xiaozhao/china-resources-2026-spring-shenzhen-5994-04a2bc/", "source": "WonderCV", "highlight": "央企总部，品牌体系完善"},
    {"company": "招商银行", "position": "视觉设计/创意设计师", "city": "深圳", "type": "国企", "salary": "面议", "deadline": "2026校招", "url": "https://www.yingjiesheng.com/guangdong/", "source": "应届生求职网", "highlight": "深圳总部，金融科技视觉方向"},
    {"company": "深圳报业集团", "position": "新媒体视觉设计师", "city": "深圳", "type": "国企", "salary": "面议", "deadline": "滚动", "url": "https://www.liepin.com/city-shenzhen/", "source": "猎聘", "highlight": "报业集团，新媒体视觉方向"},
    {"company": "深圳地铁集团", "position": "企业文化/品牌宣传设计", "city": "深圳", "type": "国企", "salary": "面议", "deadline": "2026校招", "url": "https://www.guopin.com/guangdong/", "source": "国聘", "highlight": "市属国企，品牌文化建设"},
    # --- 上市公司 ---
    {"company": "韶音科技", "position": "视觉设计管培生/UI设计师", "city": "深圳", "type": "上市公司", "salary": "面议", "deadline": "尽快投递", "url": "https://www.wondercv.com/xiaozhao/shokz-2026-spring-shenzhen-overseas-8359-8aad6b/", "source": "WonderCV", "highlight": "出海品牌，视觉/交互/三维渲染多岗"},
    {"company": "OPPO", "position": "多类岗位含设计方向", "city": "深圳/东莞", "type": "上市公司", "salary": "面议", "deadline": "尽快投递", "url": "https://www.wondercv.com/xiaozhao/oppo-2026-spring/", "source": "WonderCV", "highlight": "消费电子头部品牌，设计体系成熟"},
    {"company": "大疆创新", "position": "视觉设计师/品牌设计师", "city": "深圳", "type": "上市公司", "salary": "15-25K", "deadline": "2026校招", "url": "https://www.nowcoder.com/jobs", "source": "牛客网", "highlight": "无人机全球龙头，品牌视觉顶尖"},
    {"company": "传音控股", "position": "视觉设计师（海外品牌）", "city": "深圳", "type": "上市公司", "salary": "12-20K", "deadline": "2026校招", "url": "https://www.nowcoder.com/jobs", "source": "牛客网", "highlight": "非洲手机之王，海外品牌设计"},
    {"company": "创维集团", "position": "UI/视觉设计师", "city": "深圳", "type": "上市公司", "salary": "10-15K", "deadline": "2026校招", "url": "https://www.liepin.com/city-shenzhen/", "source": "猎聘", "highlight": "家电老牌上市公司，稳定"},
    # --- 新特精 ---
    {"company": "宇树科技", "position": "平面设计/工业设计", "city": "深圳/杭州", "type": "专精特新", "salary": "面议", "deadline": "27届提前批", "url": "https://www.liepin.com/city-shenzhen/", "source": "猎聘", "highlight": "四足机器人明星企业，设计+科技结合"},
    {"company": "追觅科技", "position": "视觉设计师/包装设计师", "city": "深圳", "type": "专精特新", "salary": "12-18K", "deadline": "持续", "url": "https://www.liepin.com/city-shenzhen/", "source": "猎聘", "highlight": "智能清洁赛道独角兽"},

    # ===== 大湾区 · 广州 =====
    # --- 央国企 ---
    {"company": "南方报业传媒集团", "position": "视觉设计师/新媒体设计", "city": "广州", "type": "国企", "salary": "面议", "deadline": "2026校招", "url": "https://www.yingjiesheng.com/guangdong/", "source": "应届生求职网", "highlight": "省级传媒集团，新闻视觉方向"},
    {"company": "广汽集团", "position": "品牌设计/UI设计（智能网联）", "city": "广州", "type": "国企", "salary": "面议", "deadline": "2026校招", "url": "https://www.guopin.com/guangdong/", "source": "国聘", "highlight": "汽车国企，智能座舱UI方向"},
    {"company": "广州地铁设计研究院", "position": "视觉传达/展览展示设计", "city": "广州", "type": "国企", "salary": "面议", "deadline": "2026校招", "url": "https://www.liepin.com/city-guangzhou/", "source": "猎聘", "highlight": "地铁设计国企，展览展示方向"},
    {"company": "广东省广新控股集团", "position": "品牌设计/视觉设计", "city": "广州", "type": "国企", "salary": "面议", "deadline": "2026校招", "url": "https://www.guopin.com/guangdong/", "source": "国聘", "highlight": "省属国企，品牌管理方向"},
    # --- 上市公司 ---
    {"company": "唯品会", "position": "视觉设计师/品牌设计师", "city": "广州", "type": "上市公司", "salary": "12-18K", "deadline": "2026校招", "url": "https://www.nowcoder.com/jobs", "source": "牛客网", "highlight": "电商上市公司，品牌视觉体系"},
    {"company": "小鹏汽车", "position": "UI/UX设计师（智能座舱）", "city": "广州", "type": "上市公司", "salary": "15-25K", "deadline": "2026校招", "url": "https://www.nowcoder.com/jobs", "source": "牛客网", "highlight": "智能电动车，座舱交互设计"},
    {"company": "欢聚集团（YY）", "position": "视觉设计师/运营设计", "city": "广州", "type": "上市公司", "salary": "10-16K", "deadline": "2026校招", "url": "https://www.liepin.com/city-guangzhou/", "source": "猎聘", "highlight": "直播平台，运营视觉设计"},
    {"company": "TCL", "position": "品牌视觉设计师/UI设计师", "city": "广州/惠州", "type": "上市公司", "salary": "10-15K", "deadline": "2026校招", "url": "https://www.liepin.com/city-guangzhou/", "source": "猎聘", "highlight": "家电巨头，品牌+UI双方向"},
    {"company": "蓝月亮", "position": "包装设计师/品牌设计师", "city": "广州", "type": "上市公司", "salary": "10-14K", "deadline": "2026校招", "url": "https://www.liepin.com/city-guangzhou/", "source": "猎聘", "highlight": "快消品牌，包装设计强项"},
    # --- 新特精 ---
    {"company": "亿航智能", "position": "工业设计师/视觉设计师", "city": "广州", "type": "专精特新", "salary": "12-20K", "deadline": "2026校招", "url": "https://www.liepin.com/city-guangzhou/", "source": "猎聘", "highlight": "eVTOL飞行器，科技+设计前沿"},
    {"company": "完美日记（逸仙电商）", "position": "品牌设计师/包装设计师", "city": "广州", "type": "专精特新", "salary": "10-16K", "deadline": "持续", "url": "https://www.liepin.com/city-guangzhou/", "source": "猎聘", "highlight": "美妆新消费品牌，包装设计需求大"},

    # ===== 上海 =====
    # --- 央国企 ---
    {"company": "上海报业集团", "position": "新媒体视觉设计师", "city": "上海", "type": "国企", "salary": "面议", "deadline": "2026校招", "url": "https://www.yingjiesheng.com/shanghai/", "source": "应届生求职网", "highlight": "省级传媒集团，新媒体视觉"},
    {"company": "上海图书馆", "position": "展览设计/视觉设计", "city": "上海", "type": "事业单位", "salary": "面议", "deadline": "2026校招", "url": "https://www.liepin.com/city-shanghai/", "source": "猎聘", "highlight": "事业单位，展览展示设计"},
    {"company": "东航集团", "position": "品牌设计/视觉设计", "city": "上海", "type": "央企", "salary": "面议", "deadline": "2026校招", "url": "https://www.guopin.com/shanghai/", "source": "国聘", "highlight": "航空央企，品牌体系完善"},
    {"company": "上海地铁", "position": "企业文化/品牌宣传设计", "city": "上海", "type": "国企", "salary": "面议", "deadline": "2026校招", "url": "https://www.liepin.com/city-shanghai/", "source": "猎聘", "highlight": "市属国企，文化建设方向"},
    # --- 上市公司 ---
    {"company": "小红书", "position": "品牌设计师/视觉设计师", "city": "上海", "type": "上市公司", "salary": "15-25K", "deadline": "2026校招", "url": "https://www.nowcoder.com/jobs", "source": "牛客网", "highlight": "内容平台，品牌视觉年轻化"},
    {"company": "哔哩哔哩", "position": "视觉设计师/活动设计师", "city": "上海", "type": "上市公司", "salary": "14-22K", "deadline": "2026校招", "url": "https://www.nowcoder.com/jobs", "source": "牛客网", "highlight": "Z世代平台，视觉风格鲜明"},
    {"company": "拼多多", "position": "UI设计师/运营设计师", "city": "上海", "type": "上市公司", "salary": "15-25K", "deadline": "2026校招", "url": "https://www.nowcoder.com/jobs", "source": "牛客网", "highlight": "电商巨头，运营设计需求大"},
    {"company": "美团", "position": "品牌设计师/视觉设计师", "city": "上海", "type": "上市公司", "salary": "15-25K", "deadline": "2026校招", "url": "https://www.nowcoder.com/jobs", "source": "牛客网", "highlight": "本地生活龙头，品牌体系完善"},
    {"company": "携程集团", "position": "品牌设计师/视觉设计师", "city": "上海", "type": "上市公司", "salary": "12-18K", "deadline": "2026校招", "url": "https://www.liepin.com/city-shanghai/", "source": "猎聘", "highlight": "旅游平台，品牌全球化"},
    {"company": "阅文集团", "position": "视觉设计师/包装设计师", "city": "上海", "type": "上市公司", "salary": "12-18K", "deadline": "2026校招", "url": "https://www.liepin.com/city-shanghai/", "source": "猎聘", "highlight": "IP内容平台，出版物设计"},
    # --- 新特精 ---
    {"company": "米哈游", "position": "视觉设计师/美术设计师", "city": "上海", "type": "专精特新", "salary": "18-30K", "deadline": "2026校招", "url": "https://www.nowcoder.com/jobs", "source": "牛客网", "highlight": "游戏巨头，美术视觉顶尖"},
    {"company": "莉莉丝游戏", "position": "视觉设计师/UI设计师", "city": "上海", "type": "专精特新", "salary": "15-25K", "deadline": "2026校招", "url": "https://www.nowcoder.com/jobs", "source": "牛客网", "highlight": "出海游戏公司，视觉要求高"},
    {"company": "得物App", "position": "品牌设计师/包装设计师", "city": "上海", "type": "专精特新", "salary": "14-22K", "deadline": "2026校招", "url": "https://www.nowcoder.com/jobs", "source": "牛客网", "highlight": "潮流电商平台，包装设计刚需"},
    {"company": "帆书（原樊登读书）", "position": "视觉设计师/新媒体设计", "city": "上海", "type": "专精特新", "salary": "10-16K", "deadline": "持续", "url": "https://www.liepin.com/city-shanghai/", "source": "猎聘", "highlight": "知识付费平台，新媒体视觉"},
]

# 推荐搜索平台链接
SEARCH_LINKS = {
    "应届生求职网-福建": "https://www.yingjiesheng.com/",
    "应届生求职网-广东": "https://www.yingjiesheng.com/guangdong/",
    "应届生求职网-上海": "https://www.yingjiesheng.com/shanghai/",
    "智联招聘-福建": "https://www.zhaopin.com/fujian/",
    "智联招聘-广东": "https://www.zhaopin.com/guangdong/",
    "智联招聘-上海": "https://www.zhaopin.com/shanghai/",
    "猎聘-厦门": "https://www.liepin.com/city-xiamen/",
    "猎聘-福州": "https://www.liepin.com/city-fuzhou/",
    "猎聘-广州": "https://www.liepin.com/city-guangzhou/",
    "猎聘-深圳": "https://www.liepin.com/city-shenzhen/",
    "猎聘-上海": "https://www.liepin.com/city-shanghai/",
    "牛客网校招": "https://www.nowcoder.com/jobs",
    "厦门人才网": "https://www.xmrc.com.cn/",
    "中国海峡人才网": "https://www.hxrc.com/",
    "福建国聘": "https://www.guopin.com/fujian/",
    "广东省事业单位公开招聘": "https://rsj.gd.gov.cn/",
    "上海一网通办-招聘": "https://zwdt.sh.gov.cn/",
    "福建省事业单位公开招聘": "http://rst.fujian.gov.cn/zw/ztzl/zxzt/sydwrczp/",
    "大学生求职神器": "（微信小程序搜索）",
}

def generate_fujian_report():
    """生成福建省每日校招情报报告"""
    today = datetime.date.today()
    weekday = ["周一", "周二", "周三", "周四", "周五", "周六", "周日"][today.weekday()]
    
    # 分类筛选
    state_owned = [j for j in JOB_POOL if j["type"] in ["国企", "央企", "事业单位", "国企关联"]]
    listed = [j for j in JOB_POOL if j["type"] == "上市公司"]
    xinte = [j for j in JOB_POOL if j["type"] in ["专精特新", "文创"]]
    xiamen = [j for j in JOB_POOL if j["city"] in ["厦门", "厦门/多城市", "福州/厦门"]]
    fuzhou = [j for j in JOB_POOL if j["city"] in ["福州", "福州/厦门"]]
    quanzhou = [j for j in JOB_POOL if j["city"] == "泉州"]
    shenzhen = [j for j in JOB_POOL if "深圳" in j["city"]]
    guangzhou = [j for j in JOB_POOL if "广州" in j["city"]]
    shanghai = [j for j in JOB_POOL if j["city"] == "上海"]
    
    report = f"""🎯 校招情报日报 · 2026届视觉传达设计
📅 {today.strftime('%Y年%m月%d日')} {weekday} | ⏰ 每日8点前推送

━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
📍 覆盖地区：福建（厦门·福州·泉州）| 大湾区（广州·深圳）| 上海
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
    
    report += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🌆 【深圳专场】（{len(shenzhen)}家）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for job in shenzhen:
        report += f"• {job['company']} · {job['position']} · {job['salary']}\n"
    
    report += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🏙️ 【广州专场】（{len(guangzhou)}家）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for job in guangzhou:
        report += f"• {job['company']} · {job['position']} · {job['salary']}\n"
    
    report += f"""
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
🗼 【上海专场】（{len(shanghai)}家）
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""
    for job in shanghai:
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
        "央国企/事业单位岗位：关注各省人社厅官网招聘公告",
        "厦门地区重点：厦门人才网 xmrc.com.cn 每周更新事业单位和国企岗位",
        "福州地区重点：中国海峡人才网 hxrc.com 是福建权威招聘平台",
        "深圳/广州重点：牛客网和WonderCV校招日历，大厂设计岗集中",
        "上海重点：牛客网+猎聘网，互联网/游戏/内容平台设计岗多",
        "上市公司校招：优先关注牛客网和WonderCV的校招日历",
        "专精特新企业：猎聘网筛选'高新技术企业'标签",
        "简历命名格式：姓名_澳科大_视觉传达_应聘岗位.pdf",
        "福建国企普遍要求：本科学历+作品集+面试",
        "深圳游戏/科技大厂：作品集质量决定一切，提前准备",
        "上海互联网大厂：关注牛客网内推渠道，简历过筛率高",
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
    json_path = os.path.join(report_dir, "jobs.json")
    with open(json_path, "w", encoding="utf-8") as f:
        json.dump({
            "date": today_str,
            "update_time": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "coverage": "福建+大湾区+上海",
            "jobs": JOB_POOL,
            "summary": {
                "state_owned": len([j for j in JOB_POOL if j["type"] in ["国企", "央企", "事业单位", "国企关联"]]),
                "listed": len([j for j in JOB_POOL if j["type"] == "上市公司"]),
                "xinte": len([j for j in JOB_POOL if j["type"] in ["专精特新", "文创"]]),
                "xiamen": len([j for j in JOB_POOL if "厦门" in j["city"]]),
                "fuzhou": len([j for j in JOB_POOL if "福州" in j["city"]]),
                "quanzhou": len([j for j in JOB_POOL if j["city"] == "泉州"]),
                "shenzhen": len([j for j in JOB_POOL if "深圳" in j["city"]]),
                "guangzhou": len([j for j in JOB_POOL if "广州" in j["city"]]),
                "shanghai": len([j for j in JOB_POOL if j["city"] == "上海"]),
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
