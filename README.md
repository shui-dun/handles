# Handles

一般的任务管理器只能查看一个进程当前占有的句柄，不能查看一个进程曾经占有但已经释放的句柄。本工具可以完全该任务

## 使用方法

- 下载 [Handle](https://docs.microsoft.com/en-us/sysinternals/downloads/handle) 程序，并将其放入 `PATH`
- `git clone https://github.com/shui-dun/handles`
- 仿照 `config.template.py` 编写 `config.py`
- `python.exe main.py`
