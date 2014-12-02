## 程序功能

压缩给定目录下的javascript文件和php文件：

- 去掉注释（单行和区块）
- 去掉缩进
- 去掉换行

将压缩后的代码输出到指定的目录下，目标目录的结构和原目录相同。
注意：程序目前不能处理单行注释与多行注释嵌套的情况（例如多行注释中包含协议头标识符）

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
- `main_GUI.py`: 图形界面模块，在`main.py`中被导入，用于对`config.py`中的值进行设置
- `test.py`: 单元测试模块

----

## 使用示例

### 方法一：运行可执行文件
`\bin`目录为打包生成目录，可以只下载该目录运行`main.exe`程序。

### 方法二：解释源代码

> 运行程序需要python 3.x环境，并将`python.exe`的路径添加到`PATH`环境变量中

1. 在程序目录下通过`cmd`运行`python main.py`；如果`py`的文件关联是使用python解释器运行，则可直接双击`main.py`文件。
2. 设置源目录与目标目录
3. 设置对应语言的文件后缀名
    - 语言在左边的列表中选择
    - 后缀名在右边列表中显示
    - 添加后缀名使用右侧下方的单行输入框，回车进行添加
    - 暂不提供删除后缀名的功能，因此输入错误后需要重新来过= =
4. 关闭配置框后，程序会根据设置生成代码
  - 注意：如果目标文件已经存在，将会**直接覆盖**
> 这点确实很诡异，但时间所限。但愿后续会逐渐完善
5. 如果源目录或目标目录中任意一个**为空**，则程序会什么也不做，可以用于取消本次操作
