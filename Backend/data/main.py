import tkinter as tk
from tkinter import ttk, messagebox
from pull_data import fetch_info
from process_data import returns, get_recommend
from graphs import plot_close_price, plot_returns, plot_volatility
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

# ---------------- Root Window ----------------
root = tk.Tk()
root.title("Stock Tracker")
root.geometry("1200x800")  # Set a fixed window size
root.configure(bg="#1e1e2f")  # Dark background

# ---------------- Fonts ----------------
LABEL_FONT = ("Segoe UI", 18, "bold")
DATA_FONT = ("Segoe UI", 16)
BUTTON_FONT = ("Segoe UI", 14, "bold")

# ---------------- Top Frame ----------------
top_frame = tk.Frame(root, bg="#1e1e2f")
top_frame.pack(side="top", fill="x", padx=15, pady=10)

tk.Label(top_frame, text="Stock Symbol:", font=LABEL_FONT, fg="#ffffff", bg="#1e1e2f").pack(side="left", padx=5)
symbol_entry = tk.Entry(top_frame, font=DATA_FONT, width=10, bg="#2b2b44", fg="white", insertbackground="white")
symbol_entry.pack(side="left", padx=5)

tk.Label(top_frame, text="Period:", font=LABEL_FONT, fg="#ffffff", bg="#1e1e2f").pack(side="left", padx=5)
period_dropdown = ttk.Combobox(top_frame, values=["1mo", "3mo", "6mo", "1y", "2y"], font=DATA_FONT, width=8)
period_dropdown.current(0)
period_dropdown.pack(side="left", padx=5)

# ---------------- Tabs for Data ----------------
tab_control = ttk.Notebook(root)
tab_control.pack(expand=1, fill="both", padx=15, pady=15)

style = ttk.Style()
style.theme_use("clam")
style.configure("TNotebook.Tab", background="#2b2b44", foreground="white", font=("Segoe UI", 12, "bold"))
style.configure("TNotebook", background="#1e1e2f")

info_tab = tk.Frame(tab_control, bg="#1e1e2f")
metrics_tab = tk.Frame(tab_control, bg="#1e1e2f")
recommend_tab = tk.Frame(tab_control, bg="#1e1e2f")

tab_control.add(info_tab, text="Stock Info")
tab_control.add(metrics_tab, text="Metrics")
tab_control.add(recommend_tab, text="Recommendation")

info_label = tk.Label(info_tab, text="", font=DATA_FONT, fg="white", bg="#2b2b44", justify="left", anchor="nw", wraplength=1100)
info_label.pack(fill="both", expand=True, padx=10, pady=10)

metrics_label = tk.Label(metrics_tab, text="", font=DATA_FONT, fg="white", bg="#2b2b44", justify="left", anchor="nw", wraplength=1100)
metrics_label.pack(fill="both", expand=True, padx=10, pady=10)

recommend_label = tk.Label(recommend_tab, text="", font=DATA_FONT, fg="white", bg="#2b2b44", justify="left", anchor="nw", wraplength=1100)
recommend_label.pack(fill="both", expand=True, padx=10, pady=10)

# ---------------- Load Data Button ----------------
def load_data():
    symbol = symbol_entry.get().upper()
    period = period_dropdown.get()

    try:
        metrics = returns(symbol, period)
        info = fetch_info(symbol)
        recommendation = get_recommend(symbol)

        # Populate the Info Tab
        info_text = ""
        for k, v in info.items():
            info_text += f"{k}: {v}\n"
        info_label.config(text=info_text)

        # Populate the Metrics Tab
        metrics_text = ""
        for k, v in metrics.items():
            metrics_text += f"{k}: {round(v, 2) if isinstance(v, float) else v}\n"
        metrics_label.config(text=metrics_text)

        # Populate the Recommendation Tab
        recommend_label.config(text=f"Recommendation:\n{recommendation}")

    except Exception as e:
        messagebox.showerror("Error", str(e))


load_button = tk.Button(top_frame, text="Load Data", command=load_data, bg="#1976d2", fg="white",
                        font=BUTTON_FONT, activebackground="#1565c0", activeforeground="white", relief="flat", padx=15,
                        pady=8, borderwidth=0)
load_button.pack(side="left", padx=15)

# ---------------- Tabs for Graphs ----------------
graph_tab_control = ttk.Notebook(root)
graph_tab_control.pack(expand=1, fill="both", padx=15, pady=15)

tab1 = tk.Frame(graph_tab_control, bg="#1e1e2f")
tab2 = tk.Frame(graph_tab_control, bg="#1e1e2f")
tab3 = tk.Frame(graph_tab_control, bg="#1e1e2f")

graph_tab_control.add(tab1, text="Close Price")
graph_tab_control.add(tab2, text="Returns")
graph_tab_control.add(tab3, text="Volatility")

def update_graphs():
    symbol = symbol_entry.get().upper()
    period = period_dropdown.get()

    for widget in tab1.winfo_children(): widget.destroy()
    for widget in tab2.winfo_children(): widget.destroy()
    for widget in tab3.winfo_children(): widget.destroy()

    fig1 = plot_close_price(symbol, period)
    canvas1 = FigureCanvasTkAgg(fig1, master=tab1)
    canvas1.draw()
    canvas1.get_tk_widget().pack(fill="both", expand=True)

    fig2 = plot_returns(symbol, period)
    canvas2 = FigureCanvasTkAgg(fig2, master=tab2)
    canvas2.draw()
    canvas2.get_tk_widget().pack(fill="both", expand=True)

    fig3 = plot_volatility(symbol, period)
    canvas3 = FigureCanvasTkAgg(fig3, master=tab3)
    canvas3.draw()
    canvas3.get_tk_widget().pack(fill="both", expand=True)


graph_button = tk.Button(top_frame, text="Show Graphs", command=update_graphs, bg="#1976d2", fg="white",
                         font=BUTTON_FONT, activebackground="#1565c0", activeforeground="white", relief="flat", padx=15,
                         pady=8, borderwidth=0)
graph_button.pack(side="left", padx=15)

root.mainloop()