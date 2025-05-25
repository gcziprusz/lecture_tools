import os

output_file = "6300_combined_subtitles.txt"
base_dir = "./subtitles"  # Change this if needed

with open(output_file, "w", encoding="utf-8") as outfile:
    for subfolder in os.listdir(base_dir):
        subfolder_path = os.path.join(base_dir, subfolder)
        if os.path.isdir(subfolder_path):
            for file in os.listdir(subfolder_path):
                if file.lower().endswith(".srt"):
                    srt_path = os.path.join(subfolder_path, file)
                    with open(srt_path, "r", encoding="utf-8") as infile:
                        lines = infile.readlines()
                        # Optional: Remove SRT timecodes and line numbers
                        clean_lines = [
                            line for line in lines 
                            if not line.strip().isdigit() 
                            and "-->" not in line
                        ]
                        outfile.write(f"\n--- {file} ---\n")
                        outfile.writelines(clean_lines)

