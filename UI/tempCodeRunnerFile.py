 # Title UI
        title_label = ctk.CTkLabel(
            self.root,
            text = "To-Do List",
            font = ("Helvetica", 22, "bold"),
            text_color = '#f0f4f7'
        )
        title_label.pack(pady=10)

        input_frame = ctk.CTkFrame(self.root)
        input_frame.pack(pady=10)