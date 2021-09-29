import os
import subprocess
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <mkv_file>")
        return

    mkv_file = sys.argv[1]
    mp4_file = mkv_file.replace(".mkv", ".mp4")
    
    #Replace with your own directory to FFMpeg :)
    cmd = "ffmpeg -i " + mkv_file + " -c:v copy -c:a copy " + mp4_file
    subprocess.call(cmd, shell=True)

if __name__ == "__main__":
    main()
