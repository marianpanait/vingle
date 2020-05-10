from multiprocessing import Lock

from src.static.constants import Files


class FileManager:
    def __init__(self):
        self.lock = Lock()

    def append_to_file(self, data, file):
        self.lock.acquire()

        with open(file, 'a') as f:
            f.write(data)

        self.lock.release()

    def move_first_line_to_end(self, file):
        self.lock.acquire()
        with open(file, 'r+') as f:  # open file in read / write mode
            first_line = f.readline()  # read the first line and throw it out
            data = f.read()  # read the rest
            f.seek(0)  # set the cursor to the top of the file
            f.write(data)  # write the data back
            f.write(first_line)  # write the first line to the end
            f.truncate()  # set the file size to the current size
        self.lock.release()

    def get_first_line(self, file):
        self.lock.acquire()
        with open(file, 'r+') as f:  # open file in read / write mode
            first_line = f.readline()  # read the first line and throw it out
            data = f.read()  # read the rest
            f.seek(0)  # set the cursor to the top of the file
            f.write(data)  # write the data back
            f.write(first_line)  # write the first line to the end
            f.truncate()  # set the file size to the current size
        self.lock.release()

        return first_line.strip()

    def remove_line(self, file, data):
        self.lock.acquire()

        with open(file, 'r') as f:  # open file in read / write mode
            lines = f.readlines()

        with open(file, 'w') as f:  # open file in read / write mode
            for line in lines:
                if data not in line:
                    f.write(line)

        self.lock.release()
