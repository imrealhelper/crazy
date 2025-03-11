from cflib.crtp import scan_interfaces

print("Scanning for Crazyflies...")
available = scan_interfaces()
print(f"Available Crazyflies: {available}")
