import os
import subprocess
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 mkv2mp4.py <mkv_file>")
        return

    mkv_file = sys.argv[1]
    mp4_file = mkv_file.replace(".mkv", ".mp4")

    cmd = "C:\\Users\\Megan\\Downloads\\ffmpeg-4.3.2-full_build-shared\\ffmpeg-4.3.2-2021-02-27-essentials_build\\bin\\ffmpeg -i " + mkv_file + " -c:v copy -c:a copy " + mp4_file
    subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    main()