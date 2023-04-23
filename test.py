import os
import sys
import subprocess


folder_dir = int(sys.argv[1])

dst_path = "%s%05d/%05d/" % ("/Users/kadragon/Dev/acmicpc_python/",
                             (folder_dir//1000)*1000, folder_dir)


print("=========================================")

i = 1
while True:
    input_data, output_data = "", ""
    if os.path.exists(dst_path + "input%d.txt" % (i)):
        with open(dst_path + "input%d.txt" % (i), "r") as f:
            input_data = f.read()

        with open(dst_path + "output%d.txt" % (i), "r") as f:
            output_data = f.read()

        result = subprocess.run(["python3", dst_path + "main.py"],
                                input=input_data, encoding="utf-8", stdout=subprocess.PIPE)

        if result.stdout != output_data:
            print("결과\n" + result.stdout)
            print("정답\n" + output_data, end="")
            print("=========================================")
    else:
        break

    i += 1
