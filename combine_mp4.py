import os
import subprocess

def collect_mp4_files_from_current_dir():
    mp4_files = []
    current_dir = os.getcwd()
    for item in os.listdir(current_dir):
        folder_path = os.path.join(current_dir, item)
        if os.path.isdir(folder_path):
            for file in os.listdir(folder_path):
                if file.lower().endswith('.mp4'):
                    full_path = os.path.join(folder_path, file)
                    mp4_files.append(full_path)
    return mp4_files

def combine_videos(input_files, output_file):
    # Create a temporary text file listing the input files
    with open('input_list.txt', 'w') as f:
        for file in input_files:
            f.write(f"file '{os.path.abspath(file)}'\n")
    
    # Run FFmpeg to concatenate the videos
    command = [
        'ffmpeg', '-f', 'concat', '-safe', '0',
        '-i', 'input_list.txt', '-c', 'copy', output_file
    ]
    
    subprocess.run(command, check=True)
    os.remove('input_list.txt')
    print(f"Combined video saved to {output_file}")

if __name__ == '__main__':
    # Collect MP4 files from all folders in the current directory
    mp4_files = collect_mp4_files_from_current_dir()

    # Sort files (optional for predictable order)
    mp4_files.sort()

    if not mp4_files:
        print("No MP4 files found in any folders.")
    else:
        combine_videos(mp4_files, 'combined_output.mp4')
