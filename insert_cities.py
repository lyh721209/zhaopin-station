#!/usr/bin/env python3
"""
在 index.html 中插入深圳、广州、上海城市专场
"""

SHENZHEN_HTML = """
<!-- 深圳专场 -->
<section class="container" id="shenzhen">
  <div class="city-section">
    <div class="city-header">
      <div class="city-name">🌆 深圳专场 <small>科技创新之都 · 互联网/游戏/消费电子 · 2026届校招</small></div>
      <div class="city-count">8 家企业</div>
    </div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>企业</th>
            <th>行业</th>
            <th>岗位</th>
            <th>类型</th>
            <th>薪资</th>
            <th>截止</th>
            <th>投递</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="company-cell">韶音科技<br><small>（出海品牌·骨传导耳机）</small></td>
            <td class="location-cell">消费电子</td>
            <td class="position-cell">视觉设计管培生 / UI设计师 / 三维渲染设计师</td>
            <td class="location-cell">上市公司</td>
            <td class="location-cell">面议</td>
            <td class="deadline-cell warning">尽快投递</td>
            <td class="link-cell"><a href="https://app.mokahr.com/campus-recruitment/aftershokzhr/36940" target="_blank">官网投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">OPPO</td>
            <td class="location-cell">消费电子</td>
            <td class="position-cell">多类岗位含设计方向</td>
            <td class="location-cell">上市公司</td>
            <td class="location-cell">面议</td>
            <td class="deadline-cell warning">尽快投递</td>
            <td class="link-cell"><a href="https://www.oppo.com/cn/careers/" target="_blank">官网投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">大疆创新<br><small>（DJI·无人机全球龙头）</small></td>
            <td class="location-cell">智能硬件</td>
            <td class="position-cell">视觉设计师 / 品牌设计师</td>
            <td class="location-cell">上市公司</td>
            <td class="location-cell">15-25K</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.dji.com/careers" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">传音控股<br><small>（TECNO·非洲手机之王）</small></td>
            <td class="location-cell">消费电子</td>
            <td class="position-cell">视觉设计师（海外品牌）</td>
            <td class="location-cell">上市公司</td>
            <td class="location-cell">12-20K</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.transsion.com/careers" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">华润集团</td>
            <td class="location-cell">央企多元化</td>
            <td class="position-cell">品牌设计 / 视觉设计管培生</td>
            <td class="location-cell">央企</td>
            <td class="location-cell">面议</td>
            <td class="deadline-cell safe">2026春招</td>
            <td class="link-cell"><a href="https://runjob.crc.com.cn" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">招商银行</td>
            <td class="location-cell">金融科技</td>
            <td class="position-cell">视觉设计 / 创意设计师</td>
            <td class="location-cell">国企</td>
            <td class="location-cell">面议</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.cmbchina.com/careers" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">追觅科技<br><small>（智能清洁·独角兽）</small></td>
            <td class="location-cell">智能家居</td>
            <td class="position-cell">视觉设计师 / 包装设计师</td>
            <td class="location-cell">专精特新</td>
            <td class="location-cell">12-18K</td>
            <td class="deadline-cell safe">持续</td>
            <td class="link-cell"><a href="https://www.dreame.tech/" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">深圳报业集团</td>
            <td class="location-cell">传媒</td>
            <td class="position-cell">新媒体视觉设计师</td>
            <td class="location-cell">国企</td>
            <td class="location-cell">面议</td>
            <td class="deadline-cell safe">滚动招聘</td>
            <td class="link-cell"><a href="https://www.sznews.com/" target="_blank">投递 →</a></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div style="margin-top:20px;padding:14px 18px;background:#f8f9fa;border-radius:8px;font-size:13px;color:#666;line-height:1.8">
      <strong>💡 深圳投递建议：</strong><br>
      ① 大疆/韶音/OPPO 对作品集质量要求极高，建议准备 3-5 个完整项目 case；<br>
      ② 深圳游戏/科技大厂集中，牛客网内推渠道简历过筛率高，优先使用内推码；<br>
      ③ 传音控股海外品牌方向需展示跨文化设计能力；<br>
      ④ 华润/招行等央国企深圳分支竞争激烈，简历突出政治面貌和学生干部经历。
    </div>
  </div>
</section>
"""

