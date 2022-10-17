import os
txt_tables = []
ef2_name = input("请输入ef2文件路径及文件名：（格式：C:\\Users\\xx\\Desktop\\xxx.ef2）\n")
video_path = input("请输入批量下载视频文件路径：（格式：C:\\Users\\xxx\\Downloads\\Video）\n")
name_pop = input("请输入视频文件名中需要删除的字段：\n")
try:
    f = open(ef2_name, "r", encoding='utf-8')
    line = f.readline()  # 读取第一行
    https_list = []
    filename_list = []
    while line:
        if 'https://' in line and 'referer:' not in line:
            https_list.append(line)
        if 'filename: ' in line:
            filename_list.append(line.replace('filename: ', ''))
        line = f.readline()  # 读取下一行

    try:
        all_names = os.listdir(video_path)
        for i in range(len(all_names)):
            for j in range(len(https_list)):
                if all_names[i] in https_list[j]:
                    try:
                        os.rename(video_path + '\\' + all_names[i], video_path + '\\' +
                                  filename_list[j].replace(name_pop, '').replace('\n', ''))
                        print('将' + video_path + '\\' + all_names[i] + '替换为：' + video_path + '\\' +
                              filename_list[j].replace(name_pop, ''))
                    except:
                        pass
    except:
        print('文件夹路径格式错误。')
except:
    print('文件路径错误，找不到文件。')
print('重命名完成！')

