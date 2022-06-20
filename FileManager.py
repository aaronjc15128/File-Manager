def main():
    import tkinter as tk
    from tkinter import filedialog

    import os
    import shutil
    import sys
    import webbrowser


    filetypesDIC = {
        ".aif": "Audio",
        ".cda": "Audio",
        ".mid": "Audio",
        ".midi": "Audio",
        ".mp3": "Audio",
        ".mpa": "Audio",
        ".ogg": "Audio",
        ".wav": "Audio",
        ".wma": "Audio",
        ".wpl": "Audio",
        ".7z": "Compressed",
        ".arj": "Compressed",
        ".deb": "Compressed",
        ".pkg": "Compressed",
        ".rar": "Compressed",
        ".rpm": "Compressed",
        ".z": "Compressed",
        ".zip": "Compressed",
        ".bin": "Disc & Media",
        ".dmg": "Disc & Media",
        ".iso": "Disc & Media",
        ".toast": "Disc & Media",
        ".vcd": "Disc & Media",
        ".csv": "Data & Database",
        ".dat": "Data & Database",
        ".db": "Data & Database",
        ".dbf": "Data & Database",
        ".log": "Data & Database",
        ".mdb": "Data & Database",
        ".sav": "Data & Database",
        ".sql": "Data & Database",
        ".tar": "Data & Database",
        ".xml": "Data & Database",
        ".email": "Email",
        ".eml": "Email",
        ".emix": "Email",
        ".msg": "Email",
        ".oft": "Email",
        ".ost": "Email",
        ".pst": "Email",
        ".vcf": "Email",
        ".apk": "Executable",
        ".bat": "Executable",
        ".bin": "Executable",
        ".cgi": "Executable",
        ".pl": "Executable",
        ".com": "Executable",
        ".exe": "Executable",
        ".gadget": "Executable",
        ".jar": "Executable",
        ".msi": "Executable",
        ".py": "Executable",
        ".wsf": "Executable",
        ".fnt": "Fonts",
        ".fon": "Fonts",
        ".otf": "Fonts",
        ".ttf": "Fonts",
        ".ai": "Images",
        ".bmp": "Images",
        ".gif": "Images",
        ".iso": "Images",
        ".jpeg": "Images",
        ".jpg": "Images",
        ".png": "Images",
        ".ps": "Images",
        ".psd": "Images",
        ".svg": "Images",
        ".tif": "Images",
        ".tiff": "Images",
        ".key": "Presentations",
        ".odp": "Presentations",
        ".pps": "Presentations",
        ".ppt": "Presentations",
        ".pptx": "Presentations",
        ".ods": "Spreadsheets",
        ".xls": "Spreadsheets",
        ".xlsm": "Spreadsheets",
        ".xlsx": "Spreadsheets",
        ".3g2": "Video",
        ".3gp": "Video",
        ".avi": "Video",
        ".flv": "Video",
        ".h264": "Video",
        ".m4v": "Video",
        ".mkv": "Video",
        ".mov": "Video",
        ".mp4": "Video",
        ".mpg": "Video",
        ".mpeg": "Video",
        ".rm": "Video",
        ".swf": "Video",
        ".vob": "Video",
        ".wmv": "Video",
        ".doc": "Word Processor",
        ".docx": "Word Processor",
        ".pdf": "Word Processor",
        ".rtf": "Word Processor",
        ".tex": "Word Processor",
        ".txt": "Word Processor",
        ".wpd": "Word Processor"
    }


    def RaiseFrame(frame, **kwargs):
        frame.grid(row=0, column=0)
        frame.config(background="#181818")
        frame.tkraise()
        if "hide" in kwargs:
            kwargs["hide"].grid_forget()


    if getattr(sys, 'frozen', False):
        application_path = os.path.dirname(sys.executable)
    elif __file__:
        application_path = os.path.dirname(__file__)


    root  = tk.Tk()

    root.iconbitmap(os.path.join(application_path, "Icon.ico"))
    root.title("File Manager - Aaron Chauhan")
    root.config(background="#181818")

    def SetWindowSize(window_width, window_height):
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        
        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


    # frames
    f1 = tk.Frame(root)
    f2 = tk.Frame(root)
    f3 = tk.Frame(root)
    f4 = tk.Frame(root)

    for frame in {f1, f2, f3, f4}:
        frame.grid(row=0, column=0, sticky="NESW")
        frame.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)

        frame.config(background="#181818")


    # setup
    SetWindowSize(600, 800)


    # backup
    def ClearBackup():
        try:
            for file in os.listdir(os.path.join(application_path, "backup\\undo_button")):
                os.remove(os.path.join(application_path, "backup\\undo_button", file))
        except (FileExistsError, PermissionError) as e:
            for folder in os.listdir(os.path.join(application_path, "backup\\undo_button")):
                shutil.rmtree(os.path.join(application_path, "backup\\undo_button", folder))
        except FileNotFoundError:
            pass
        
        try:
            os.rmdir(os.path.join(application_path, "backup\\undo_button"))
        except FileNotFoundError:
            return
    ClearBackup()

    def CreateBackup():
        shutil.copytree(path, os.path.join(application_path, "backup\\undo_button"))


    # f1
    tk.Label(f1, text="File Manager", fg="#FFFFFF", bg="#181818", font=("Roboto", 32)).pack()
    tk.Label(f1, text="by Aaron Chauhan", fg="#FFFFFF", bg="#181818", font=("Roboto", 15)).pack()
    for _ in range(3): tk.Label(f1, bg="#181818").pack()
    tk.Label(f1, text="Please put all files to sort in a folder", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
    for _ in range(3): tk.Label(f1, bg="#181818").pack()

    tk.Label(f1, text="Enter path of folder:", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()

    svpath = tk.StringVar()
    path_entry = tk.Entry(f1, textvariable=svpath, width=100)
    path_entry.pack()

    tk.Label(f1, bg="#181818").pack()

    def browsefiles():
        path_fdad = filedialog.askdirectory(initialdir = "/", title = "Select Path")
        path_entry.delete(0, tk.END)
        path_entry.insert(0, path_fdad)
    tk.Button(f1, text="Browse", command=browsefiles).pack()

    def showfiles():
        global path
        path = svpath.get()

        global files
        files = os.listdir(path)
        filesStr = ""
        for file in files:
            filesStr += f"{file}\n"
        filesStr.strip()

        filestofont = {78:1, 54:2, 31:4, 22:6, 14:8, 0:12}

        for key in filestofont:
            if len(files) > key:
                filesLabel.config(font=("Roboto", filestofont[key]))
                break

        filesLabel.config(text=filesStr)
        filesLabel.pack()
    tk.Button(f1, text="Show Files", command=showfiles).pack()
    
    def submitbtn():
        if os.path.isdir(str(svpath.get())) and os.path.exists(str(svpath.get())):
            pass
        else:
            return
        
        RaiseFrame(f2, hide=f1)
        SetWindowSize(260, 650)

        global path
        path = svpath.get()

        global files
        files = os.listdir(path)

        SortMenu()
    tk.Button(f1, text="Submit", command=submitbtn).pack()
    
    for _ in range(5): tk.Label(f1, bg="#181818").pack()
    tk.Label(f1, text="Files to Sort:", fg="#FFFFFF", bg="#181818", font=("Roboto", 15)).pack()
    filesLabel = tk.Label(f1, fg="#FFFFFF", bg="#181818")


    def UseAgain_samepath():
        ClearBackup()
        CreateBackup()
        
        RaiseFrame(f2, hide=f3)
        RaiseFrame(f2, hide=f4)

        SetWindowSize(260, 650)

        global path
        path = svpath.get()

        global files
        files = os.listdir(path)

        for widget in f4.winfo_children():
            widget.destroy()
        
        for widget in f3.winfo_children():
            widget.destroy()

    def UseAgain_diffpath():
        ClearBackup()
        
        RaiseFrame(f1, hide=f3)
        RaiseFrame(f1, hide=f4)
        
        SetWindowSize(600, 800)

        for widget in f4.winfo_children():
            widget.destroy()
        
        for widget in f3.winfo_children():
            widget.destroy()

        for widget in f2.winfo_children():
            widget.destroy()


    # f2
    def SortMenu():
        CreateBackup()

        def undobtn(undo_button_widget):
            for file in os.listdir(path):
                try:
                    shutil.rmtree(os.path.join(path, file))
                except NotADirectoryError:
                    os.remove(os.path.join(path, file))
            
            for file in os.listdir(os.path.join(application_path, "backup\\undo_button")):
                shutil.move(os.path.join(application_path, "backup\\undo_button", file), path)

            undo_button_widget.destroy()

            
        
        def btn1():
            RaiseFrame(f3, hide=f2)
            
            SetWindowSize(700, 800)
            

            extensions = []
            for file in files:
                extension = "." + file.split(".")[len(file.split(".")) - 1]
                if extension in extensions:
                    pass
                else:
                    extensions.append(extension)
            for extension in extensions:
                os.mkdir(os.path.join(path, extension))
            for file in files:
                os.rename(os.path.join(path, file), os.path.join(path, "." + file.split(".")[len(file.split(".")) - 1], file))
            
            tk.Label(f3, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            ub = tk.Button(f3, text="Undo changes", command=lambda:undobtn(ub))
            ub.pack()
            tk.Button(f3, text="Use again with same path", command=UseAgain_samepath).pack()
            tk.Button(f3, text="Use again with different path", command=UseAgain_diffpath).pack()
            tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()

            for _ in range(3): tk.Label(f3, bg="#181818").pack()
            tk.Label(f3, text="File Manager", fg="#FFFFFF", bg="#181818", font=("Roboto", 26)).pack()
            tk.Label(f3, text="by Aaron Chauhan", fg="#FFFFFF", bg="#181818", font=("Roboto", 18)).pack()
            tk.Label(f3, bg="#181818").pack()
            tk.Label(f3, text="Links:", fg="#FFFFFF", bg="#181818", font=("Roboto", 14)).pack()
            ghlink = tk.Label(f3, text="Check out the GitHub page!", fg="#FFFFFF", bg="#181818", font=("Roboto", 12), cursor="hand2")
            ghlink.pack()
            ghlink.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/aaronjc15128/File-Manager"))
        def btn2():
            RaiseFrame(f3, hide=f2)
            
            SetWindowSize(750, 800)
            

            extensions = []
            for file in files:
                extension = "." + file.split(".")[len(file.split(".")) - 1]
                if extension in extensions:
                    pass
                else:
                    extensions.append(extension)
            types = []
            for extension in extensions:
                if extension in filetypesDIC:
                    type = filetypesDIC[extension]
                    if type in types:
                        pass
                    else:
                        types.append(type)
                else:
                    pass
            for type in types:
                os.mkdir(os.path.join(path, type))
            miscellaneous = False
            for file in files:
                extension = "." + file.split(".")[len(file.split(".")) - 1]
                if extension in filetypesDIC:
                    os.rename(os.path.join(path, file), os.path.join(path, filetypesDIC[extension], file))
                elif miscellaneous == False:
                    os.mkdir(os.path.join(path, "Miscellaneous"))
                    os.rename(os.path.join(path, file), os.path.join(path, "Miscellaneous", file))
                    miscellaneous = True
                else:
                    os.rename(os.path.join(path, file), os.path.join(path, "Miscellaneous", file))
            
            tk.Label(f3, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            ub = tk.Button(f3, text="Undo changes", command=lambda:undobtn(ub))
            ub.pack()
            tk.Button(f3, text="Use again with same path", command=UseAgain_samepath).pack()
            tk.Button(f3, text="Use again with different path", command=UseAgain_diffpath).pack()
            tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()

            for _ in range(3): tk.Label(f3, bg="#181818").pack()
            tk.Label(f3, text="File Manager", fg="#FFFFFF", bg="#181818", font=("Roboto", 26)).pack()
            tk.Label(f3, text="by Aaron Chauhan", fg="#FFFFFF", bg="#181818", font=("Roboto", 18)).pack()
            tk.Label(f3, bg="#181818").pack()
            tk.Label(f3, text="Links:", fg="#FFFFFF", bg="#181818", font=("Roboto", 14)).pack()
            ghlink = tk.Label(f3, text="Check out the GitHub page!", fg="#FFFFFF", bg="#181818", font=("Roboto", 12), cursor="hand2")
            ghlink.pack()
            ghlink.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/aaronjc15128/File-Manager"))
        def btn3():
            RaiseFrame(f3, hide=f2)
            
            SetWindowSize(750, 800)
            

            extensions = []
            for file in files:
                extension = "." + file.split(".")[len(file.split(".")) - 1]
                if extension in extensions:
                    pass
                else:
                    extensions.append(extension)
            types = []
            for extension in extensions:
                if extension in filetypesDIC:
                    type = filetypesDIC[extension]
                    if type in types:
                        pass
                    else:
                        types.append(type)
                else:
                    pass
            for type in types:
                os.mkdir(os.path.join(path, type))
            for extension in extensions:
                os.mkdir(os.path.join(path, filetypesDIC[extension], extension))
            for file in files:
                extension = "." + file.split(".")[len(file.split(".")) - 1]
                os.rename(os.path.join(path, file), os.path.join(path, filetypesDIC[extension], extension, file))
            
            tk.Label(f3, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            ub = tk.Button(f3, text="Undo changes", command=lambda:undobtn(ub))
            ub.pack()
            tk.Button(f3, text="Use again with same path", command=UseAgain_samepath).pack()
            tk.Button(f3, text="Use again with different path", command=UseAgain_diffpath).pack()
            tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()

            for _ in range(3): tk.Label(f3, bg="#181818").pack()
            tk.Label(f3, text="File Manager", fg="#FFFFFF", bg="#181818", font=("Roboto", 26)).pack()
            tk.Label(f3, text="by Aaron Chauhan", fg="#FFFFFF", bg="#181818", font=("Roboto", 18)).pack()
            tk.Label(f3, bg="#181818").pack()
            tk.Label(f3, text="Links:", fg="#FFFFFF", bg="#181818", font=("Roboto", 14)).pack()
            ghlink = tk.Label(f3, text="Check out the GitHub page!", fg="#FFFFFF", bg="#181818", font=("Roboto", 12), cursor="hand2")
            ghlink.pack()
            ghlink.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/aaronjc15128/File-Manager"))
        def btn4():
            RaiseFrame(f3, hide=f2)
            
            SetWindowSize(210, 120)


            tk.Label(f3, text="Number of characters in prefix:", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            svprefixchar = tk.StringVar()
            tk.Entry(f3, textvariable=svprefixchar, width=30).pack()
            def submitbtnf2():
                try:
                    _prefixchar = int(svprefixchar.get())
                except:
                    return
                
                
                RaiseFrame(f4, hide=f3)
                
                prefixchar = int(svprefixchar.get())

                prefixes = []
                for file in files:
                    prefix = file[:prefixchar]
                    if prefix in prefixes:
                        pass
                    else:
                        prefixes.append(prefix)
                for prefix in prefixes:
                    os.mkdir(os.path.join(path, prefix))
                for file in files:
                    os.rename(os.path.join(path, file), os.path.join(path, file[:prefixchar], file))
            
                SetWindowSize(750, 900)

                tk.Label(f4, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
                ub = tk.Button(f4, text="Undo changes", command=lambda:undobtn(ub))
                ub.pack()
                tk.Button(f4, text="Use again with same path", command=UseAgain_samepath).pack()
                tk.Button(f4, text="Use again with different path", command=UseAgain_diffpath).pack()
                tk.Button(f4, text="Exit", command=lambda:root.destroy()).pack()

                for _ in range(3): tk.Label(f4, bg="#181818").pack()
                tk.Label(f4, text="File Manager", fg="#FFFFFF", bg="#181818", font=("Roboto", 26)).pack()
                tk.Label(f4, text="by Aaron Chauhan", fg="#FFFFFF", bg="#181818", font=("Roboto", 18)).pack()
                tk.Label(f4, bg="#181818").pack()
                tk.Label(f4, text="Links:", fg="#FFFFFF", bg="#181818", font=("Roboto", 14)).pack()
                ghlink = tk.Label(f4, text="Check out the GitHub page!", fg="#FFFFFF", bg="#181818", font=("Roboto", 12), cursor="hand2")
                ghlink.pack()
                ghlink.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/aaronjc15128/File-Manager"))
            tk.Label(f3, bg="#181818").pack()
            tk.Button(f3, text="Submit", command=submitbtnf2).pack()
        def btn5():
            RaiseFrame(f3, hide=f2)
            
            SetWindowSize(180, 120)


            tk.Label(f3, text="Prefix:", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            svprefixchar = tk.StringVar()
            tk.Entry(f3, textvariable=svprefixchar, width=30).pack()
            def submitbtnf2():
                for c in {"<", ">", ":", '"', "/", " \ ".strip(), "|", "?", "*"}:
                    if c in str(svprefixchar.get()):
                        return
                
                RaiseFrame(f4, hide=f3)
                
                prefixchar = str(svprefixchar.get()) + " "

                for file in files:
                    os.rename(os.path.join(path, file), os.path.join(path, prefixchar + file))
            
                SetWindowSize(750, 900)

                tk.Label(f4, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
                ub = tk.Button(f4, text="Undo changes", command=lambda:undobtn(ub))
                ub.pack()
                tk.Button(f4, text="Use again with same path", command=UseAgain_samepath).pack()
                tk.Button(f4, text="Use again with different path", command=UseAgain_diffpath).pack()
                tk.Button(f4, text="Exit", command=lambda:root.destroy()).pack()

                for _ in range(3): tk.Label(f4, bg="#181818").pack()
                tk.Label(f4, text="File Manager", fg="#FFFFFF", bg="#181818", font=("Roboto", 26)).pack()
                tk.Label(f4, text="by Aaron Chauhan", fg="#FFFFFF", bg="#181818", font=("Roboto", 18)).pack()
                tk.Label(f4, bg="#181818").pack()
                tk.Label(f4, text="Links:", fg="#FFFFFF", bg="#181818", font=("Roboto", 14)).pack()
                ghlink = tk.Label(f4, text="Check out the GitHub page!", fg="#FFFFFF", bg="#181818", font=("Roboto", 12), cursor="hand2")
                ghlink.pack()
                ghlink.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/aaronjc15128/File-Manager"))
            tk.Label(f3, bg="#181818").pack()
            tk.Button(f3, text="Submit", command=submitbtnf2).pack()
        def btn6():
            RaiseFrame(f3, hide=f2)
            
            SetWindowSize(700, 800)
            

            units = {
                "b":0.125,
                "B":1,
                "KB":1024,
                "MB":1048576,
                "GB":1073741824,
                "TB":1099511627776,
                "PB":1125899906842624
            }


            for file in files:
                filesize = os.path.getsize(os.path.join(path, file))
                
                if filesize == 0:
                    strfs = "0B"
                else:
                    if filesize / units["b"] >= 8:
                        if filesize / units["B"] >= 1024:
                            if filesize / units["KB"] >= 1024:
                                if filesize / units["MB"] >= 1024:
                                    if filesize / units["GB"] >= 1024:
                                        if filesize / units["TB"] >= 1024:
                                            if filesize / units["PB"] >= 1024:
                                                unit = "PB"
                                            else:
                                                unit = "PB"
                                        else:
                                            unit = "TB"
                                    else:
                                        unit = "GB"
                                else:
                                    unit = "MB"
                            else:
                                unit = "KB"
                        else:
                            unit = "B"
                    else:
                        unit = "b"

                    strfs = str(round(filesize/units[unit], 2))+unit

                os.rename(os.path.join(path, file), os.path.join(path, f"{strfs} {file}"))
            
            tk.Label(f3, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            ub = tk.Button(f3, text="Undo changes", command=lambda:undobtn(ub))
            ub.pack()
            tk.Button(f3, text="Use again with same path", command=UseAgain_samepath).pack()
            tk.Button(f3, text="Use again with different path", command=UseAgain_diffpath).pack()
            tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()

            for _ in range(3): tk.Label(f3, bg="#181818").pack()
            tk.Label(f3, text="File Manager", fg="#FFFFFF", bg="#181818", font=("Roboto", 26)).pack()
            tk.Label(f3, text="by Aaron Chauhan", fg="#FFFFFF", bg="#181818", font=("Roboto", 18)).pack()
            tk.Label(f3, bg="#181818").pack()
            tk.Label(f3, text="Links:", fg="#FFFFFF", bg="#181818", font=("Roboto", 14)).pack()
            ghlink = tk.Label(f3, text="Check out the GitHub page!", fg="#FFFFFF", bg="#181818", font=("Roboto", 12), cursor="hand2")
            ghlink.pack()
            ghlink.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/aaronjc15128/File-Manager"))
        def btn7():
            RaiseFrame(f3, hide=f2)
            
            SetWindowSize(700, 800)
            

            for file in files:
                os.rename(os.path.join(path, file), os.path.join(path, "." + file.split(".")[len(file.split(".")) - 1] + " " + file))
            
            tk.Label(f3, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            ub = tk.Button(f3, text="Undo changes", command=lambda:undobtn(ub))
            ub.pack()
            tk.Button(f3, text="Use again with same path", command=UseAgain_samepath).pack()
            tk.Button(f3, text="Use again with different path", command=UseAgain_diffpath).pack()
            tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()

            for _ in range(3): tk.Label(f3, bg="#181818").pack()
            tk.Label(f3, text="File Manager", fg="#FFFFFF", bg="#181818", font=("Roboto", 26)).pack()
            tk.Label(f3, text="by Aaron Chauhan", fg="#FFFFFF", bg="#181818", font=("Roboto", 18)).pack()
            tk.Label(f3, bg="#181818").pack()
            tk.Label(f3, text="Links:", fg="#FFFFFF", bg="#181818", font=("Roboto", 14)).pack()
            ghlink = tk.Label(f3, text="Check out the GitHub page!", fg="#FFFFFF", bg="#181818", font=("Roboto", 12), cursor="hand2")
            ghlink.pack()
            ghlink.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/aaronjc15128/File-Manager"))
        def btn8():
            RaiseFrame(f3, hide=f2)
            
            SetWindowSize(700, 800)
            

            for file in files:
                os.rename(os.path.join(path, file), os.path.join(path, filetypesDIC["." + file.split(".")[len(file.split(".")) - 1]] + " " + file))
            
            tk.Label(f3, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            ub = tk.Button(f3, text="Undo changes", command=lambda:undobtn(ub))
            ub.pack()
            tk.Button(f3, text="Use again with same path", command=UseAgain_samepath).pack()
            tk.Button(f3, text="Use again with different path", command=UseAgain_diffpath).pack()
            tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()

            for _ in range(3): tk.Label(f3, bg="#181818").pack()
            tk.Label(f3, text="File Manager", fg="#FFFFFF", bg="#181818", font=("Roboto", 26)).pack()
            tk.Label(f3, text="by Aaron Chauhan", fg="#FFFFFF", bg="#181818", font=("Roboto", 18)).pack()
            tk.Label(f3, bg="#181818").pack()
            tk.Label(f3, text="Links:", fg="#FFFFFF", bg="#181818", font=("Roboto", 14)).pack()
            ghlink = tk.Label(f3, text="Check out the GitHub page!", fg="#FFFFFF", bg="#181818", font=("Roboto", 12), cursor="hand2")
            ghlink.pack()
            ghlink.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/aaronjc15128/File-Manager"))
        def btn9():
            RaiseFrame(f3, hide=f2)
            
            SetWindowSize(180, 120)


            tk.Label(f3, text="Prefix:", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            svprefix = tk.StringVar()
            tk.Entry(f3, textvariable=svprefix, width=30).pack()
            def submitbtnf2():
                RaiseFrame(f4, hide=f3)

                prefix = str(svprefix.get()) + " "

                for file in files:
                    if file.startswith(prefix) == True:
                        os.remove(os.path.join(path, file))


                SetWindowSize(750, 900)

                tk.Label(f4, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
                ub = tk.Button(f4, text="Undo changes", command=lambda:undobtn(ub))
                ub.pack()
                tk.Button(f4, text="Use again with same path", command=UseAgain_samepath).pack()
                tk.Button(f4, text="Use again with different path", command=UseAgain_diffpath).pack()
                tk.Button(f4, text="Exit", command=lambda:root.destroy()).pack()

                for _ in range(3): tk.Label(f4, bg="#181818").pack()
                tk.Label(f4, text="File Manager", fg="#FFFFFF", bg="#181818", font=("Roboto", 26)).pack()
                tk.Label(f4, text="by Aaron Chauhan", fg="#FFFFFF", bg="#181818", font=("Roboto", 18)).pack()
                tk.Label(f4, bg="#181818").pack()
                tk.Label(f4, text="Links:", fg="#FFFFFF", bg="#181818", font=("Roboto", 14)).pack()
                ghlink = tk.Label(f4, text="Check out the GitHub page!", fg="#FFFFFF", bg="#181818", font=("Roboto", 12), cursor="hand2")
                ghlink.pack()
                ghlink.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/aaronjc15128/File-Manager"))
            tk.Label(f3, bg="#181818").pack()
            tk.Button(f3, text="Submit", command=submitbtnf2).pack()  
        def btn10():
            RaiseFrame(f3, hide=f2)
            
            SetWindowSize(180, 120)


            tk.Label(f3, text="File Extension:", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            svextension = tk.StringVar()
            tk.Entry(f3, textvariable=svextension, width=30).pack()
            def submitbtnf2():
                RaiseFrame(f4, hide=f3)
                
                extension = str(svextension.get())

                for file in files:
                    if "." + file.split(".")[len(file.split(".")) - 1] == extension:
                        os.remove(os.path.join(path, file))


                SetWindowSize(750, 900)

                tk.Label(f4, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
                ub = tk.Button(f4, text="Undo changes", command=lambda:undobtn(ub))
                ub.pack()
                tk.Button(f4, text="Use again with same path", command=UseAgain_samepath).pack()
                tk.Button(f4, text="Use again with different path", command=UseAgain_diffpath).pack()
                tk.Button(f4, text="Exit", command=lambda:root.destroy()).pack()

                for _ in range(3): tk.Label(f4, bg="#181818").pack()
                tk.Label(f4, text="File Manager", fg="#FFFFFF", bg="#181818", font=("Roboto", 26)).pack()
                tk.Label(f4, text="by Aaron Chauhan", fg="#FFFFFF", bg="#181818", font=("Roboto", 18)).pack()
                tk.Label(f4, bg="#181818").pack()
                tk.Label(f4, text="Links:", fg="#FFFFFF", bg="#181818", font=("Roboto", 14)).pack()
                ghlink = tk.Label(f4, text="Check out the GitHub page!", fg="#FFFFFF", bg="#181818", font=("Roboto", 12), cursor="hand2")
                ghlink.pack()
                ghlink.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/aaronjc15128/File-Manager"))
            tk.Label(f3, bg="#181818").pack()
            tk.Button(f3, text="Submit", command=submitbtnf2).pack()
        def btn11():
            RaiseFrame(f3, hide=f2)
            
            SetWindowSize(180, 120)


            tk.Label(f3, text="File Type:", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            svtype = tk.StringVar()
            tk.Entry(f3, textvariable=svtype, width=30).pack()
            def submitbtnf2():
                RaiseFrame(f4, hide=f3)
                
                type = str(svtype.get())

                for file in files:
                    if filetypesDIC["." + file.split(".")[len(file.split(".")) - 1]].lower() == type.lower():
                        os.remove(os.path.join(path, file))


                SetWindowSize(750, 900)

                tk.Label(f4, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
                ub = tk.Button(f4, text="Undo changes", command=lambda:undobtn(ub))
                ub.pack()
                tk.Button(f4, text="Use again with same path", command=UseAgain_samepath).pack()
                tk.Button(f4, text="Use again with different path", command=UseAgain_diffpath).pack()
                tk.Button(f4, text="Exit", command=lambda:root.destroy()).pack()

                for _ in range(3): tk.Label(f4, bg="#181818").pack()
                tk.Label(f4, text="File Manager", fg="#FFFFFF", bg="#181818", font=("Roboto", 26)).pack()
                tk.Label(f4, text="by Aaron Chauhan", fg="#FFFFFF", bg="#181818", font=("Roboto", 18)).pack()
                tk.Label(f4, bg="#181818").pack()
                tk.Label(f4, text="Links:", fg="#FFFFFF", bg="#181818", font=("Roboto", 14)).pack()
                ghlink = tk.Label(f4, text="Check out the GitHub page!", fg="#FFFFFF", bg="#181818", font=("Roboto", 12), cursor="hand2")
                ghlink.pack()
                ghlink.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/aaronjc15128/File-Manager"))
            tk.Label(f3, bg="#181818").pack()
            tk.Button(f3, text="Submit", command=submitbtnf2).pack()
        def btn12():
            RaiseFrame(f3, hide=f2)
            
            SetWindowSize(180, 120)


            tk.Label(f3, text="Type DELETE to confirm:", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            svconfirm = tk.StringVar()
            tk.Entry(f3, textvariable=svconfirm, width=30).pack()
            def submitbtnf2():
                RaiseFrame(f4, hide=f3)
                
                confirm = str(svconfirm.get())

                if confirm.lower() == "delete":
                    for file in files:
                        os.remove(os.path.join(path, file))


                    SetWindowSize(750, 900)

                    tk.Label(f4, text=f"DELETED Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
                    ub = tk.Button(f4, text="Undo changes", command=lambda:undobtn(ub))
                    ub.pack()
                    tk.Button(f4, text="Use again with same path", command=UseAgain_samepath).pack()
                    tk.Button(f4, text="Use again with different path", command=UseAgain_diffpath).pack()
                    tk.Button(f4, text="Exit", command=lambda:root.destroy()).pack()

                    for _ in range(3): tk.Label(f4, bg="#181818").pack()
                    tk.Label(f4, text="File Manager", fg="#FFFFFF", bg="#181818", font=("Roboto", 26)).pack()
                    tk.Label(f4, text="by Aaron Chauhan", fg="#FFFFFF", bg="#181818", font=("Roboto", 18)).pack()
                    tk.Label(f4, bg="#181818").pack()
                    tk.Label(f4, text="Links:", fg="#FFFFFF", bg="#181818", font=("Roboto", 14)).pack()
                    ghlink = tk.Label(f4, text="Check out the GitHub page!", fg="#FFFFFF", bg="#181818", font=("Roboto", 12), cursor="hand2")
                    ghlink.pack()
                    ghlink.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/aaronjc15128/File-Manager"))
                else:
                    SetWindowSize(750, 900)

                    tk.Label(f4, text=f"DID NOT sort files in {path}\n(Incorrect Confirmation)", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
                    tk.Button(f4, text="Use again with same path", command=UseAgain_samepath).pack()
                    tk.Button(f4, text="Use again with different path", command=UseAgain_diffpath).pack()
                    tk.Button(f4, text="Exit", command=lambda:root.destroy()).pack()

                    for _ in range(3): tk.Label(f4, bg="#181818").pack()
                    tk.Label(f4, text="File Manager", fg="#FFFFFF", bg="#181818", font=("Roboto", 26)).pack()
                    tk.Label(f4, text="by Aaron Chauhan", fg="#FFFFFF", bg="#181818", font=("Roboto", 18)).pack()
                    tk.Label(f4, bg="#181818").pack()
                    tk.Label(f4, text="Links:", fg="#FFFFFF", bg="#181818", font=("Roboto", 14)).pack()
                    ghlink = tk.Label(f4, text="Check out the GitHub page!", fg="#FFFFFF", bg="#181818", font=("Roboto", 12), cursor="hand2")
                    ghlink.pack()
                    ghlink.bind("<Button-1>", lambda e: webbrowser.open_new("https://github.com/aaronjc15128/File-Manager"))
            
            tk.Label(f3, bg="#181818").pack()
            tk.Button(f3, text="Submit", command=submitbtnf2).pack()

        tk.Label(f2, text="File Manager", fg="#FFFFFF", bg="#181818", font=("Roboto", 32)).pack()
        tk.Label(f2, text="by Aaron Chauhan", fg="#FFFFFF", bg="#181818", font=("Roboto", 15)).pack()
        for _ in range(3): tk.Label(f2, bg="#181818").pack()
        tk.Label(f2, text="What to do?", fg="#FFFFFF", bg="#181818", font=("Roboto", 15)).pack()
        tk.Label(f2, bg="#181818").pack()
        tk.Label(f2, text="Sort by:", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
        tk.Button(f2, text="File Extension", command=btn1).pack()
        tk.Button(f2, text="File Type", command=btn2).pack()
        tk.Button(f2, text="File Type & Extension", command=btn3).pack()
        tk.Button(f2, text="File Name Prefix", command=btn4).pack()
        tk.Label(f2, bg="#181818").pack()
        tk.Label(f2, text="Rename by:", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
        tk.Button(f2, text="Adding Prefix", command=btn5).pack()
        tk.Button(f2, text="Adding File Size", command=btn6).pack()
        tk.Button(f2, text="Adding File Extension", command=btn7).pack()
        tk.Button(f2, text="Adding File Type", command=btn8).pack()
        tk.Label(f2, bg="#181818").pack()
        tk.Label(f2, text="Delete by:", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
        tk.Button(f2, text="Prefix", command=btn9).pack()
        tk.Button(f2, text="File Extension", command=btn10).pack()
        tk.Button(f2, text="File Type", command=btn11).pack()
        tk.Button(f2, text="ALL FILES", command=btn12).pack()


    RaiseFrame(f1, hide=f2)
    root.mainloop()


if __name__ == "__main__":
    # check for updates
    import requests, os, ctypes

    try:
        response = requests.get("https://api.github.com/repos/aaronjc15128/file-manager/releases/latest")
        name = response.json()["name"]
        latestversion = name[name.index("v"):]

        try:
            version = ((os.path.basename(__file__)[os.path.basename(__file__).index("-"):])[1:])[:-4]

            if version != latestversion:
                ctypes.windll.user32.MessageBoxW(0, f"FileManager-{latestversion} is now available on GitHub.\nCurrent Version: {version}", "New update available!", 0)
        except ValueError:
            pass
    except requests.exceptions.ConnectionError:
        pass
    
    main()