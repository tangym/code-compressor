import os
import tkinter
import tkinter.filedialog
import tkinter.messagebox
import tkinter.ttk
import config

def generate_frame_select_dir(frame):
    def set_text(text_widget, text):
        text_widget.delete(0, tkinter.END)
        text_widget.insert(0, text)

    label_source = tkinter.Label(frame, text='源目录', justify='left')    # why justify doesn't work?
    label_target = tkinter.Label(frame, text='目标目录', justify='left')

    frame_source = tkinter.ttk.Frame(frame)
    frame_target = tkinter.ttk.Frame(frame)
    text_source = tkinter.Entry(frame_source, width=50)
    text_target = tkinter.Entry(frame_target, width=50)
    button_source = tkinter.Button(frame_source, text='选择目录')
        # command=lambda: set_text(text_source, tkinter.filedialog.askdirectory()))
    button_target = tkinter.Button(frame_target, text='选择目录')
        # command=lambda: set_text(text_target, tkinter.filedialog.askdirectory()))

    def handler_save_dir(event):
        if event.widget in (button_source, button_target):
            directory = tkinter.filedialog.askdirectory()
        if event.widget == button_source:
            set_text(text_source, directory)
        elif event.widget == button_target:
            set_text(text_target, directory)

        if event.widget in (button_source, text_source):
            config.SOURCE_DIR = text_source.get().strip()
            if not os.path.exists(config.SOURCE_DIR):
                tkinter.messagebox.showerror('错误', '路径不存在')
        elif event.widget in (button_target, text_target):
            config.TARGET_DIR = text_target.get().strip()

    text_source.bind('<FocusOut>', handler_save_dir)
    text_target.bind('<FocusOut>', handler_save_dir)
    button_source.bind('<Button-1>', handler_save_dir)
    button_target.bind('<Button-1>', handler_save_dir)

    text_source.pack(side='left', fill='x')
    button_source.pack(side='left', fill='x')
    text_target.pack(side='left', fill='x')
    button_target.pack(side='left', fill='x')

    set_text(text_source, config.SOURCE_DIR)
    set_text(text_target, config.TARGET_DIR)

    label_source.pack(fill='x')
    frame_source.pack(fill='x')
    label_target.pack(fill='x')
    frame_target.pack(fill='x')


def generate_frame_select_extension(frame):
    label_extension = tkinter.Label(frame, text='添加后缀名')
    box_language = tkinter.Listbox(frame)
    frame_extension = tkinter.ttk.Frame(frame)
    box_extension = tkinter.Listbox(frame_extension)
    text_extension = tkinter.Entry(frame_extension)

    box_extension.pack(side='top', fill='x')
    text_extension.pack(side='bottom', fill='x')

    for lang in config.EXTENSION:
        box_language.insert(0, lang)

    # TODO: how about delete_extension?
    def handler_add_extension(event):
        ext = text_extension.get().strip()
        if ext:
            ext = ext.split('.')[-1]
            box_extension.insert(0, ext)
            text_extension.delete(0, tkinter.END)

            lang = box_language.get(tkinter.ACTIVE)
            config.EXTENSION[lang] = box_extension.get(0, tkinter.END)

    def handler_show_extension(event):
        # lang = event.widget.get(tkinter.ACTIVE)
        lang = event.widget.get(event.widget.curselection())
        box_extension.delete(0, tkinter.END)
        for ext in config.EXTENSION[lang]:
            box_extension.insert(0, ext)

    box_language.bind('<<ListboxSelect>>', handler_show_extension)
    text_extension.bind('<Return>', handler_add_extension)

    label_extension.pack(side='top')
    box_language.pack(side='left', fill='y')
    frame_extension.pack(side='left', fill='y')


def handler_next_frame(frame_current):
    index_current = frames.index(frame_current)
    print(index_current)
    if index_current + 1 < len(frames):
        frame_current.forget()
        frame_buttons.forget()
        frame_current = frames[index_current + 1]
        frame_current.pack(expand='yes', fill='both')
        frame_buttons.pack(expand='yes', fill='both')
    else:
        # TODO: 把下一步隐藏/改为完成，并退出程序
        pass


def handler_previous_frame(frame_current):
    index_current = frames.index(frame_current)
    print(index_current)
    if index_current - 1 > 0:
        frame_current.forget()
        frame_buttons.forget()
        frame_current = frames[index_current - 1]
        frame_current.pack(expand='yes', fill='both')
        frame_buttons.pack(expand='yes', fill='both')
    else:
        button_previous.forget()


if not __name__ == '__main__':
    root = tkinter.Tk()
    # root.geometry("500x309")
    frames = [tkinter.ttk.Frame(root) for i in range(5)]
    frame_buttons = tkinter.ttk.Frame(root)

    generate_frame_select_dir(frames[0])
    generate_frame_select_extension(frames[1])
    frame_current = frames[0]

    button_previous = tkinter.Button(frame_buttons, text='上一步', command=lambda: handler_previous_frame(frame_current))
    button_next = tkinter.Button(frame_buttons, text='下一步', command=lambda: handler_next_frame(frame_current))
    button_next.pack(side='right')
    button_previous.pack(side='right')

    frames[0].pack(expand='yes', fill='both')
    frames[1].pack(expand='yes', fill='both')
    # tkinter.Button(root, text='开始').pack(expand='yes', fill='both')
    # frame_buttons.pack(expand='yes', fill='both')
    root.mainloop()
