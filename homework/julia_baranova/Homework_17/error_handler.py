import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument("folder", help="Path to the folder with logs")
parser.add_argument("text", help="Text need to be found")
args = parser.parse_args()


def program1(folder_path):
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            with open(file_path, 'r') as log_file:
                for line_number, line in enumerate(log_file, start=1):
                    words = line.split()
                    for i, word in enumerate(words):
                        if word == args.text:
                            start = max(i - 5, 0)
                            end = i + 6
                            snippet = words[start:end]
                            print(f"[{filename}] String {line_number}: {' '.join(snippet)}")


program1(args.folder)
