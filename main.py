import module.gitPush.gitPush as gitPush
import module.markdownProcess.markdownProcess as markdownProcess
import json
from pathlib import Path


def main():
    global config
    with open('./config.json', 'r') as c_f:
        config = json.load(c_f)
    gitFolder = Path(config["gitFolder"])
    markdownProcess.main(config)
    gitPush.main(gitFolder)


if __name__ == "__main__":
    main()
