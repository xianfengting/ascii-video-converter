
import argparse
from src.main import main

# 命令行输入参数处理
parser = argparse.ArgumentParser()
parser.add_argument('file')
parser.add_argument('-o', '--output')

if __name__ == "__main__":
    # 获取参数
    args = parser.parse_args()
    input_file = args.file
    output_file = args.output
    main(input_file, output_file)
