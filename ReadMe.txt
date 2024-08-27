QuranQAGUI.Py requires the assets and model folders included in the first release of the program,
you'll have to download both parts of the 7zip file in order to extract those two folders.
Folder Names:
"model" & "assets" (assets is located in the _internal folder)

to compile QuranQA.py you need to install the required libraries in "requirements.txt" after creating your new environement in anaconda prompt.
Then install pyinstaller and use the following command to compile the gui application:
pyinstaller --windowed QuranQAGUI.Py
