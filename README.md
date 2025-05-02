# Man in the Middle Project

## What's This?
This is my "Man in the Middle" project I came up with and coded during the COVID-19 lockdown. I was stuck at home and got curious about network attacks, so I built this Python script to learn how MITM attacks work using ARP spoofing. It’s for educational purposes only, so use it responsibly!

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
- I made this to learn during COVID, not to cause trouble.
- It might not work on networks with strong security (e.g., ARP protection).

## If It Doesn’t Work
- **No Output**: Ensure you’re root (`sudo`) and IPs are correct.
- **Scapy Errors**: Verify Scapy is installed (`pip show scapy`).
- **Network Issues**: Check if the target and gateway are reachable (`ping`).

## Final Word
I built this during lockdown just for fun while getting into network security. It’s a simple little script I came up with myself, and I’m pretty proud of it! Feel free to use it for learning — just keep it legal.
