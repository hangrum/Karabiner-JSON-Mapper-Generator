import json
import random
import argparse

def char_to_key_code(char, delay):
    event = {"key_code": char.lower() if char.isupper() else char}

    if char.isupper():
        event["modifiers"] = ["left_shift"]

    special_mappings = {
        '!': ("1", ["left_shift"]),
        '@': ("2", ["left_shift"]),
        '#': ("3", ["left_shift"]),
        '$': ("4", ["left_shift"]),
        '%': ("5", ["left_shift"]),
        '^': ("6", ["left_shift"]),
        '&': ("7", ["left_shift"]),
        '*': ("8", ["left_shift"]),
        '(': ("9", ["left_shift"]),
        ')': ("0", ["left_shift"]),
        '-': ("hyphen", None),
        '_': ("hyphen", ["left_shift"]),
        '=': ("equal_sign", None),
        '+': ("equal_sign", ["left_shift"]),
        '[': ("open_bracket", None),
        '{': ("open_bracket", ["left_shift"]),
        ']': ("close_bracket", None),
        '}': ("close_bracket", ["left_shift"]),
        '\\': ("backslash", None),
        '|': ("backslash", ["left_shift"]),
        ';': ("semicolon", None),
        ':': ("semicolon", ["left_shift"]),
        '\'': ("quote", None),
        '"': ("quote", ["left_shift"]),
        ',': ("comma", None),
        '<': ("comma", ["left_shift"]),
        '.': ("period", None),
        '>': ("period", ["left_shift"]),
        '/': ("slash", None),
        '?': ("slash", ["left_shift"]),
        '`': ("grave_accent", None),
        '~': ("grave_accent", ["left_shift"]),
        ' ': ("spacebar", None)
    }

    if char in special_mappings:
        key_code, modifiers = special_mappings[char]
        event["key_code"] = key_code
        if modifiers:
            event["modifiers"] = modifiers
    if delay > 0:
        event["hold_down_milliseconds"] = random.randint(0, delay)

    return event

def convert_text_to_karabiner(text, trigger_key="f17", delay=0):
    to_sequence = []
    for char in text:
        key_event = char_to_key_code(char, delay)
        if key_event:
            to_sequence.append(key_event)
    manipulators = {
        "description": f"Map {trigger_key}",
        "manipulators": [
            {
                "type": "basic",
                "from": {
                    "key_code": trigger_key,
                    "modifiers": {"optional": ["any"]}
                },
                "to": to_sequence
            }
        ]
    }
    return manipulators

def main():
    parser = argparse.ArgumentParser(description="Convert text to karabiner Complex Modifications JSON Configuration")
    parser.add_argument("text", help="Text to convert karabiner Complex_Modifications")
    parser.add_argument("trigger_key", help="Trigger key (example: f1~f20)")
    parser.add_argument("-d","--delay", help="Delay in milliseconds (default 0)", default=0, type=int)
    args = parser.parse_args()

    delay = args.delay if args.delay is not None else 0
    json_result = convert_text_to_karabiner(args.text,args.trigger_key,delay)
    print(json.dumps(json_result, indent=2))

if __name__ == "__main__":
    main()
