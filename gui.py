import tkinter as tk
from tkinter import filedialog
import ContractResourceReplacer as crr


class HadesResourceChangerGUI:
    def __init__(self, master):
        # Window title and dimensions
        master.title("Hades Resource Changer")

        # Directory input label and button
        directory_label = tk.Label(master, text="Hades Directory:")
        directory_label.pack(pady=10)
        self.directory_entry = tk.Entry(master, width=50)
        self.directory_entry.pack(pady=5)
        self.browse_button = tk.Button(master, text="Browse", command=self.browse_directory)
        self.browse_button.pack(pady=5)

        # Overwrite resource values checkbox
        self.overwrite_resource_values_var = tk.BooleanVar(value=False)
        self.overwrite_resource_values_checkbox = tk.Checkbutton(master, text="Overwrite resource values?",
                                                                 variable=self.overwrite_resource_values_var,
                                                                 command=self.update_resource_value_widgets)
        self.overwrite_resource_values_checkbox.pack(pady=5)

        # Resource value label and entry
        self.resource_value_label = tk.Label(master, text="Resource Value:")
        self.resource_value_entry = tk.Entry(master, width=50, state="disabled")
        self.resource_value_label.pack(pady=5)
        self.resource_value_entry.pack(pady=5)

        # Overwrite resource type checkbox
        self.overwrite_resource_type_var = tk.BooleanVar(value=False)
        self.overwrite_resource_type_checkbox = tk.Checkbutton(master, text="Overwrite resource type?",
                                                               variable=self.overwrite_resource_type_var,
                                                               command=self.update_resource_type_widgets)
        self.overwrite_resource_type_checkbox.pack(pady=5)

        # Resource type radio buttons
        self.resource_type_var = tk.StringVar(value="Gems")
        self.resource_type_buttons = []
        resource_types = ["Gems", "SuperGems", "MetaPoints", "GiftPoints", "LockKeys", "SuperLockKeys",
                          "SuperGiftPoints"]
        for resource_type in resource_types:
            button = tk.Radiobutton(master, text=resource_type, variable=self.resource_type_var, value=resource_type,
                                    state="disabled")
            self.resource_type_buttons.append(button)
            button.pack(anchor="w")

        # Apply button
        self.apply_button = tk.Button(master, text="Apply", state="disabled", command=self.apply_changes)
        self.apply_button.pack(pady=10)

    def browse_directory(self):
        directory = filedialog.askdirectory()
        if directory:
            self.directory_entry.delete(0, tk.END)
            self.directory_entry.insert(0, directory)
            self.overwrite_resource_values_checkbox.config(state="normal")
            self.overwrite_resource_type_checkbox.config(state="normal")

    def update_resource_value_widgets(self):
        if self.overwrite_resource_values_var.get():
            self.resource_value_entry.config(state="normal")
        else:
            self.resource_value_entry.config(state="disabled")

    def update_resource_type_widgets(self):
        if self.overwrite_resource_type_var.get():
            for button in self.resource_type_buttons:
                button.config(state="normal")
        else:
            for button in self.resource_type_buttons:
                button.config(state="disabled")

    def apply_changes(self):
        hades_directory = self.directory_entry.get()
        change_resource_value = self.overwrite_resource_values_var.get()
        change_resource_type = self.overwrite_resource_type_var.get()
        resource_input_value = abs(int(self.resource_value_entry.get())) if change_resource_value else 0
        resource_input_type = self.resource_type_var.get()

        # Call
        crr.apply_changes(hades_directory, change_resource_value, change_resource_type, resource_input_value,
                          resource_input_type)


if __name__ == "__main__":
    root = tk.Tk()
    app = HadesResourceChangerGUI(root)
    root.mainloop()
