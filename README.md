# PacketSim: Simplified L2/L3 Telecom Network Emulator (Advanced Update)

**PacketSim** is a lightweight, interactive, and visually stunning network emulator designed specifically for undergraduate telecommunications and networking courses. 

Built using **React**, **Tailwind CSS**, and **Recharts**, this emulator runs entirely in the browser with **zero installation required**—allowing students and instructors to dive straight into network topology creation, routing algorithms, and protocol encapsulation concepts without troubleshooting local Node.js or development environment setups.

---

## 🚀 How to Run the Emulator

### Method 1: Direct Browser Opening (No Server Required)
1. Navigate to the project directory: `C:\Users\rayyi\.gemini\antigravity\scratch\network-emulator\`
2. Double-click the **`index.html`** file, or drag-and-drop it into any modern web browser (Google Chrome, Microsoft Edge, Mozilla Firefox, or Apple Safari).
3. The application will initialize, compile in real-time, and run instantly!

### Method 2: Serve Locally (Recommended for clean asset handling)
If you prefer to serve the application over HTTP (e.g., using a VS Code Live Server extension or terminal command):
- **Using Python**:
  ```bash
  python -m http.server 8000
  ```
  Then open [http://localhost:8000](http://localhost:8000) in your browser.

---

## 🌟 Advanced Updates & Interactive Systems

This advanced version of PacketSim introduces deep telecom simulation math, spatial navigation, and hardware integration abstraction layers:

### 1. Infinite Workspace Canvas (Pan & Zoom)
- **Fluid Zooming**: Center-focused zooming mapped to mouse wheel scrolling. Zoom ranges from `0.4` (broad outline views) to `2.5` (close-up interface work).
- **Background Panning**: Clicking and dragging on the empty workspace grid allows panning across an infinite canvas.
- **Drift-Free Snapping**: All node drag-and-drop snapping coordinates are computed dynamically relative to pan offset and zoom scale, preventing layout drift.

### 2. High-Fidelity Latency Simulation Engine
- Link models support custom **Bandwidth** (1 to 1000 Mbps), propagation **Delay** (ms), and dynamic **Packet Loss Rate** (0 to 100%).
- Packets support configurable payload **Sizes** (64B ICMP pings, 1500B standard MTUs, 65KB TCP windows, or 1MB FTP files).
- Telemetry path latency is calculated using propagation, transmission, and processing delays:
  $$\text{Link Latency} = \text{Propagation Delay} + \text{Transmission Delay} + \text{Processing Delay}$$
  where:
  - $\text{Propagation Delay} = \text{link.delayMs}$
  - $\text{Transmission Delay} = \frac{\text{sizeBytes} \times 8}{\text{bandwidthMbps} \times 10^6} \times 1000 \text{ ms}$
  - $\text{Processing Delay} = 0.5 \text{ ms}$ per node hop.

### 3. Hybrid Device Abstraction Layer (OOP Classes)
Exposes modular ES6 classes that mimic interfacing with real-world infrastructure APIs and shell interfaces:
- **`VirtualDeviceAdapter`**: Internal browser simulation loop.
- **`EmulatedLinuxAdapter`**: Mocks a Docker/LXC container shell.
- **`RealDeviceSSHAdapter`**: Mocks an active SSH tunnel session to a physical router.
- **`MikroTikAdapter`**: Mocks a WinBox/RouterOS terminal session.
- **`OpenWrtAdapter`**: Mocks an OpenWrt UCI network configuration manager.

### 4. Interactive Hybrid CLI Console
- Selected nodes feature a **"Hybrid CLI"** tab alongside their default visual Properties panel.
- Students can select an adapter type and run shell commands in an interactive, responsive terminal terminal.
- Commands supported:
  - `help` - Lists CLI options.
  - `status` - Calls `getStatus()` showing connection and hardware parameters.
  - `config <interface> <ip> <subnet>` - Mocks platform-specific configuration commands. **This dynamically updates the main canvas device properties and labels in real-time!**
  - `ping <targetIp>` - Mocks 4 platform-specific ICMP ping queries.
  - `telemetry` - Queries `getTelemetry()` to print CPU charts and RAM statuses.

---

## 🎓 Core Educational Features & Concepts Covered

- **Layer-2 Switching & MAC Address Learning**: Switches inspect frames, associate source MACs with physical interfaces dynamically, and build a local **MAC Table**.
- **Layer-3 Gateway Routing & Subnet Matching**: Devices check target IPs against CIDR prefix masks to forward locally or route through a resolved **Default Gateway**.
- **Dijkstra Shortest-Path Engine**: Recalculates paths dynamically based on Hop Count, Latency, or Loss Rate.
- **L2 vs. L3 Encapsulation Log Terminal**: Demonstrates how **MAC addresses change hop-by-hop** at each gateway transition, while **IP addresses remain constant** throughout the entire route.
- **Telemetry Analytics Dashboard (Recharts)**: Compiles line and bar charts tracking round-trip latencies, jitter, and link cost comparisons.
