#!/bin/bash
# 校招情报站每日自动更新脚本
# 执行时间：每天早上 6:30

set -e

WORKSPACE="/root/.openclaw/workspace/校招情报站"
DATE=$(date +%Y-%m-%d)
TIME=$(date +%H:%M)
LOG="$WORKSPACE/reports/auto_update_$DATE.log"

echo "=== 校招情报站自动更新 ===" >> "$LOG"
echo "时间: $DATE $TIME" >> "$LOG"

# 1. 生成福建省日报
cd "$WORKSPACE"
/usr/bin/python3 fujian_daily.py > "$WORKSPACE/reports/福建省日报_$DATE.md" 2>> "$LOG"
echo "✅ 福建省日报已生成" >> "$LOG"

# 2. 生成全国日报
/usr/bin/python3 daily_report.py > "$WORKSPACE/reports/全国日报_$DATE.md" 2>> "$LOG"
echo "✅ 全国日报已生成" >> "$LOG"

# 3. 复制最新日报到网站目录（作为当日展示）
cp "$WORKSPACE/reports/福建省日报_$DATE.md" "$WORKSPACE/今日情报.md" 2>/dev/null || true
cp "$WORKSPACE/reports/全国日报_$DATE.md" "$WORKSPACE/今日全国情报.md" 2>/dev/null || true

# 4. 生成 PDF 版本（如果 md2html.py 可用）
if [ -f "$WORKSPACE/md2html.py" ]; then
    /usr/bin/python3 "$WORKSPACE/md2html.py" "$WORKSPACE/reports/福建省日报_$DATE.md" "$WORKSPACE/reports/福建省日报_$DATE.html" 2>> "$LOG" || true
    echo "✅ HTML 版本已生成" >> "$LOG"
fi

# 5. 确保本地服务器在运行
if ! pgrep -f "python3 -m http.server 8888" > /dev/null; then
    cd "$WORKSPACE" && nohup python3 -m http.server 8888 > /tmp/server.log 2>&1 &
    echo "✅ 本地服务器已启动" >> "$LOG"
else
    echo "✅ 本地服务器运行中" >> "$LOG"
fi

echo "=== 更新完成 ===" >> "$LOG"
echo ""
