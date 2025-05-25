# 🎬 Lecture Tools: Video and Subtitle Processing Scripts

This repository contains two Python scripts designed to assist educators and content creators in processing lecture materials.

---

## 📁 Scripts Overview

### 1. `combine_mp4.py`

**Purpose:**
Combines multiple `.mp4` video files from subdirectories into a single video file using FFmpeg.

**Functionality:**

* Recursively searches subdirectories for `.mp4` files.
* Generates a temporary `input_list.txt` file listing all found videos.
* Utilizes FFmpeg to concatenate the videos into `combined_output.mp4`.
* Removes the temporary list file after processing.

**Usage:**
Ensure FFmpeg is installed and accessible via the command line.

Run the script:

```bash
python combine_mp4.py
```

([GitHub][1])

**Note:**
The script assumes that all `.mp4` files are compatible for concatenation (e.g., same codec and resolution).

---

### 2. `combine_srt_to_txt.py`

**Purpose:**
Merges multiple `.srt` subtitle files from subdirectories into a single `.txt` transcript.

**Functionality:**

* Traverses the `./subtitles` directory and its subfolders.
* Identifies `.srt` files and extracts their textual content.
* Removes timecodes and line numbers for a clean transcript.
* Appends each subtitle's content to `6300_combined_subtitles.txt`, prefixed by the filename.

**Usage:**
Place all subtitle folders within a directory named `subtitles`.([GitHub][2])

Run the script:

```bash
python combine_srt_to_txt.py
```



**Note:**
The script assumes that subtitle files are encoded in UTF-8.

---

## 🔧 Requirements

* Python 3.x
* FFmpeg installed and added to your system's PATH (for `combine_mp4.py`)([VideoHelp][3], [OTTVerse][4])