GUANGZHOU_HTML = """
<!-- 广州专场 -->
<section class="container" id="guangzhou">
  <div class="city-section">
    <div class="city-header">
      <div class="city-name">🏙️ 广州专场 <small>商贸之都 · 汽车/传媒/电商/快消 · 2026届校招</small></div>
      <div class="city-count">7 家企业</div>
    </div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>企业</th>
            <th>行业</th>
            <th>岗位</th>
            <th>类型</th>
            <th>薪资</th>
            <th>截止</th>
            <th>投递</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="company-cell">唯品会</td>
            <td class="location-cell">电商</td>
            <td class="position-cell">视觉设计师 / 品牌设计师</td>
            <td class="location-cell">上市公司</td>
            <td class="location-cell">12-18K</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.vip.com/join" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">小鹏汽车<br><small>（智能电动车）</small></td>
            <td class="location-cell">新能源汽车</td>
            <td class="position-cell">UI/UX设计师（智能座舱）</td>
            <td class="location-cell">上市公司</td>
            <td class="location-cell">15-25K</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.xiaopeng.com/join" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">广汽集团</td>
            <td class="location-cell">汽车制造</td>
            <td class="position-cell">品牌设计 / UI设计（智能网联）</td>
            <td class="location-cell">国企</td>
            <td class="location-cell">面议</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.gac.com.cn/careers" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">南方报业传媒集团</td>
            <td class="location-cell">传媒</td>
            <td class="position-cell">视觉设计师 / 新媒体设计</td>
            <td class="location-cell">国企</td>
            <td class="location-cell">面议</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.nfmedia.com/" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">TCL</td>
            <td class="location-cell">家电/电子</td>
            <td class="position-cell">品牌视觉设计师 / UI设计师</td>
            <td class="location-cell">上市公司</td>
            <td class="location-cell">10-15K</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.tcl.com/careers" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">蓝月亮</td>
            <td class="location-cell">快消</td>
            <td class="position-cell">包装设计师 / 品牌设计师</td>
            <td class="location-cell">上市公司</td>
            <td class="location-cell">10-14K</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.bluemoon.com.cn/careers" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">亿航智能<br><small>（eVTOL飞行器）</small></td>
            <td class="location-cell">低空经济</td>
            <td class="position-cell">工业设计师 / 视觉设计师</td>
            <td class="location-cell">专精特新</td>
            <td class="location-cell">12-20K</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.ehang.com/careers" target="_blank">投递 →</a></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div style="margin-top:20px;padding:14px 18px;background:#f8f9fa;border-radius:8px;font-size:13px;color:#666;line-height:1.8">
      <strong>💡 广州投递建议：</strong><br>
      ① 小鹏/广汽智能座舱UI方向需要展示车机界面或交互设计作品；<br>
      ② 南方报业传媒集团适合有媒体实习经历（泉州广电/厦门广电/泉港宣传部）的你；<br>
      ③ 唯品会/TCL/蓝月亮等大厂校招集中在牛客网和官网，注意网申时间节点；<br>
      ④ 广州生活成本低于深圳，国企/事业单位比例更高，适合偏好稳定的求职者。
    </div>
  </div>
</section>
"""

