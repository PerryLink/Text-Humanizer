# Contributing to Text Humanizer

[English](#english) | [中文](#中文)

---

## English

### Project Status

This is a personal project currently maintained by [PerryLink](https://github.com/PerryLink). While contributions are welcome, please note that this project is primarily developed and maintained by a single developer.

### Reporting Issues

If you encounter any bugs or have feature requests, please open an issue on GitHub:

1. Check if the issue already exists
2. Provide a clear description of the problem or feature
3. Include steps to reproduce (for bugs)
4. Add relevant code snippets or error messages

### Development Setup

1. Clone the repository:
```bash
git clone https://github.com/PerryLink/text-humanizer.git
cd text-humanizer
```

2. Install Poetry (if not already installed):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. Install dependencies:
```bash
poetry install
```

4. Run tests:
```bash
poetry run pytest
```

### Code Style

This project follows PEP 8 guidelines:

- Use Black for code formatting (line length: 88)
- Write docstrings for all public functions and classes
- Add type hints where appropriate
- Keep functions focused and concise

Format your code before committing:
```bash
poetry run black src/ tests/
```

### Pull Request Process

1. Fork the repository
2. Create a new branch for your feature or bugfix:
```bash
git checkout -b feature/your-feature-name
```

3. Make your changes and ensure tests pass:
```bash
poetry run pytest
```

4. Format your code:
```bash
poetry run black src/ tests/
```

5. Commit your changes with a clear message:
```bash
git commit -m "Add feature: description of your changes"
```

6. Push to your fork and submit a pull request

7. Wait for review and address any feedback

### Questions?

Feel free to open an issue for any questions or concerns. You can also reach out to the maintainer at novelnexusai@outlook.com.

---

## 中文

### 项目状态

这是一个由 [PerryLink](https://github.com/PerryLink) 个人维护的项目。虽然欢迎贡献,但请注意该项目主要由单个开发者开发和维护。

### 报告问题

如果你遇到任何 bug 或有功能请求,请在 GitHub 上提交 issue:

1. 检查问题是否已存在
2. 提供清晰的问题或功能描述
3. 包含重现步骤(针对 bug)
4. 添加相关代码片段或错误信息

### 开发环境搭建

1. 克隆仓库:
```bash
git clone https://github.com/PerryLink/text-humanizer.git
cd text-humanizer
```

2. 安装 Poetry(如果尚未安装):
```bash
curl -sSL https://install.python-poetry.org | python3 -
```

3. 安装依赖:
```bash
poetry install
```

4. 运行测试:
```bash
poetry run pytest
```

### 代码规范

本项目遵循 PEP 8 规范:

- 使用 Black 进行代码格式化(行长度: 88)
- 为所有公共函数和类编写文档字符串
- 在适当的地方添加类型提示
- 保持函数专注和简洁

提交前格式化代码:
```bash
poetry run black src/ tests/
```

### Pull Request 流程

1. Fork 仓库
2. 为你的功能或 bug 修复创建新分支:
```bash
git checkout -b feature/your-feature-name
```

3. 进行更改并确保测试通过:
```bash
poetry run pytest
```

4. 格式化代码:
```bash
poetry run black src/ tests/
```

5. 使用清晰的消息提交更改:
```bash
git commit -m "Add feature: description of your changes"
```

6. 推送到你的 fork 并提交 pull request

7. 等待审查并处理任何反馈

### 有问题?

欢迎为任何问题或疑虑提交 issue。你也可以通过 novelnexusai@outlook.com 联系维护者。
