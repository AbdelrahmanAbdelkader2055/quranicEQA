If The Program crashes at launch, then download the latest version of of Visual C++ Redist: https://github.com/abbodi1406/vcredist
If that didn't work, then download this dll file and copy it to your System32 folder https://www.dllme.com/dll/files/libomp140_x86_64/versions
QuranQAGUI.Py requires the assets and model folders included in the first release of the program,
you'll have to download both parts of the 7zip file in order to extract those two folders.
Folder Names:
"model" & "assets" (assets is located in the _internal folder)

to compile QuranQA.py you need to install the required libraries in "requirements.txt" after creating your new environement in anaconda prompt.
Then install pyinstaller and use the following command to compile the gui application:
pyinstaller --windowed QuranQAGUI.Py
