import os
import sys
import shutil
import requests
import subprocess
from bs4 import BeautifulSoup


class Parser:
    def __init__(self):
        self.base_url: str = "https://www.acmicpc.net/problem/"
        self.html_text: str = None

        self.example_input: list[str] = []
        self.example_ouput: list[str] = []

        self.src_path: str = "/Users/kadragon/Dev/acmicpc_python/main.py"
        self.dst_path: str = None

    def make_url(self, problem_id):
        return self.base_url + str(problem_id)

    def get_html(self):
        problem_id = sys.argv[1]
        url = self.make_url(problem_id)

        headers = {
            'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/112.0.0.0 Safari/537.36 Edg/112.0.1722.48',
            'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9',
            'accept-encoding': 'gzip, deflate, br'
        }

        response = requests.get(url, headers=headers)
        self.html_text = response.text

    def get_example(self):
        soup = BeautifulSoup(self.html_text, 'html.parser')

        i: int = 1
        while True:
            try:
                sample_input = soup.find('pre', id=f'sample-input-{i}').text
                sample_output = soup.find('pre', id=f'sample-output-{i}').text

                self.example_input.append(sample_input)
                self.example_ouput.append(sample_output)

            except AttributeError:
                break

            i += 1

    def make_dir(self):
        folder_dir = int(sys.argv[1])
        root_dir = "/Users/kadragon/Dev/acmicpc_python/"

        self.dst_path = "%s%05d/%05d/" % (root_dir,
                                          (folder_dir//1000)*1000, folder_dir)

        print(self.dst_path)

        try:
            os.makedirs(self.dst_path)
        except FileExistsError:
            pass

    def make_file(self):
        shutil.copy(self.src_path, self.dst_path)

        for i in range(len(self.example_input)):
            with open(self.dst_path + f'_input{i+1}.txt', 'w') as f:
                f.write(self.example_input[i])

            with open(self.dst_path + f'_output{i+1}.txt', 'w') as f:
                f.write(self.example_ouput[i])


if __name__ == '__main__':
    parser = Parser()
    parser.get_html()
    parser.get_example()
    parser.make_dir()
    parser.make_file()
