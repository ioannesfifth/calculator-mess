from constants import BCOLORS

def header(text: str) -> str:
    return BCOLORS.HEADER + BCOLORS.BOLD + text + BCOLORS.ENDC

def text(text: str) -> str:
    return BCOLORS.TEXT + text + BCOLORS.ENDC

def result_string(header_string: str, number: float) -> str:
    return header(header_string) + ' ' + text(f"{(round(number)):,}")