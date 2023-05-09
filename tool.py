# 获取指纹浏览器使用端口
import psutil
import os

def get_url():
    url = "http://127.0.0.1:"
    for proc in psutil.process_iter():
        if proc.name() == '比特浏览器.exe':
            for x in proc.connections():
                if x.status == psutil.CONN_LISTEN:
                    url = url + str(x.laddr.port)
                    return url
    return None


# 写入文件
def write_file(file_name, data_list,mode= 'a'):
    path = r"%s/%s" % (os.getcwd(), file_name)
    wf = open(path, mode, newline="")
    wf.writelines(data_list)
    wf.close()


def open_txt(file_name):
    """
    一列一列返回txt列表数组
    :param file_name: 文件名字
    :return: [hi,hello,大家好]
    """

    lines = []
    with open(file_name, 'r', encoding="UTF-8") as file_to_read:
        ff = file_to_read.readlines()
        for line in ff:
            lines.append(line.rstrip("\n"))
    return lines

def clear_file(filename):
    with open(filename, "w") as file:
        file.write("")
