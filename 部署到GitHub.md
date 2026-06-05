# 🚀 部署到 GitHub Pages（永久在线）

> 做完这些之后，不管在哪，一个链接就能看全部资料！

---

## 一次性设置（5分钟）

### 第1步：创建 GitHub 仓库

1. 打开 https://github.com/new
2. Repository name 填：`cet4-dashboard`（或你喜欢的名字）
3. 选择 **Public**（公开）
4. ❌ 不要勾选任何初始化选项
5. 点击 **Create repository**

### 第2步：推送代码

创建后会看到一段命令，复制下面这些在终端里运行：

```powershell
cd "d:\英语四级备战"
git add index.html .gitignore 备考资料/ 启动服务器.bat
git commit -m "四级冲刺仪表盘 v1"
git branch -M main
git remote add origin https://github.com/你的用户名/cet4-dashboard.git
git push -u origin main
```

> ⚠️ 把 `你的用户名` 和 `cet4-dashboard` 换成你实际的

### 第3步：开启 Pages

1. 打开仓库 → Settings → Pages
2. Source 选 **Deploy from a branch**
3. Branch 选 **main**，文件夹选 **/ (root)**
4. 点 **Save**
5. 等1-2分钟，会显示网址：`https://你的用户名.github.io/cet4-dashboard/`

---

## 📱 完成后的访问方式

| 场景 | 方式 |
|------|------|
| 🏠 在家 | `http://localhost:8080`（双击启动服务器.bat） |
| 🚌 外面 | `https://你的用户名.github.io/cet4-dashboard/` |
| 📱 手机 | 同上，浏览器打开就行 |

---

## 🔄 以后更新

资料有变动时，终端运行：

```powershell
cd "d:\英语四级备战"
git add .
git commit -m "更新资料"
git push
```

GitHub Pages 会自动更新，1-2分钟后生效。
