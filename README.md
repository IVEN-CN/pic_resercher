# 实现自动化办公
    在日常办公，会经常遇到批量修改文件名或者按照颜色分类颜色文件的情况，花费很多时间，也会消耗精力，于是决定开发此程序
# renamer
这是一个批量修改文件名的程序
### 使用情况
    现有文件夹800X800,800X1200,750X1000,下面的文件名都不一样，但是我们要将这些文件夹下的文件重命名为前面对应的数字，例如：
    在文件夹800X800中的文件全部重命名为800(6),800(7)等，括号后面的数字从6开始
### 使用方法
    # 在源代码中
    结尾的main函数的参数改成主文件夹的名字，这个文件夹会包含800X800,750X1000,800X1200文件夹

    # UI代码
    这是一个用于编写UI界面的代码，会保留主文件的功能，在输入框输入主文件夹的名字，这个文件夹会包含800X800,750X1000,800X1200文件夹

# color_div
这是一个用于分类不同颜色衣服(亦或是色卡)图片的程序，支持的颜色有：黑色，白色，杏色，粉红，浅紫，浅蓝，浅绿。其他的颜色不会被识别。
### 使用方法
    <!-- 在使用前要先初始化，使用init.py文件 -->
#### init的使用
    在init结尾的main函数调用里修改图片路径，这是初始化图片的路径，完整的路径类似于D:\\photo\\white.jpg，这里要注意，一定是\\而不是\。
    然后进行颜色识别，运行代码会弹出3个窗口，要调整颜色阈值，满足阈值的颜色会在一个窗口被白色标注，调整完阈值后调整面积，这个面积是被识别到的部分的矩形范围，大于这个面积会用绿色框框出。
    阈值调整完成后，滑动color滑块到对应的颜色的数字：

            0:'白色'
            1:'黑色'
            2:'浅紫'
            3:'粉红'
            4:'浅蓝'
            5:'浅绿'
            6:'杏色'

    调整完所有参数后，滑动save_color滑块到右侧完成特定颜色阈值的保存。
    然后用上述方法保存面积
    <!-- 面积只用保存一次 -->

#### main主文件的使用
    在文件结尾，main的调用，修改参数，将参数修改为主文件夹，这个文件夹会可能会包括很多文件夹，文件夹底下会有要分类的图片。
    运行代码，会自动创建文件夹，将对应颜色的图片放进对应的文件夹。
    <!-- 注意！空文件夹不会被删除 -->