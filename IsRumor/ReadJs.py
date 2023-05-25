import os
import json
import xlwt

folder_path = r'E:\Rumor\weibo\rumdect\Weibo'  # 文件夹路径
workbook = xlwt.Workbook(encoding='utf-8')  # 新建一个Excel工作簿
worksheet = workbook.add_sheet('Sheet1')  # 新建一个工作表
worksheet.write(0, 0, '文件名')  # 设置表头
worksheet.write(0, 1, '文本')
worksheet.write(0, 2, '粉丝数')
row = 1  # 从第二行开始写入数据


filter_words=["转发微博。","轉發微博。","转发微博"]
for file_name in os.listdir(folder_path):
    if file_name.endswith('.json'):  # 如果文件是JSON文件
        file_path = os.path.join(folder_path, file_name)  # 拼接文件路径
        with open(file_path, 'rb') as f:
            row_cnt=0
            json_str = f.read()  # 读取JSON格式的字符串
            json_list = json.loads(json_str)  # 加载JSON数据
            original_text = json_list[0]['original_text']
            followers_count=json_list[0]["followers_count"]
            file_name_without_extension = file_name[:-5]
            worksheet.write(row, 0, file_name_without_extension)  # 设置文件名列
            worksheet.write(row, 1, original_text)  # 设置文本列
            worksheet.write(row,2, followers_count)  # 设置粉丝数列
            row += 1  # 行数加1

workbook.save('output.xls')  # 保存Excel工作簿