def centralizar(w, h, t):
    screen_width = t.winfo_screenwidth()
    screen_height = t.winfo_screenheight()

    x = (screen_width / 2) - (w / 2)
    y = (screen_height / 2) - (h / 2)

    t.geometry(f'{w}x{h}+{int(x)}+{int(y)}')