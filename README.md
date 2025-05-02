# Man in the Middle Project

## What's This?
This is my "Man in the Middle" project, which I originally wrote from scratch during the COVID-19 lockdown. I was bored at home and got curious about network attacks, so I came up with this Python script to learn how MITM attacks work using ARP spoofing. The original code got deleted, so this is my best shot at recreating it. It’s for learning only, so please use it responsibly!

## What It Does
- Tricks devices into thinking my computer is the gateway (ARP spoofing).
- Captures and forwards network traffic between a target and the gateway.
- Shows requests and responses in real-time (e.g., DNS packets).
- Restores the network when stopped.

## What You Need
- **Software**:
  - Python 3.x
  - Scapy library (`pip install scapy`)
- **Hardware**:
  - Computer on the same network as the target and gateway

## How to Set It Up
1. Install Scapy: `pip install scapy`.
2. Clone or download my project files.
3. Update the script with your target and gateway IPs:
   - `target = "your_target_ip"` (e.g., `10.0.0.17`)
   - `host = "your_gateway_ip"` (e.g., `10.0.0.138`)
4. Run the script as root: `sudo python3 mitm.py`.

## How to Use It
1. Run the script with root privileges.
2. It starts ARP spoofing to intercept traffic.
3. Watch the terminal for captured requests and responses.
4. Press `Ctrl+C` to stop and restore the network.

## Important Notes
- Only test this on networks you own or have permission to use!
- I wrote this myself to learn during COVID, not to cause any harm.
- It might not work on networks with strong security (e.g., ARP protection).

## If It Doesn’t Work
- **No Output**: Ensure you’re root (`sudo`) and IPs are correct.
- **Scapy Errors**: Verify Scapy is installed (`pip show scapy`).
- **Network Issues**: Check if the target and gateway are reachable (`ping`).

## Final Word
I coded this from scratch during lockdown to dive into network security, and I’m proud of rebuilding it after losing the original. It’s a simple script I thought up myself—use it for learning, and keep it legal!
