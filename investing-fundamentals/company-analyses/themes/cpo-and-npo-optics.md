---
title: Co-packaged Optics (CPO) vs. Near-packaged Optics (NPO)
created: 2026-07-15
updated: 2026-07-15
type: concept
tags: [infrastructure, company, thesis]
sources: []
confidence: high
contested: false
---

# Co-packaged Optics (CPO) vs. Near-packaged Optics (NPO)

In the scaling of generative AI clusters, optical interconnects (Silicon Photonics, high-power lasers, and advanced packaging) represent the primary physical layer for managing bandwidth, latency, and power consumption between switch ASICs and compute nodes.

---

## 1. Architectural Distinctions: CPO vs. NPO

While conceptually similar, Co-packaged Optics (CPO) and Near-packaged Optics (NPO) differ significantly in their physical layout, electrical trace lengths, and overall efficiency:

| Metric / Dimension | Co-packaged Optics (CPO) | Near-packaged Optics (NPO) |
| :--- | :--- | :--- |
| **Physical Placement** | Optical engine is co-packaged directly on the same substrate as the host ASIC (e.g., switch, GPU) | Optical engine is placed on a separate PCB/substrate near the host ASIC |
| **Electrical Trace Length** | Extremely short (< 10-20mm) | Longer (typically 50-100mm) with multiple PCB reflections |
| **Power Efficiency** | Very High (requires minimal SerDes amplification, less bump capacitance) | Moderate-Low (requires strong electrical SerDes, more equalization, and complex drivers) |
| **Channel Density** | Extremely High (tighter routing spacing, high-density grating couplers) | Moderate-Low (requires more fiber/wavelengths to achieve the same data rate) |
| **Thermal / Repairability** | Harder to cool; if the optical engine fails, the entire ASIC package must be replaced | Easier thermal management; modular engines can be replaced independently |

### The Power Sweet Spot
A major design bottleneck is the modulation datarate of a CPO system. Design sweet spots typically sit between **32G and 64G NRZ**:
* **Too Slow:** Laser heater power consumption explodes due to the high volume of lanes.
* **Too Fast (e.g., PAM4):** Laser power and SerDes power requirements escalate non-linearly to meet strict Signal-to-Noise Ratio (SNR) and Relative Intensity Noise (RIN) thresholds.

---

## 2. Silicon Photonics (SiPho) Integration & Foundry Shift

Advanced optical architectures rely on Silicon Photonics (SiPho) foundries for manufacturing grating couplers, waveguides, and ring modulators.

### The TSMC to Tower Semiconductor Transition
Nvidia shifted its optical development program away from TSMC and toward **Tower Semiconductor** due to foundry execution delays:
1. **TSMC Failures:** TSMC botched the development of its high-density 2-D grating couplers and fell behind schedule on Silicon Nitride (SiN) PDK development. This delayed their flagship **COUPE** (Compact Organic Universal Chiplet Engine) CPO platform.
2. **Nvidia's Fallback (Plan-B):** 
   * *Plan-A (TSMC COUPE CPO):* "Slow-and-wide" design using 8-wavelength DWDM (Dense Wavelength Division Multiplexing) running at 50-64G NRZ.
   * *Plan-B (Tower SiPho NPO):* "Faster-and-narrower" design using 16-wavelength DWDM running at 200/400G PAM4.

---

## 3. High-Power CW Lasers: Lumentum vs. Coherent

The transition to higher modulation rates (PAM4) and NPO configurations places a massive burden on the external Continuous Wave (CW) laser source. Higher speeds degrade the extinction ratio of ring modulators, demanding lasers with ultra-narrow linewidths and very low Relative Intensity Noise (RIN).

### UHP Laser Specs & WPE
* **UHP Rating:** Ultra-High-Power (UHP) lasers typically target **350mW to 400mW** of output power. Operating above 450mW degrades Wall-Plug Efficiency (WPE / power conversion efficiency) and severely impacts long-term reliability.
* **Thermal Dependencies:** Laser efficiency degrades non-linearly with temperature. System designers balance performance by operating the thermo-electric cooler (TEC) with a cold-side temperature of **40°C** and a hot-side of **50°C**. (OFC demo metrics at 30°C cold-side setpoints represent idealized, non-production conditions).

### Vendor Landscape
* **Lumentum (LITE) & Broadcom (AVGO):** Dominate the UHP CW laser market. They are currently the only vendors capable of meeting Nvidia's noise and linewidth specifications for the NPO transition, representing a major content-value expansion for Lumentum.
* **Coherent (COHR):** Has struggled to deliver a viable monolithic 400mW CW laser. As a pivot, Coherent is working on a **MOPA (Main-Oscillator Power-Amplifier)** design:
  * *MOPA Mechanism:* Combines a low-power 100mW DFB laser with a semiconductor optical amplifier (SOA) on a single Indium Phosphide (InP) chip.
  * *Trade-off:* While it stabilizes noise, it requires a larger InP footprint and introduces significant **mode-hop (flickering/instability)** risk.
* **Chinese Entrants:** While domestic Chinese suppliers (e.g., JY) claim 300mW DFB lasers, they have failed to publish data proving stable linewidth, cavity length, or WPE curves under high temperatures.

---

## 4. VCSEL CPO & Packaging (AMS OSRAM)

Vertically Cavity Surface Emitting Lasers (VCSELs) represent an alternative channel to Silicon Photonics (SiPho) ring modulators for optical engines.

* **VCSEL vs. Micro-LED:** While micro-LEDs are cheaper, their bandwidth is physically capped at **2-5 GHz** (stretching to 10 GHz), which creates severe electromagnetic interference (EMI), crosstalk, and Forward Error Correction (FEC) overhead across hundreds of lanes. VCSELs easily scale to **50-70 GHz** bandwidth.
* **Packaging as the Core Moat:** VCSEL NPO/CPO performance is not bottlenecked by the VCSEL crystal itself, but by packaging, driver integration, and assembly yield. 
* **AMS OSRAM Thesis:** Following the departure of former Nvidia optics head Ashkan Seyedi to AMS OSRAM, the thesis is that the firm is utilizing its historical LED packaging expertise to scale high-yield VCSEL CPO/NPO systems to challenge Silicon Photonics ring modulators.

---

## Cross-References
* Analysis of Nvidia's custom silicon, networking racks, and memory architectures can be found in [[market-newsletter-digest-2026-07-10]].
* The Indium Phosphide (InP) supply chain bottlenecks and Coherent's Texas wafer line are detailed in [[market-newsletter-digest-2026-06-19]].
* Historical valuation frameworks for hardware and semiconductor sectors are logged in [[valuations]].
