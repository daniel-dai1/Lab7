from machine import Pin, PWM
from servo_translator import translate

# Hardware Setup for Servos

# Connector J1 = Pin 0 (Shoulder Servo)
shoulder = PWM(Pin(0))
shoulder.freq(50)

# Connector J2 = Pin 1 (Elbow Servo)
elbow = PWM(Pin(1))
elbow.freq(50)

# Connector J3 = Pin 2 (Wrist Servo)
wrist = PWM(Pin(2))
wrist.freq(50)



# G-Code Parsing and Execution Functions
def parse_gcode_line(line):
    """
    Parses a single line of G-Code.
    Extracts the command type (e.g., 'G1', 'M3', 'M5', 'M18') 
    and a dictionary of parameters (e.g., {'S': 90.0, 'E': 45.0}).
    """
    tokens = line.split()
    if not tokens:
        return None, {}
    
    command = tokens[0]
    params = {}
    
    # Process parameters following the command
    for token in tokens[1:]:
        prefix = token[0].upper()  # e.g., 'S' or 'E'
        try:
            value = float(token[1:])   # e.g., 90.0
            params[prefix] = value
        except ValueError:
            pass  # Ignore invalid parameter formatting
            
    return command, params


def interpret_command(command, params):
    """
    Interprets the parsed command and moves the servos accordingly.
    """
    if command == "G1":
        # Move shoulder servo if 'S' parameter is given
        if "S" in params:
            angle = params["S"]
            shoulder.duty_u16(translate(angle))
            
        # Move elbow servo if 'E' parameter is given
        if "E" in params:
            angle = params["E"]
            elbow.duty_u16(translate(angle))
            
    elif command == "M3":
        # Lower wrist servo to down position (~30 degrees)
        wrist.duty_u16(translate(30))
        
    elif command == "M5":
        # Raise wrist servo to up position (0 degrees)
        wrist.duty_u16(translate(0))
        
    elif command == "M18":
        # Disable all servos by turning off PWM duty cycle
        shoulder.duty_u16(0)
        elbow.duty_u16(0)
        wrist.duty_u16(0)


def run_gcode_file(filename):
    """
    Opens the G-Code file, reads it line by line, and runs it.
    """
    print(f"Executing G-Code from: {filename}")
    try:
        with open(filename, "r") as f:
            for line in f:
                # Clean line of extra spaces and newline characters
                clean_line = line.strip()
                
                # Skip empty lines or comment lines starting with ';'
                if not clean_line or clean_line.startswith(";"):
                    continue
                
                # Parse and interpret the command
                cmd, params = parse_gcode_line(clean_line)
                if cmd:
                    interpret_command(cmd, params)
                    
        print("Finished executing G-Code file.")
        
    except OSError:
        print(f"Error: Could not find or open file '{filename}' on the Pico.")


# Main Execution
if __name__ == "__main__":
    # Change 'shape.gcode' to match the actual file name you uploaded to your Pico
    run_gcode_file("circle.gcode")