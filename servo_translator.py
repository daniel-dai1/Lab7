def translate(position):
    """Convert a servo angle in degrees to a 16-bit PWM duty value."""
    pulse_width_us = 500 + (position / 180) * 2000
    return round(pulse_width_us * 65535 / 20000)