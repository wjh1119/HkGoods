import pandas as pd
import os

def json2excel(json_url):


    df = pd.read_json(json_url)
    li=os.path.splitext(json_url)
    if li[1]==".json":
        newname=li[0]+".xlsx"
        os.rename(json_url,newname)
    output_excel(df,newname,index=False)
    

def output_excel(df, path, sheet_name="Sheet1", index=True, header=True):
    if type(path) != str:
        raise Exception("invalid param 'path'")

    if type(df) == pd.core.frame.DataFrame:
        writer = pd.ExcelWriter(path)
        df.to_excel(
            writer, sheet_name, index=index, header=header, encoding='utf-8')
        writer.save()
    elif type(df) == dict:
        writer = pd.ExcelWriter(path)
        for key in df:
            df[key].to_excel(
                writer, key, index=index, header=header, encoding='utf-8')
        writer.save()
    else:
        print("导入失败，请检查df")

if __name__ == "__main__":

    data_dir = './'
    json_url_list = [i for i in os.listdir(data_dir) if '.json' in i]
    print("有以下文件：")
    for i in json_url_list:
        print(i)

    for json_url in json_url_list:
        json2excel(json_url)
    print("转换完毕")