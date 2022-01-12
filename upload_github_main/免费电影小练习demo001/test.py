from 免费电影小练习demo001.play_video import a

"""
这里面使用相对路径会__main__找不到 
from .play_video import a 不能简单的这样执行，这样执行的话，模块的名字被变成了main
"""

a().b()