SHANGHAI_HTML = """
<!-- 上海专场 -->
<section class="container" id="shanghai">
  <div class="city-section">
    <div class="city-header">
      <div class="city-name">🗼 上海专场 <small>国际金融中心 · 互联网/游戏/内容平台 · 2026届校招</small></div>
      <div class="city-count">10 家企业</div>
    </div>
    <div class="table-wrap">
      <table>
        <thead>
          <tr>
            <th>企业</th>
            <th>行业</th>
            <th>岗位</th>
            <th>类型</th>
            <th>薪资</th>
            <th>截止</th>
            <th>投递</th>
          </tr>
        </thead>
        <tbody>
          <tr>
            <td class="company-cell">小红书</td>
            <td class="location-cell">内容平台</td>
            <td class="position-cell">品牌设计师 / 视觉设计师</td>
            <td class="location-cell">上市公司</td>
            <td class="location-cell">15-25K</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.xiaohongshu.com/join" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">哔哩哔哩<br><small>（B站）</small></td>
            <td class="location-cell">视频平台</td>
            <td class="position-cell">视觉设计师 / 活动设计师</td>
            <td class="location-cell">上市公司</td>
            <td class="location-cell">14-22K</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://jobs.bilibili.com/" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">米哈游<br><small>（miHoYo·原神/崩坏）</small></td>
            <td class="location-cell">游戏</td>
            <td class="position-cell">视觉设计师 / 美术设计师</td>
            <td class="location-cell">专精特新</td>
            <td class="location-cell">18-30K</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.mihoyo.com/careers" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">莉莉丝游戏</td>
            <td class="location-cell">游戏</td>
            <td class="position-cell">视觉设计师 / UI设计师</td>
            <td class="location-cell">专精特新</td>
            <td class="location-cell">15-25K</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.lilithgames.com/careers" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">得物App</td>
            <td class="location-cell">潮流电商</td>
            <td class="position-cell">品牌设计师 / 包装设计师</td>
            <td class="location-cell">专精特新</td>
            <td class="location-cell">14-22K</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.dewu.com/join" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">美团</td>
            <td class="location-cell">本地生活</td>
            <td class="position-cell">品牌设计师 / 视觉设计师</td>
            <td class="location-cell">上市公司</td>
            <td class="location-cell">15-25K</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.meituan.com/join" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">拼多多</td>
            <td class="location-cell">电商</td>
            <td class="position-cell">UI设计师 / 运营设计师</td>
            <td class="location-cell">上市公司</td>
            <td class="location-cell">15-25K</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.pinduoduo.com/join" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">携程集团</td>
            <td class="location-cell">旅游平台</td>
            <td class="position-cell">品牌设计师 / 视觉设计师</td>
            <td class="location-cell">上市公司</td>
            <td class="location-cell">12-18K</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.ctrip.com/join" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">上海报业集团</td>
            <td class="location-cell">传媒</td>
            <td class="position-cell">新媒体视觉设计师</td>
            <td class="location-cell">国企</td>
            <td class="location-cell">面议</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.shmedia.com/" target="_blank">投递 →</a></td>
          </tr>
          <tr>
            <td class="company-cell">东航集团</td>
            <td class="location-cell">航空</td>
            <td class="position-cell">品牌设计 / 视觉设计</td>
            <td class="location-cell">央企</td>
            <td class="location-cell">面议</td>
            <td class="deadline-cell safe">2026校招</td>
            <td class="link-cell"><a href="https://www.ceair.com/careers" target="_blank">投递 →</a></td>
          </tr>
        </tbody>
      </table>
    </div>
    <div style="margin-top:20px;padding:14px 18px;background:#f8f9fa;border-radius:8px;font-size:13px;color:#666;line-height:1.8">
      <strong>💡 上海投递建议：</strong><br>
      ① 米哈游/莉莉丝对美术功底要求极高，建议准备游戏UI、角色设计或场景设计作品；<br>
      ② 小红书/B站/得物等品牌调性年轻化，作品集风格需贴合平台气质；<br>
      ③ 美团/拼多多/携程等大厂校招流程标准化，牛客网内推码可提高过筛率；<br>
      ④ 上海生活成本高，但设计类岗位薪资天花板最高（米哈游18-30K），适合冲击高薪；<br>
      ⑤ 东航/上海报业等央国企竞争相对温和，可作为保底选择。
    </div>
  </div>
</section>
"""

with open('/root/.openclaw/workspace/校招情报站/index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 找到插入位置：在 "<!-- 校招日历 -->" 之前
insert_marker = '<!-- 校招日历 -->'
idx = content.find(insert_marker)

if idx != -1:
    new_content = content[:idx] + SHENZHEN_HTML + GUANGZHOU_HTML + SHANGHAI_HTML + '\n' + content[idx:]
    with open('/root/.openclaw/workspace/校招情报站/index.html', 'w', encoding='utf-8') as f:
        f.write(new_content)
    print(f"✅ 已成功插入深圳、广州、上海专场（位置: {idx}）")
else:
    print("❌ 未找到插入标记")
