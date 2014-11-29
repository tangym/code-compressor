## 程序功能

压缩给定目录下的javascript文件和php文件：

- 去掉注释（单行和区块）
- 去掉缩进
- 去掉换行

将压缩后的代码输出到指定的目录下，目标目录的结构和原目录相同。

> 除了给出的扩展名以外的文件不会输出到目标目录

----

## 文件说明

- `config.py`: 配置模块，定义必要参数
    - `SOURCE_DIR`: 源代码根目录的绝对路径
    - `TARGET_DIR`: 输出的绝对路径；程序会自动创建该路径，如果已经存在，则直接退出
    - `SOURCE_ENCODING`: 源文件编码方式
    - `TARGET_ENCODING`: 目标文件编码方式
    - `EXTENSION`: 语言对应的文件扩展名，键值对的形式；键允许添加，但不允许修改；多个扩展名可以使用数组表示
- `compressor.py`: 定义了处理每种语言对应的类
- `main.py`: 驱动模块，进行目录拷贝、文件读入、调用对应的类进行文件处理以及写入
- `test.py`: 单元测试模块

----

## 使用示例

> 运行程序需要python 3.x环境，并将`python.exe`的路径添加到`PATH`环境变量中

1. 配置`config.py`文件中的`SOURCE_DIR`和`TARGET_DIR`
2. 在本程序目录下通过`cmd`运行`python main.py`；如果·py·的文件关联是使用python解释器运行，则可直接双击·main.py·文件。