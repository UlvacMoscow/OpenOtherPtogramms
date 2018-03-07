import subprocess
import os

source = 'Source'
result = 'result'
current_dir = os.path.dirname(os.path.abspath(__file__))
folder_source_way = os.path.join(current_dir, source)
list_dir = os.listdir(folder_source_way)

def source_cat(way):
    folder_result_way = os.path.join(current_dir, result)
    if not os.path.exists(folder_result_way):
        os.mkdir(folder_result_way)
    print(folder_result_way)
    source_way = os.path.join(folder_source_way, way)
    result_way = os.path.join(folder_result_way, way)
    subprocess.run('convert.exe {} -resize 200 {} '.format(source_way, result_way))
    print(source_way)


for cut in list_dir:
    source_cat(cut)
