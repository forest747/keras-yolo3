import subprocess
import glob


def get_dir_list(pth):
    path = pth
    directory = glob.glob(path + '/*')
    return directory


dir_list = get_dir_list("/input")
dirs = {}
for ele in dir_list:
    if "many" in ele:
        target_dir = ele.split("/")[-1]
        files = get_dir_list("/input/" + target_dir)
        file_list = []
        for element in files:
            file_list.append(element.split("/")[-1])
    dirs[target_dir] = file_list

for key, values in dirs.items():
    for e in values:
        subprocess.call('python3 yolo_video.py --input /input/{0}/{1} --output /colab/output_test/{0}/{1}.mp4',
                        shell=True).foramt(key, e)


