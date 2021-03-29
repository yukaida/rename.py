# This is a sample Python script.
import os


# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    # Press Ctrl+F8 to toggle the breakpoint.
    # 输入文件夹地址
    path = r"E:\BaiduNetdiskDownload\024-掘金小册（前端小册+后端小册）\前端小册"
    fileParents = os.listdir(path)

    # 输出所有文件名，只是为了看一下
    for files in fileParents:
        dir = os.path.join(path, files)
        item = os.listdir(dir)
        for file in item:
            print(file)
            old = dir + os.sep + file
            # new是新名称的信息，这里的操作是删除了最前面的‘考拉很忙o - ‘共8个字符
            new = dir + os.sep + file.replace('[天下无鱼][shikey.com]', '')
            # 新旧替换
            os.rename(old, new)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
