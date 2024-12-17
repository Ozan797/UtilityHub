# System Resource Management CLI Tool

A powerful and user-friendly **Command-Line Interface (CLI)** tool written in Python to monitor system resources, manage processes, and track network activity in real-time.

---

## 🚀 **Features**

- **System Monitoring**:
   - Display **CPU**, **Memory**, and **Disk Usage** in real-time.
   - Set refresh intervals for dynamic updates.
   - Log system stats for analysis.

- **Process Management**:
   - List all active processes with their **PID**, **CPU %,** and **Memory %**.
   - Filter processes by name.
   - Terminate processes by PID.

- **Network Monitoring**:
   - Display real-time **network activity**: Data sent and received.

- **Threshold Alerts**:
   - Send desktop notifications when CPU usage exceeds a specified threshold.

- **Polished Terminal UI**:
   - Clean and readable output with colours, progress bars, and section headers.

---

## 🛠️ **Technologies Used**

- **Python 3.x**
- **psutil**: System resource monitoring.
- **argparse**: Command-line interface handling.
- **colorama**: Colour-coded terminal output.
- **tqdm**: Progress bars for dynamic refresh intervals.
- **plyer**: Cross-platform desktop notifications.

---

## 📦 **Installation**

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/Ozan797/UtilityHub.git
   cd UtilityHub
   ```

2. **Create a Virtual Environment** (recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On macOS/Linux
   venv\Scripts\activate     # On Windows
   ```

3. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

---

## 🚀 **Usage**

Run the CLI tool using the following syntax:
```bash
python main.py <command> [options]
```

### **1. System Monitoring**

**Monitor CPU, memory, and disk usage**:
```bash
python main.py monitor --all
```

**Set refresh intervals (e.g., every 3 seconds)**:
```bash
python main.py monitor --all --sleep 3
```

**Monitor individual resources**:
```bash
python main.py monitor --cpu        # Monitor CPU
python main.py monitor --memory     # Monitor memory
python main.py monitor --disk       # Monitor disk
```

**Set a CPU usage threshold for notifications**:
```bash
python main.py monitor --cpu --threshold 80
```

---

### **2. Process Management**

**List all active processes**:
```bash
python main.py process --list
```

**Filter processes by name**:
```bash
python main.py process --list --filter python
```

**Terminate a process by PID**:
```bash
python main.py process --kill <PID>
```

---

### **3. Network Monitoring**

**Track real-time network activity (bytes sent/received)**:
```bash
python main.py network
```

**Refresh network stats every N seconds**:
```bash
python main.py network --sleep 3
```

---

## 📝 **Examples**

**Monitor system stats and log data**:
```bash
python main.py monitor --all --log --sleep 5
```

**List all processes and filter by "chrome"**:
```bash
python main.py process --list --filter chrome
```

**Monitor network activity with 3-second updates**:
```bash
python main.py network --sleep 3
```

---

## ✅ **Future Improvements**

- Add sorting options for processes (e.g., by CPU or memory usage).
- Enhance network monitoring to track individual interfaces.
- Export logs to CSV for analysis.

---

## 📄 **License**

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 **Acknowledgements**

- [psutil](https://github.com/giampaolo/psutil): For system resource monitoring.
- [colorama](https://pypi.org/project/colorama/): For terminal colours.
- [tqdm](https://pypi.org/project/tqdm/): For progress bars.
- [plyer](https://github.com/kivy/plyer): For desktop notifications.

---

