import os


def run(**args):
    print "[*] In dirlister module."
    files = os.listerdir(".")
    return str(files)
