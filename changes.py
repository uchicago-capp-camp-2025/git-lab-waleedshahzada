import pathlib

def replace(filename, fro, to):
    print('replacing text in', filename)
    text = pathlib.Path(filename).read_text()
    text = text.replace(fro, to)
    pathlib.Path(filename).write_text(text)

if __name__ == "__main__":
    replace("text/time-machine.txt", "with red hair", "with green hair")
    replace("text/last-question.txt", "question", "?")
