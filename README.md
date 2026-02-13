# Text Humanizer 🤖➡️👤

> Stop sounding like a bot. Instantly check your text's "Humanity Score".

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/License-Apache%202.0-blue.svg)](https://opensource.org/licenses/Apache-2.0)
[![Code style: black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

[English](#english) | [中文](#中文)

---

## English

### Features

- 📊 **Instant Readability Score** - Get a 0-100 score showing how "human" your text sounds
- 🎨 **Beautiful Terminal UI** - Color-coded gauge from 🔴 Robot to 🟢 Human
- 📝 **Multiple Formats** - Supports Markdown (`.md`) and plain text (`.txt`) files
- 🚨 **AI Word Detection** - Highlights common AI-generated words like "delve", "testament", "tapestry"
- ⚡ **Fast & Lightweight** - No API calls, runs completely offline

### Quick Start

#### Installation

```bash
pip install text-humanizer
```

Or install from source:

```bash
git clone https://github.com/PerryLink/text-humanizer.git
cd text-humanizer
poetry install
```

#### Usage

Check a file:
```bash
check-human ./draft.md
```

Pipe from clipboard (macOS):
```bash
pbpaste | check-human -
```

Pipe from clipboard (Windows):
```bash
powershell Get-Clipboard | check-human -
```

### How It Works

The tool uses proven readability algorithms:

1. **Flesch Reading Ease Score** - Higher scores = easier to read
   - 0-30: Very difficult (Academic/Robot)
   - 30-60: Difficult (Standard)
   - 60-100: Easy (Conversational/Human)

2. **Average Sentence Length** - Shorter sentences = more natural
   - Penalty applied if average > 25 words

3. **AI Word Detection** - Flags common AI-generated words that make text sound robotic

### Project Structure

```
text-humanizer/
├── src/
│   └── text_humanizer/
│       ├── __init__.py
│       ├── __main__.py
│       ├── analyzer.py      # Core analysis logic
│       ├── cleaner.py       # Text preprocessing
│       ├── cli.py           # Command-line interface
│       └── ui.py            # Terminal UI rendering
├── tests/
│   ├── test_analyzer.py
│   └── test_cleaner.py
├── examples/
│   ├── sample_human.txt
│   ├── sample_robot.txt
│   └── sample_markdown.md
├── pyproject.toml
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

### Tech Stack

- **Python 3.8+** - Core language
- **textstat** - Readability metrics calculation
- **rich** - Beautiful terminal output
- **typer** - CLI framework
- **pytest** - Testing framework
- **black** - Code formatting

### License

This project is licensed under the Apache License 2.0 - see the [LICENSE](LICENSE) file for details.

Copyright 2026 Chance Dean (novelnexusai@outlook.com)

### Contributing

Contributions are welcome! Please see [CONTRIBUTING.md](CONTRIBUTING.md) for details.

---

## 中文

### 功能特性

- 📊 **即时可读性评分** - 获得 0-100 分的"人性化"评分
- 🎨 **精美终端界面** - 从 🔴 机器人到 🟢 人类的彩色评分条
- 📝 **多格式支持** - 支持 Markdown (`.md`) 和纯文本 (`.txt`) 文件
- 🚨 **AI 词汇检测** - 高亮显示常见的 AI 生成词汇,如 "delve"、"testament"、"tapestry"
- ⚡ **快速轻量** - 无需 API 调用,完全离线运行

### 快速开始

#### 安装

```bash
pip install text-humanizer
```

或从源码安装:

```bash
git clone https://github.com/PerryLink/text-humanizer.git
cd text-humanizer
poetry install
```

#### 使用方法

检查文件:
```bash
check-human ./draft.md
```

从剪贴板读取(macOS):
```bash
pbpaste | check-human -
```

从剪贴板读取(Windows):
```bash
powershell Get-Clipboard | check-human -
```

### 工作原理

本工具使用经过验证的可读性算法:

1. **Flesch 阅读易度评分** - 分数越高 = 越易读
   - 0-30:非常困难(学术/机器人)
   - 30-60:困难(标准)
   - 60-100:简单(对话/人类)

2. **平均句子长度** - 句子越短 = 越自然
   - 平均超过 25 个单词会被扣分

3. **AI 词汇检测** - 标记使文本听起来像机器人的常见 AI 生成词汇

### 项目结构

```
text-humanizer/
├── src/
│   └── text_humanizer/
│       ├── __init__.py
│       ├── __main__.py
│       ├── analyzer.py      # 核心分析逻辑
│       ├── cleaner.py       # 文本预处理
│       ├── cli.py           # 命令行界面
│       └── ui.py            # 终端 UI 渲染
├── tests/
│   ├── test_analyzer.py
│   └── test_cleaner.py
├── examples/
│   ├── sample_human.txt
│   ├── sample_robot.txt
│   └── sample_markdown.md
├── pyproject.toml
├── README.md
├── LICENSE
└── CONTRIBUTING.md
```

### 技术栈

- **Python 3.8+** - 核心语言
- **textstat** - 可读性指标计算
- **rich** - 精美终端输出
- **typer** - CLI 框架
- **pytest** - 测试框架
- **black** - 代码格式化

### 许可证

本项目采用 Apache License 2.0 许可证 - 详见 [LICENSE](LICENSE) 文件。

版权所有 2026 Chance Dean (novelnexusai@outlook.com)

### 贡献

欢迎贡献!详情请参阅 [CONTRIBUTING.md](CONTRIBUTING.md)。
