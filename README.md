# MergeEevee（合成伊布）

> 一个基于 **BigNaiWa** 二次创作的宝可梦主题合成小游戏。  
> 保留了原项目优秀的物理玩法，并将游戏素材替换为伊布家族角色。

![preview](preview.png)

---

## 🎮 在线体验

> https://yongmon.github.io/MergeEevee/

支持：

- 💻 PC 浏览器
- 📱 手机浏览器
- 📲 可添加到主屏幕作为 Web App

---

## ✨ 游戏特色

- 🍃 伊布家族主题
- 🎨 全部游戏素材替换为伊布及其进化形态
- ⚡ 保留原版流畅的物理碰撞体验
- 🏆 在线排行榜
- 📱 支持桌面端与移动端
- 🚀 无需安装，打开网页即可游玩

---

## 🕹️ 游戏玩法

玩法与经典《合成大西瓜》一致：

- 点击（PC）或松手（手机）投放角色
- 两个相同等级角色碰撞即可合成为下一阶段
- 合成更高级角色，获得更高分数
- 当角色堆积超过警戒线并停留一段时间，游戏结束

---

## 📷 游戏截图

![preview](preview.png)

---

## 🚀 本地运行

克隆项目：

```bash
git clone https://github.com/Yongmon/MergeEevee.git

cd MergeEevee
```

启动静态服务器：

```bash
python -m http.server 8000
```

浏览器访问：

```
http://localhost:8000
```

---

## 📂 项目结构

```
MergeEevee
│
├── assets/
│   └── fruits/          # 伊布素材
├── game.js              # 游戏逻辑
├── style.css            # 页面样式
├── index.html           # 页面入口
├── leaderboard.min.js   # 排行榜
├── preview.png          # 游戏截图
└── README.md
```

---

## 🛠️ 开发

项目采用纯前端实现：

- HTML5
- CSS3
- JavaScript
- Canvas API

无需任何框架或构建工具。

---

## ❤️ 致谢

本项目基于 **BigNaiWa** 进行二次创作。

本次修改主要包括：

- 更换为伊布家族主题素材
- 调整部分游戏资源与界面
- 保留原项目优秀的物理系统与玩法

感谢原作者的开源分享。

**原项目：**

GitHub：

> https://github.com/yhsome/BigNaiWa

在线体验：

> https://yhsome.github.io/BigNaiWa/

---

## 📄 License

本项目仅供学习与交流使用。

本项目为 **BigNaiWa** 的二次创作，请遵守原项目的开源协议。

**Pokémon（宝可梦）及伊布等角色版权归 Nintendo、Game Freak、Creatures Inc. 所有。**

如本项目存在版权问题，请联系删除。

---

## ⭐ Star

如果你喜欢这个项目，欢迎点一个 ⭐ Star！

同时也欢迎支持原作者的 **BigNaiWa** 项目。