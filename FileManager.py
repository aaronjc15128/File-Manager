def main():
    import tkinter as tk

    import os

    from filetypesdictionary import filetypesDIC


    def RaiseFrame(frame, **kwargs):
        frame.grid(row=0, column=0)
        frame.config(background="#181818")
        frame.tkraise()
        if "hide" in kwargs:
                kwargs["hide"].grid_forget()


    root  = tk.Tk()


    root.title("File Manager")
    root.config(background="#181818")


    # frames
    f1 = tk.Frame(root)
    f2 = tk.Frame(root)
    f3 = tk.Frame(root)

    for frame in {f1, f2, f3}:
        frame.grid(row=0, column=0)
        frame.config(background="#181818")


    # setup
    window_width = 600
    window_height = 800
    
    screen_width = root.winfo_screenwidth()
    screen_height = root.winfo_screenheight()
    center_x = int(screen_width/2 - window_width / 2)
    center_y = int(screen_height/2 - window_height / 2)
    
    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


    # f1
    tk.Label(f1, text="File Manager", fg="#FFFFFF", bg="#181818", font=("Roboto", 32)).pack()
    tk.Label(f1, text="by Aaron Chauhan", fg="#FFFFFF", bg="#181818", font=("Roboto", 15)).pack()
    for _ in range(3): tk.Label(f1, bg="#181818").pack()
    tk.Label(f1, text="Please put all files to sort in a folder", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
    for _ in range(3): tk.Label(f1, bg="#181818").pack()

    tk.Label(f1, text="Enter path of folder:", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()

    svpath = tk.StringVar()
    tk.Entry(f1, textvariable=svpath, width=100).pack()

    tk.Label(f1, bg="#181818").pack()
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
        RaiseFrame(f2, hide=f1)
        window_width = 260
        window_height = 650
        
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        center_x = int(screen_width/2 - window_width / 2)
        center_y = int(screen_height/2 - window_height / 2)
        
        root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

        global path
        path = svpath.get()

        global files
        files = os.listdir(path)
    tk.Button(f1, text="Submit", command=submitbtn).pack()
    for _ in range(5): tk.Label(f1, bg="#181818").pack()
    tk.Label(f1, text="Files to Sort:", fg="#FFFFFF", bg="#181818", font=("Roboto", 15)).pack()
    filesLabel = tk.Label(f1, fg="#FFFFFF", bg="#181818")





    # f2
    def SortMenu():
        def btn1():
            RaiseFrame(f3, hide=f2)
            
            window_width = 700
            window_height = 800

            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            center_x = int(screen_width/2 - window_width / 2)
            center_y = int(screen_height/2 - window_height / 2)

            root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
            

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
            tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()
        def btn2():
            RaiseFrame(f3, hide=f2)
            
            window_width = 750
            window_height = 800

            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            center_x = int(screen_width/2 - window_width / 2)
            center_y = int(screen_height/2 - window_height / 2)

            root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
            

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
                    os.mkdir(os.path.join(path, "miscellaneous"))
                    os.rename(os.path.join(path, file), os.path.join(path, "miscellaneous", file))
                    miscellaneous = True
                else:
                    os.rename(os.path.join(path, file), os.path.join(path, "miscellaneous", file))
            
            tk.Label(f3, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()
        def btn3():
            RaiseFrame(f3, hide=f2)
            
            window_width = 750
            window_height = 800

            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            center_x = int(screen_width/2 - window_width / 2)
            center_y = int(screen_height/2 - window_height / 2)

            root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
            

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
            tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()
        def btn4():
            RaiseFrame(f3, hide=f2)
            
            window_width = 210
            window_height = 120

            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            center_x = int(screen_width/2 - window_width / 2)
            center_y = int(screen_height/2 - window_height / 2)

            root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


            tk.Label(f3, text="Number of characters in prefix:", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            svprefixchar = tk.StringVar()
            tk.Entry(f3, textvariable=svprefixchar, width=30).pack()
            def submitbtnf2():
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
            
                window_width = 750
                window_height = 900

                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                center_x = int(screen_width/2 - window_width / 2)
                center_y = int(screen_height/2 - window_height / 2)

                root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                for _ in range(3): tk.Label(f3, bg="#181818").pack()
                tk.Label(f3, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
                tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()
            tk.Label(f3, bg="#181818").pack()
            tk.Button(f3, text="Submit", command=submitbtnf2).pack()
        def btn5():
            RaiseFrame(f3, hide=f2)
            
            window_width = 180
            window_height = 120

            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            center_x = int(screen_width/2 - window_width / 2)
            center_y = int(screen_height/2 - window_height / 2)

            root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


            tk.Label(f3, text="Prefix:", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            svprefixchar = tk.StringVar()
            tk.Entry(f3, textvariable=svprefixchar, width=30).pack()
            def submitbtnf2():
                prefixchar = str(svprefixchar.get()) + " "

                for file in files:
                    os.rename(os.path.join(path, file), os.path.join(path, prefixchar + file))
            
                window_width = 750
                window_height = 900

                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                center_x = int(screen_width/2 - window_width / 2)
                center_y = int(screen_height/2 - window_height / 2)

                root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                tk.Label(f3, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
                tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()
            tk.Label(f3, bg="#181818").pack()
            tk.Button(f3, text="Submit", command=submitbtnf2).pack()
        def btn6():
            RaiseFrame(f3, hide=f2)
            
            window_width = 700
            window_height = 800

            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            center_x = int(screen_width/2 - window_width / 2)
            center_y = int(screen_height/2 - window_height / 2)

            root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
            

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
            tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()
        def btn7():
            RaiseFrame(f3, hide=f2)
            
            window_width = 700
            window_height = 800

            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            center_x = int(screen_width/2 - window_width / 2)
            center_y = int(screen_height/2 - window_height / 2)

            root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
            

            for file in files:
                os.rename(os.path.join(path, file), os.path.join(path, "." + file.split(".")[len(file.split(".")) - 1] + " " + file))
            
            tk.Label(f3, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()    
        def btn8():
            RaiseFrame(f3, hide=f2)
            
            window_width = 700
            window_height = 800

            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            center_x = int(screen_width/2 - window_width / 2)
            center_y = int(screen_height/2 - window_height / 2)

            root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
            

            for file in files:
                os.rename(os.path.join(path, file), os.path.join(path, filetypesDIC["." + file.split(".")[len(file.split(".")) - 1]] + " " + file))
            
            tk.Label(f3, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()
        def btn9():
            RaiseFrame(f3, hide=f2)
            
            window_width = 180
            window_height = 120

            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            center_x = int(screen_width/2 - window_width / 2)
            center_y = int(screen_height/2 - window_height / 2)

            root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


            tk.Label(f3, text="Prefix:", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            svprefix = tk.StringVar()
            tk.Entry(f3, textvariable=svprefix, width=30).pack()
            def submitbtnf2():
                prefix = str(svprefix.get()) + " "

                for file in files:
                    if file.startswith(prefix) == True:
                        os.remove(os.path.join(path, file))


                window_width = 750
                window_height = 900

                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                center_x = int(screen_width/2 - window_width / 2)
                center_y = int(screen_height/2 - window_height / 2)

                root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                tk.Label(f3, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
                tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()
            tk.Label(f3, bg="#181818").pack()
            tk.Button(f3, text="Submit", command=submitbtnf2).pack()  
        def btn10():
            RaiseFrame(f3, hide=f2)
            
            window_width = 180
            window_height = 120

            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            center_x = int(screen_width/2 - window_width / 2)
            center_y = int(screen_height/2 - window_height / 2)

            root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


            tk.Label(f3, text="File Extension:", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            svextension = tk.StringVar()
            tk.Entry(f3, textvariable=svextension, width=30).pack()
            def submitbtnf2():
                extension = str(svextension.get())

                for file in files:
                    if "." + file.split(".")[len(file.split(".")) - 1] == extension:
                        os.remove(os.path.join(path, file))


                window_width = 750
                window_height = 900

                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                center_x = int(screen_width/2 - window_width / 2)
                center_y = int(screen_height/2 - window_height / 2)

                root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                tk.Label(f3, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
                tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()
            tk.Label(f3, bg="#181818").pack()
            tk.Button(f3, text="Submit", command=submitbtnf2).pack()
        def btn11():
            RaiseFrame(f3, hide=f2)
            
            window_width = 180
            window_height = 120

            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            center_x = int(screen_width/2 - window_width / 2)
            center_y = int(screen_height/2 - window_height / 2)

            root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


            tk.Label(f3, text="File Extension:", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            svtype = tk.StringVar()
            tk.Entry(f3, textvariable=svtype, width=30).pack()
            def submitbtnf2():
                type = str(svtype.get())

                for file in files:
                    if filetypesDIC["." + file.split(".")[len(file.split(".")) - 1]].lower() == type.lower():
                        os.remove(os.path.join(path, file))


                window_width = 750
                window_height = 900

                screen_width = root.winfo_screenwidth()
                screen_height = root.winfo_screenheight()
                center_x = int(screen_width/2 - window_width / 2)
                center_y = int(screen_height/2 - window_height / 2)

                root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                tk.Label(f3, text=f"Sorted Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
                tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()
            tk.Label(f3, bg="#181818").pack()
            tk.Button(f3, text="Submit", command=submitbtnf2).pack()
        def btn12():
            RaiseFrame(f3, hide=f2)
            
            window_width = 180
            window_height = 120

            screen_width = root.winfo_screenwidth()
            screen_height = root.winfo_screenheight()
            center_x = int(screen_width/2 - window_width / 2)
            center_y = int(screen_height/2 - window_height / 2)

            root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')


            tk.Label(f3, text="Type DELETE to confirm:", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
            svconfirm = tk.StringVar()
            tk.Entry(f3, textvariable=svconfirm, width=30).pack()
            def submitbtnf2():
                confirm = str(svconfirm.get())

                if confirm.lower() == "delete":
                    for file in files:
                        os.remove(os.path.join(path, file))


                    window_width = 750
                    window_height = 900

                    screen_width = root.winfo_screenwidth()
                    screen_height = root.winfo_screenheight()
                    center_x = int(screen_width/2 - window_width / 2)
                    center_y = int(screen_height/2 - window_height / 2)

                    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                    tk.Label(f3, text=f"DELETED Files in {path}", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
                    tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()
                else:
                    window_width = 750
                    window_height = 900

                    screen_width = root.winfo_screenwidth()
                    screen_height = root.winfo_screenheight()
                    center_x = int(screen_width/2 - window_width / 2)
                    center_y = int(screen_height/2 - window_height / 2)

                    root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')

                    tk.Label(f3, text=f"DID NOT sort files in {path}\n(Incorrect Confirmation)", fg="#FFFFFF", bg="#181818", font=("Roboto", 12)).pack()
                    tk.Button(f3, text="Exit", command=lambda:root.destroy()).pack()
            
            tk.Label(f3, bg="#181818").pack()
            tk.Button(f3, text="Submit", command=submitbtnf2).pack()

        tk.Label(f2, text="File Manager", fg="#FFFFFF", bg="#181818", font=("Roboto", 32)).pack()
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
    
    SortMenu()


    RaiseFrame(f1, hide=f2)
    root.mainloop()


if __name__ == "__main__":
    main()