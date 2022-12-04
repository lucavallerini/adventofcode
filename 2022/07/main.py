#!/bin/env python3

import re

filename = 'input'
with open('input', 'r') as f:
    content = f.readlines()


DIR_MAX_SIZE = 100000
TOTAL_DISK_SPACE = 70000000
REQUIRED_FREE_SPACE = 30000000


def is_cd_cmd(line):
    matches = re.findall("(\$ cd )([a-zA-Z\.\/]+)", line)
    return False if len(matches) == 0 else matches[0][1]


def is_ls_cmd(line):
    return line == '$ ls'


def is_dir(line):
    matches = re.findall("(^dir )([a-zA-Z\.\/]+)", line)
    return False if len(matches) == 0 else matches[0][1]


def is_file(line):
    matches = re.findall("(^[0-9]+ )([a-zA-Z\.\/]+)", line)
    return False if len(matches) == 0 else [int(matches[0][0].replace(' ', '')), matches[0][1]]


def find_dir(target, dirs):
    for d in dirs:
        if d["name"] == target:
            return d


# { "name": "/", "dirs": [{ "name": "a", "dirs": [{ "name": "b", "dirs": [], "files": []}], "files": []}], "files": []}
def go_to_path(path, fs):
    # ['/', 'a', 'b'] -> /a/b
    if path[0] == "/":
        if len(path) == 1:
            return fs
        else:
            return go_to_path(path[1:], fs["dirs"])
    else:
        dir = find_dir(path[0], fs)
        if len(path) == 1:
            return dir
        else:
            return go_to_path(path[1:], dir["dirs"])


def update_dir_size(navigation, file_size, fs):
    dir = go_to_path(navigation, fs)
    dir["size"] += file_size
    if len(navigation) > 1:
        update_dir_size(navigation[:-1], file_size, fs)


fs = {}
def reconstruct_fs():
    navigation = []
    for l in content:
        line = l.replace('\n', '')
        if is_cd_cmd(line):
            dir_name = is_cd_cmd(line)
            if ( dir_name == ".." ):
                navigation = navigation[:len(navigation)-1]
            elif len(fs) == 0:
                # empty fs
                fs.update({
                    "name": dir_name,
                    "size": 0,
                    "dirs": [],
                    "files": []
                })
                navigation.append(dir_name)
            else:
                parent = go_to_path(navigation, fs)
                parent["dirs"].append({
                    "name": dir_name,
                    "size": 0,
                    "dirs": [],
                    "files": []
                })
                navigation.append(dir_name)
        elif is_file(line):
            file_stats = is_file(line)
            parent = go_to_path(navigation, fs)
            parent["files"].append({
                "name": file_stats[1],
                "size": file_stats[0]
            })
            update_dir_size(navigation, file_stats[0], fs)
        elif not is_ls_cmd(line) and not is_dir(line):
            print("Unexpected line: " + line)


def find_dirs_size(max_size, current_size, dirs):
    total_size = current_size
    for d in dirs:
        if d["size"] <= max_size:
            total_size += d["size"]
        if len(d["dirs"]) > 0:
            total_size = find_dirs_size(max_size, total_size, d["dirs"])
    return total_size


def collect_dir_sizes(collection, dirs):
    for d in dirs:
        collection.append(d["size"])
        if len(d["dirs"]) > 0:
            collect_dir_sizes(collection, d["dirs"])


reconstruct_fs()


total_size_below_threshold = find_dirs_size(DIR_MAX_SIZE, 0, fs["dirs"])
print("Total size under target: " + str(total_size_below_threshold))

total_size = fs["size"]
print("Disk space: " + str(TOTAL_DISK_SPACE))
print("Total size: " + str(total_size))

minimum_space_to_free = REQUIRED_FREE_SPACE - (TOTAL_DISK_SPACE - total_size)
print("Required to free at least: " + str(minimum_space_to_free))

dir_sizes = []
collect_dir_sizes(dir_sizes, fs["dirs"])
min_dir_size = min([s for s in dir_sizes if s >= minimum_space_to_free ])
print("Delete dir of size: " + str(min_dir_size))
