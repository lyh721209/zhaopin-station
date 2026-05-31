# 校招情报站 · Gitee 国内镜像配置指南

## 状态
- [x] Gitee 仓库已存在：`lyh721209/zhaopin-station`
- [x] 本地代码已推送到 GitHub（主站）
- [x] 新 SSH 密钥对已生成（`id_ed25519_gitee`）
- [ ] Gitee 公钥待添加
- [ ] Gitee Pages 待开启
- [ ] 代码同步到 Gitee 待完成

---

## 你需要做的 3 步操作

### 步骤 1：把公钥添加到 Gitee

**公钥内容（复制下面的完整内容）：**

```
ssh-ed25519 AAAAC3NzaC1lZDI1NTE5AAAAIMBlEf/SiF/sGQWD8aPXRw513Tf46R5sddYOM2o+pAOo gitee-lyh721209
```

**添加路径：**
1. 电脑浏览器打开 `https://gitee.com`
2. 登录账号 `lyh721209`
3. 右上角头像 → **设置**
4. 左侧菜单 → **SSH 公钥**
5. 点击 **添加公钥**
6. 标题填：`校招情报站同步`
7. 公钥内容粘贴上面的完整文本
8. 点击 **确定**

---

### 步骤 2：开启 Gitee Pages

1. 登录 Gitee 后，打开仓库：`https://gitee.com/lyh721209/zhaopin-station`
2. 点击顶部菜单 **服务** → **Gitee Pages**
3. 选择部署分支：`master`
4. 选择部署目录：`/`（根目录）
5. 点击 **启动**
6. 等待 1-2 分钟，会生成一个 `https://lyh721209.gitee.io/zhaopin-station` 的地址

---

### 步骤 3：通知我完成同步

公钥添加后，回复我一声，我会立即把代码推送到 Gitee，之后两个站内容保持一致。

以后每天自动更新时，我会同时推送到 GitHub 和 Gitee，你哪个能打开就用哪个。

---

## 两个地址对照

| 站点 | 地址 | 适用场景 |
|:---|:---|:---|
| **GitHub Pages（主站）** | https://lyh721209.github.io/zhaopin-station/ | 海外网络、加速器环境 |
| **Gitee Pages（国内镜像）** | https://lyh721209.gitee.io/zhaopin-station | 国内网络、日常浏览 |

---

## 推荐浏览器

| 浏览器 | 推荐指数 | 原因 |
|:---|:---|:---|
| **Chrome（谷歌浏览器）** | ⭐⭐⭐⭐⭐ | 对 github.io / gitee.io 兼容性最好，加载稳定 |
| **Edge（微软浏览器）** | ⭐⭐⭐⭐⭐ | 国内默认预装，表现优秀 |
| **Safari（苹果浏览器）** | ⭐⭐⭐⭐⭐ | iPhone/Mac 首选，速度流畅 |
| **Firefox（火狐）** | ⭐⭐⭐⭐ | 隐私保护强，兼容性好 |
| **微信内置浏览器** | ⭐⭐ | 容易拦截 github.io，不建议 |
| **QQ浏览器 / 360** | ⭐⭐⭐ | 能用但不推荐，广告多 |

**结论：用 Chrome 或 Edge 打开，体验最好。** 手机端推荐 Safari（iOS）或 Chrome（Android）。

---

> 公钥添加完成后告诉我，我立即同步代码。 ❤️‍🔥
