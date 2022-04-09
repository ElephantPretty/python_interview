
# 解释器用的 字符串来导入模块--不推荐使用
__import__("16_property")
# 推荐使用的动态导入模块
# 要求工作目录是特定位置
import importlib
importlib.import_module("16_property")
importlib.import_module("day01.08_继承")