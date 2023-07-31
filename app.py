import certifi
import argparse
import os

def main():
    parser = argparse.ArgumentParser(
        prog='certifi-loader',
        description='loader certifi.',
        epilog='Copyright(r), 2023' 
    )
    parser.add_argument('--pemfilePath', default='./', required=False)
    args = parser.parse_args()
    pemfilePath =  os.listdir(args.pemfilePath)
    files = [file for file in pemfilePath if file.endswith('.pem')]
    cacert_path = certifi.where()
    for file in files:
        absoluteFilePath = os.path.join(args.pemfilePath, file)
        cmd = f"cat {absoluteFilePath} | tee -a {cacert_path}"
        if os.system(cmd) != 0:
            print(f"fail to excute{cmd}")
        else:
            print(f"{cmd} work!")


if __name__ == '__main__':
    main()
