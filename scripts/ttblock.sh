#/bin/bash

path=/path

$path/platform-tools/adb shell input tap 985 1156
# $path/platform-tools/adb shell input swipe 925 2165 303 2165 250
sleep 0.6
$path/platform-tools/adb shell input tap 1000 192
sleep 0.6
$path/platform-tools/adb shell input swipe 925 2165 303 2165 250
sleep 0.6
$path/platform-tools/adb shell input tap 568 2165
sleep 0.6
$path/platform-tools/adb shell input tap 747 1670
sleep 0.6
$path/platform-tools/adb shell input tap 94 202
sleep 0.6
$path/platform-tools/adb shell input swipe 555 1850 555 1000 250
