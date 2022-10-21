# TODO: Document all features

from flask import Flask, request, send_file
from werkzeug.exceptions import NotFound
from pathlib import Path
import argparse
import os
import sys
import glob

def die(msg):
    print(msg)
    sys.exit()

cli = argparse.ArgumentParser(description='Start an audio server for Yomichan')

cli.add_argument('-s', '--sort', 
                action='store_true',
                help="sort files by name to return a result with the highest priority")
cli.add_argument('-p', '--pattern', type=str, help="match files directly with this string")
cli.add_argument('-g', '--glob', type=str, help="match files using a valid glob expression")
cli.add_argument('-d',
                '--directories',
                nargs = "+",
                metavar='path',
                help='one or more valid directories containing audio files',
                required=True)

args = cli.parse_args()

paths = [Path(path) for path in args.directories if os.path.isdir(path)]

if not paths:
    die('No valid paths detected')

if args.sort:
    paths.sort()

def process_pattern(text, term, reading):
    concrete = text.replace("{term}", term).replace("{reading}", reading)
    if term not in concrete or reading not in concrete:
        die("Invalid pattern: does not consist of template literals")
    return concrete

def search(term, reading):
    # return a path to audio file
    glob_pattern = None
    pattern = f"{term}.mp3"
    if args.glob:
        glob_pattern = process_pattern(args.glob, term, reading)
    if args.pattern:
        pattern = process_pattern(args.pattern, term, reading)

    for source in paths:
        if glob_pattern:
            file_iter = glob.iglob(glob_pattern, root_dir=source)
            try:
                return next(file_iter)
            except:
                continue
        else:
            term_file = source / pattern
            if term_file.is_file():
                return str(term_file)

app = Flask(__name__)

@app.route("/", methods=["GET"])
def get_audio():
    file = search(request.args["expression"], request.args.get("reading", ""))
    if file is None:
        raise NotFound()
    return send_file(file)

if __name__ == '__main__':
    app.run()
