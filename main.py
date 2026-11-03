from machine import Pin, PWM
from servo_translator import translate

# Initialize PWM for each servo motor (shoulder, elbow, wrist) and set frequency to 50Hz
shoulder = PWM(Pin(0))
shoulder.freq(50)

elbow = PWM(Pin(1))
elbow.freq(50)

wrist = PWM(Pin(2))
wrist.freq(50)

## 2. G-CODE PARSING AND INTERPRETATION

def parse_gcode_line(line):
    """
    Parses a single line of G-Code.
    Extracts the command type and parameters.
    """
    
    pass 

def interpret_command(command, params):
    """
    Interprets the parsed command and calls the appropriate action/servo move.
    Supports: G1 (S/E angles), M3 (wrist down), M5 (wrist up), M18 (disable)
    """

    pass

def run_gcode_file(filename):
    """
    Reads the G-Code file line by line and passes lines to the parser.
    """
    print(f"Opening file: {filename}")
    try:
        with open(filename, "r") as f:
            for line in f:
                # Clean the line of extra whitespace/newlines
                clean_line = line.strip()
                
                # Skip empty lines or comments
                if not clean_line or clean_line.startswith(";"):
                    continue
                
                print(f"Reading: {clean_line}")
                

                
    except OSError:
        print(f"Error: Could not find or open {filename}")

# Main execution block
if __name__ == "__main__":
    # Example usage: run_gcode_file("example.gcode")
    pass