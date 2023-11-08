import pandas as pd
import os
from datetime import datetime

def judgeXlx(folder_path):
    keyword = "_test_case_stats"
    files = os.listdir(folder_path)
    desired_files = [file for file in files if keyword in file]
    return desired_files

def xlxToTxt(folder_path,target_file,txt_file_name):
       
    if target_file.endswith('.csv'):
        file_id = target_file[:-len('.csv')]
        # 如果文件是 CSV，使用 pandas 的 read_csv() 函数来读取
        df = pd.read_csv(folder_path+'/'+target_file)
    elif target_file.endswith('.xlsx'):
        file_id = target_file[:-len('.xlsx')]
        # 如果文件是 Excel，使用 pandas 的 read_excel() 函数来读取
        df = pd.read_excel(folder_path+'/'+target_file, engine='openpyxl')
     
    """获取表名"""
    keyword_to_remove = "_test_case_stats"
    file_id = file_id.replace(keyword_to_remove, '')

    # 删除文件后缀
    #df = pd.read_excel(target_file)
    print("找到文件，开始写入txt文件...")
    """获取文件创建时间"""
    if os.path.exists(folder_path+'/'+target_file):
        file_stats = os.stat(folder_path+'/'+target_file)
        create_time = file_stats.st_ctime
    total_data=[]
    create_date = datetime.fromtimestamp(create_time)
    formatted_date = create_date.strftime('%Y-%m-%d %H:%M:%S')
    print(formatted_date)
    column_count = df.shape[1]
    row_count = df.shape[0]
    
    """获取每一行样本对应模型及测试结果"""
    for j in range(0,row_count):
        for i in range(1,column_count):
            selected_data = []
            selected_data.append(file_id)
            sample_id = df.iloc[j,0]
            selected_data.append(sample_id)
            column_name = df.columns[i]
            model_name = column_name
            model_name_result = df.iloc[j,i]
            selected_data.append(model_name)
            selected_data.append(model_name_result)
            selected_data.append(create_time)
            total_data.append(selected_data)
    
    txt_file = txt_file_name
    # if os.path.exists(txt_file):
    #     os.remove(txt_file)
    #     print(f'已删除已存在的文件: {txt_file}')
    with open(txt_file,'w') as file:
        for item in total_data:
            for item1 in item[0:len(item)-1]:
                if item1 == "nan":
                    file.write('\t'+'\t')
                else:
                    file.write(str(item1)+'\t')
            
            file.write(formatted_date+'\n')
        
    print("txt文件写出成功。")

if __name__ == '__main__':
    """修改文件夹名称"""
    folder_path = './tests'
    
    if judgeXlx(folder_path) != []:
        print("---")
        for item in judgeXlx(folder_path):
            print(item)
            xlxToTxt(folder_path,item,txt_file_name='test3.txt')
    else:
        print("文件夹不存在目标文件。")
    