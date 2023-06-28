import srt

def load_srt(filename):
    # load original .srt file
    # parse .srt file to list of subtitles
    print("Loading {}".format(filename))
    with open(filename) as f:
        text = f.read()
    return list(srt.parse(text))


def load_txt(filename):
    # load translated text file
    print("Loading {}".format(filename))
    with open(filename) as f:
        text = f.readlines()
    return text


def merge_srt(source, target, output, replace):
    subs = load_srt(source)
    lines = load_txt(target)
    f = open(output, 'w')
    for (s, l) in zip(subs, lines):
        if replace:
            s.content = l
        else:
            s.content += '\n' + l
    
    f.writelines(srt.compose(subs))

    f.close()
    


def main():
    import argparse

    parser = argparse.ArgumentParser()

    parser.add_argument(
        "--source",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--target",
        type=str,
        required=True,
    )
    parser.add_argument(
        "--output",
        type=str,
        default="output.srt",
    )
    parser.add_argument(
        "--replace",
        type=bool,
        default=False,
    )
    args = parser.parse_args()

    merge_srt(args.source, args.target, args.output, args.replace)


if __name__ == "__main__":
    main()