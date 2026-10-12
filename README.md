# Multithreaded TCP Port Scanner

A simple multithreaded TCP port scanner written in Python using only the standard library (`socket` and `threading`). It scans a range of ports on a target host and prints the ones that are open.

Built as a learning project for understanding how TCP connect scanning works and how threads speed up network tasks.

## Features

- TCP connect scan using `socket.connect_ex()`
- Splits the port range across 3 threads for faster scanning
- Short socket timeout (0.02s) for quick results on localhost
- No external dependencies

## How It Works

1. The script creates a TCP socket for each port.
2. It calls `connect_ex((target, port))`. A return value of `0` means the connection succeeded, so the port is **open**.
3. The port range (1-1500) is divided into three chunks, each handled by its own thread.
4. Open ports are printed as they are found, and the sockets are always closed in a `finally` block.

| Thread | Ports scanned |
|--------|---------------|
| `first_half` | 1 - 500 |
| `second_half` | 501 - 1000 |
| `third_half` | 1001 - 1500 |

## Requirements

- Python 3.6+

## Usage

```bash
python port_scanner.py
```

Example output:

```
port135:OPEN
port445:OPEN
program close
```

By default the target is `127.0.0.1` (your own machine). Change it by editing this line:

```python
target = "127.0.0.1"
```

## Known Limitations / Future Improvements

- The three scan functions are nearly identical; they could be merged into one function that takes a start and end port.
- Output order may vary between runs because threads run concurrently.
- Planned: command-line arguments (`argparse`) for target and port range, service name detection, banner grabbing, and saving results to a file.

## Legal Disclaimer

This tool is for **educational purposes only**. Only scan systems you own or have explicit written permission to test. Unauthorized port scanning may be illegal.

## Author

Jeeva - Cyber Security graduate | CompTIA Security+ | Aspiring SOC Analyst

## License

MIT License
