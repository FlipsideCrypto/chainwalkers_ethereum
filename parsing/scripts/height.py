import json
import sys
import os

BASE_DIR = (os.path.abspath(os.path.dirname(__file__))).replace("/parsing/scripts", '')
sys.path.append(BASE_DIR)

from parsing.node import Node
from parsing.config import NODE_URL


def main():
    node = Node(NODE_URL)
    height = node.get_block_count()
    data = json.dumps({"height": height})
    sys.stdout.write(data)


if __name__ == "__main__":
    main()
