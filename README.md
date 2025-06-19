# 🎯 Projectile Motion Calculator (CLI Physics Tool)

A command-line based projectile motion calculator written in Python. This tool allows students, hobbyists, and educators to calculate various aspects of projectile motion using **standard physics formulas**, with built-in **unit conversion**, **error handling**, and a **"full analysis" mode** for quick summaries.

---

## 📐 Features

✅ Calculates the following:
- Horizontal Velocity  
- Vertical Velocity  
- Horizontal Distance  
- Maximum Height  
- Range (Total Horizontal Distance)  
- Total Time of Flight  
- Full Analysis (Time, Height, Range in one go)

✅ Supports:
- Input in **non-SI units** (feet, yards, kilometers, minutes, hours)  
- Clean SI unit conversion to **meters** and **seconds**

✅ Built-in:
- Error handling for invalid numerical inputs  
- Option to repeat or exit after every calculation  
- Modular and clean function design

---

## 🧠 Physics Formulas Used

- **Horizontal Distance**: `x = vₓ * t`  
- **Maximum Height**: `h = (vᵧ² * sin²θ) / (2g)`  
- **Range**: `R = (v² * sin(2θ)) / g`  
- **Time of Flight**: `T = (2v * sinθ) / g`

> Where:
> - `v` is initial velocity  
> - `θ` is angle in degrees  
> - `g = 9.8 m/s²` (acceleration due to gravity)

---

## 🛠️ How to Run

### ▶️ Prerequisites:
- Python 3.6 or later

### ▶️ Run the script:
```bash
python projectile.py
