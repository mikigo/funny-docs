import os
import re
import time
from git import Repo, Git

def _words_count(markdown: str):
    chinese, english, codes = _split_markdown(markdown)
    code_lines = 0
    words = len(chinese) + len(english.split())
    for code in codes:
        code_lines += len(code.splitlines()) - 2
    read_time = round(words / 300 + code_lines / 80)
    return words, code_lines, read_time

def _split_markdown(markdown: str):
    markdown, codes = _clean_markdown(markdown)
    chinese = "".join(re.findall(r'[\u4e00-\u9fa5]', markdown))
    english = " ".join(re.findall(r'[a-zA-Z0-9]*?(?![a-zA-Z0-9])', markdown))
    return chinese, english, codes

def _clean_markdown(markdown: str):
    codes = re.findall(r'```[^\n].*?```', markdown, re.S)
    markdown = re.sub(r'```[^\n].*?```', '', markdown, flags=re.DOTALL | re.MULTILINE)
    markdown = re.sub(r'<!--.*?-->', '', markdown, flags=re.DOTALL | re.MULTILINE)
    markdown = markdown.replace('\t', '    ')
    markdown = re.sub(r'[ ]{2,}', '    ', markdown)
    markdown = re.sub(r'^\[[^]]*\][^(].*', '', markdown, flags=re.MULTILINE)
    markdown = re.sub(r'{#.*}', '', markdown)
    markdown = markdown.replace('\n', ' ')
    markdown = re.sub(r'!\[[^\]]*\]\([^)]*\)', '', markdown)
    markdown = re.sub(r'\[([^\]]*)\]\([^)]*\)', r'\1', markdown)
    markdown = re.sub(r'</?[^>]*>', '', markdown)
    markdown = re.sub(r'[#*`~\-–^=<>+|/:]', '', markdown)
    markdown = re.sub(r'\[[0-9]*\]', '', markdown)
    markdown = re.sub(r'[0-9#]*\.', '', markdown)
    return markdown, codes

def get_statistics(path, base):
    words, codes, read_time = 0, 0, 0
    path = os.path.join(base, path)
    if os.path.exists(path):
        for root, dirs, files in os.walk(path):
            for file in files:
                if file.endswith(".md"):
                    with open(os.path.join(root, file), "r", encoding="utf-8") as f:
                        markdown = f.read()
                        w, c, r = _words_count(markdown)
                        words += w
                        codes += c
                        read_time += r
    else:
        if path.endswith("/"):
            file = path[:-1] + ".md"
        else:
            file = path + ".md"
        if os.path.exists(file):
            with open(file, "r", encoding="utf-8") as f:
                markdown = f.read()
                words, codes, read_time = _words_count(markdown)
    return words, codes, read_time

_repo_cache = {}

def _get_repo(path: str) -> Git:
    """
    Get the git repository of the path.
    """

    if not os.path.isdir(path):
        path = os.path.dirname(path)

    if path not in _repo_cache:
        _repo_cache[path] = Repo(path, search_parent_directories=True).git
        
    return _repo_cache[path]

def get_latest_commit_timestamp(path: str) -> int:
    """
    Get the timestamp of the latest commit of the path.

    If no commit is found, return the current timestamp.
    """
    
    realpath = os.path.realpath(path)
    repo = _get_repo(realpath)

    commit_timestamp = repo.log(realpath, format="%at", n=1)

    if commit_timestamp == "":
        commit_timestamp = time.time()

    return int(commit_timestamp)

def get_update_time(path, base):
    path = os.path.join(base, path)
    if os.path.exists(path):
        time = 0
        for root, dirs, files in os.walk(path):
            for file in files:
                if len(files) != 1 and file == "index.md":
                    continue
                if file.endswith(".md"):
                    file = os.path.join(root, file)
                    time = max(time, get_latest_commit_timestamp(file))
        return time
    else:
        if path.endswith("/"):
            file = path[:-1] + ".md"
        else:
            file = path + ".md"
        if os.path.exists(file):
            return get_latest_commit_timestamp(file)
    return 0