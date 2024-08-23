import codecs
import os
import yaml
import json

def json_to_yaml(filename:str):
    f = open(filename,"r",encoding="utf8")
    content = f.read()
    f.close()
    obj = json.loads(content)

    f = open(filename[:-4]+"yaml", "w")
    yaml.dump(obj, f, indent=4, allow_unicode=True)
    f.close()

def yaml_to_json(filename:str):
    f = open(filename,"r",encoding="utf8")
    content = f.read()
    obj = yaml.full_load(content)
    f.close()

    f = open(filename[:-4]+"json", "w")
    content = json.dumps(obj, indent=4)
    f.write(content)
    f.close()

def scan_folder(folder:str):
    files = os.listdir(folder)
    for fname in files:
        ext = fname[-5:].lower()
        if ext != '.json':
            continue
        
        fpath = os.path.join(folder, fname)
        print(fpath)
        # convert_gbk_to_utf8(fpath, fpath)
        json_to_yaml(fpath)


# def convert_gbk_to_utf8(input_file, output_file):
#     try:
#         with codecs.open(input_file, 'r', 'gbk') as f:
#             content = f.read()
#
#         # 将读取的内容以UTF-8编码写入新文件
#         with codecs.open(output_file, 'w', 'utf-8') as f:
#             f.write(content)
#
#         print(f"文件 {input_file} 已成功转换为UTF-8编码并保存为 {output_file}")
#
#     except UnicodeDecodeError as e:
#         print(f"无法将文件 {input_file} 转换为UTF-8编码: {e}")

if __name__ == "__main__":
    folder = "./"
    dirs = os.listdir(folder)
    for dname in dirs:        
        dpath = os.path.join(folder, dname)
        if not os.path.isdir(dpath):
            continue
        scan_folder(dpath)
