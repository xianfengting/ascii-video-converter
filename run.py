
import argparse
from src.main import main

# 命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o', '--output')
# 获取参数
args = parser.parse_args()
INPUT_FILE = args.file
OUTPUT_FILE = args.output

if __name__ == "__main__":
    main(INPUT_FILE, OUTPUT_FILE)
