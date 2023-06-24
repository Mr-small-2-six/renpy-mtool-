# renpy-mtool-json
单纯用chatgpt帮我写了几个代码在rpy转去json格式里面还有很多不完美的地方，希望有好心人去改进

试用了几个用chatgpt翻译的软件就只能用在rpgmaker游戏里，Translator++的方式导入的时候会卡住就想到试试把ti 里.rpy的文本转去json格式作为翻译

所以我这个编程小白自己找chatgpt和bing还有Claude写了几个导出和导入的代码

因为自己一边翻译一边导入，导致有几个.py 我都不知道那个最稳定了

因为还有一些文本无法正常翻译到，大概是导出的时候导出的不够干净和导入的时候不够干净

fix.py 是修复一些英文游戏# 修复反斜杠转义的问题，大概是英文游戏容易出现的bug

导出tran.py 是导出rpy的文件转去json格式，让json格式的文本可以使用一些chatgpt翻译工具翻译

导入2.py 把翻译好的文件导入去 rpy里

导入3.py 把把翻译好的文件导入去 rpy里 

导入2.py和导入3.py 已经忘记那个比较稳定了

检查空白.py  是检查json 导入前使用,因为导入json去rpy的时有时候会发生错误，所以需要检查，实际用途我也大概忘记了

这里的所有代码都是chatgpt写的，有任何疑问可以询问AI大神，让他修改由于自己是编程小白，有很多函数还是指定条件都无法正确给ai提示所以变成有些难度要完美的用json格式翻译

希望在这里抛砖引玉让人完善代码或者有更好的方法用ai翻译renpy的游戏

我是使用 https://github.com/NEKOparapa/AiNiee-chatgpt 来翻译renpy
