# tiktok-nav

This Flask app enables you to perform various actions on TikTok directly from your computer. (Android Only)

Due to suboptimal algorithm performance, it can effortlessly block bot accounts with a simple click.

![nav](https://github.com/NQevxvEtg/tiktok-nav/blob/main/app.png)

## Howto 
1. Download platform tools from https://developer.android.com/tools/releases/platform-tools
2. Update `path=/path` in all the shell scripts to your platform-tools path
3. Enable `Show taps` and `Pointer location` from Developer Options on your Android device
4. Update X and Y coordinates in all the shell scripts to match your phone screen coordinates
5. Install flask `pip install flask`
6. Update `script_path = home_path + '/path/` in tiktok.py to match your path
7. Run `python tiktok.py`
