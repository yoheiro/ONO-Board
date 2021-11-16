# import sys
# from cx_Freeze import setup, Executable
 
# base = None
 
# if sys.platform == 'win32':
#     base = 'Win32GUI'
# # CUIの場合はこのif文をコメントアウトしてください。
 
# exe = Executable(script = "ono.py", base= base)
# # "main.py"にはpygameを用いて作成したファイルの名前を入れてください。
 
# setup(name = 'your_filename',
#     version = '0.1',
#     description = 'converter',
#     executables = [exe])

import sys
from cx_Freeze import setup, Executable
 
base = None
 
# if sys.platform == 'win32':
#     base = 'Win32GUI'
 
executables = [
   Executable('ono.py', base=base)
]
 
# appにパッケージ化するときのInfo.plistを指定する
bdist_mac_options = {
    'custom_info_plist': 'Info.plist',
}
includes = [] 
include_files = ['DB'] 
setup(name='ono',
      version='0.1',
      description='ono',
      options={'build_exe': {'includes': includes, 'include_files': include_files}},

      executables=executables)

# import cx_Freeze

# executables = [cx_Freeze.Executable("voiceToText.py")]

# import speech_recognition as sr
# from os import path
# base_path = path.dirname(path.abspath(sr.__file__))

# cx_Freeze.setup(
#     name="Sing it-Hear it",
#     options={
#         "build_exe": {
#             "packages":["speech_recognition", "pyaudio"],
#             "include_files": [path.join(base_path, "flac-win32.exe"), path.join(base_path, "flac-mac"), path.join(base_path, "flac-linux-x86"), path.join(base_path, "flac-linux-x86_64")],
#         }
#     },
#     executables = executables
# )