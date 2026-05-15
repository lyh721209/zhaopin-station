#!/bin/bash
# 校招情报站服务器守护脚本
# 确保 HTTP 服务器始终运行

WORKSPACE="/root/.openclaw/workspace/校招情报站"
PIDFILE="/tmp/zhaopin_server.pid"

# 检查是否已在运行
if [ -f "$PIDFILE" ]; then
    OLD_PID=$(cat "$PIDFILE")
    if ps -p "$OLD_PID" > /dev/null 2>&1; then
        echo "Server already running (PID: $OLD_PID)"
        exit 0
    fi
fi

# 启动服务器
cd "$WORKSPACE"
nohup python3 -m http.server 8888 > /tmp/server.log 2>&1 &
echo $! > "$PIDFILE"
echo "Server started on port 8888 (PID: $!)"
