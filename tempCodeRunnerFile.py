
entry_substring.pack(pady=5)

tk.Label(root, text="Enter old text (for Replace):", font=("Arial", 10)).pack(pady=5)
entry_old = tk.Entry(root, width=30)
entry_old.pack(pady=5)

tk.Label(root, text="Enter new text (for Replace):", font=("Arial