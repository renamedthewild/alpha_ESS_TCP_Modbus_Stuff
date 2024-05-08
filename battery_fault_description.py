
# Dictionary mapping each bit position to its fault description
fault_map = {
    0: None,
    1: None,
    2: "Cell Temp Differ",
    3: "Balancer Fault",
    4: "Charge Over Current",
    5: "Balancer Mos Fault",
    6: "Dischage Over Current",
    7: "Pole Over Temp",
    8: "Cell Over Volt",
    9: "Cell Volt Differ",
    10: "Discharge Low Temp",
    11: None,
    12: "Cell Low Volt",
    13: "ISO Comm Fault",
    14: "LMU SN Repeat",
    15: None,
    16: "IR Fault",
    17: "LMU Comm Fault",
    18: "Cell Over Temp",
    19: "BMU Comm Fault",
    20: None,
    21: "Charge Low Temp",
    22: None,
    23: "Volt Detect Fault",
    24: "Wire Harness Fault",
    25: None,
    26: "Relay Fault",
    27: "LMU ID Repeat",
    28: "LMU ID Discontinuous",
    29: "Current Sensor Fault",
    30: None,
    31: "Temp Sensor Fault"
}

# Get fault code from data
fault_code = int(data.get('fault_code', 0))

# Calculate fault descriptions
detected_faults = [fault_map[i] for i in range(32) if (fault_code & (1 << i)) and fault_map[i]]

# Set the state in Home Assistant
state = ', '.join(detected_faults) if detected_faults else "No Faults Detected"
hass.states.set('sensor.battery_fault_description', state)
