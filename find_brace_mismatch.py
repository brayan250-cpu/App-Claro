#!/usr/bin/env python3
import sys

def find_brace_mismatch(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    stack = []
    
    for i, line in enumerate(lines, 1):
        for j, char in enumerate(line):
            if char == '{':
                stack.append((i, j, '{', len(stack)))
            elif char == '}':
                if not stack:
                    print(f"ERROR: Unmatched closing brace at line {i}, column {j}")
                    print(f"Line: {line.strip()}")
                    return i
                stack.pop()
    
    if stack:
        print("ERROR: Unmatched opening braces:")
        for line_num, col, char, depth in stack[-10:]:
            print(f"  Line {line_num}, column {col}, depth {depth}")
            print(f"    {lines[line_num-1].strip()}")
    else:
        print("All braces are matched!")
    
    return None

def find_extra_close_in_styles(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        lines = f.readlines()
    
    # Find styles section (line 245 to 750)
    in_styles = False
    styles_start = 0
    depth = 1  # Start at 1 because of @Component({
    
    for i, line in enumerate(lines, 1):
        if 'styles: [`' in line:
            in_styles = True
            styles_start = i
            print(f"Styles section starts at line {i}")
        
        if in_styles:
            # Count braces
            for char in line:
                if char == '{':
                    depth += 1
                elif char == '}':
                    depth -= 1
                    if depth < 1:
                        print(f"\n!!! DEPTH BELOW 1 at line {i}, depth={depth}")
                        print(f"Line {i}: {line.rstrip()}")
                        return i
            
            if i > styles_start and i % 50 == 0:
                print(f"Line {i}: depth={depth}")
            
            if '`]' in line:
                print(f"Styles section ends at line {i}, final depth={depth}")
                if depth != 1:
                    print(f"ERROR: Expected depth 1 at end of styles, got {depth}")
                break

if __name__ == '__main__':
    file_path = r'c:\Users\Brayan Denis\Downloads\Template_Prototipos_ANGULAR_v2.0\Template_Prototipos_ANGULAR_v2.0\claro-viajes-app\src\app\features\rendiciones\pages\listado-rendiciones\listado-rendiciones.component.ts'
    print("=== Method 1: Find first unmatched brace ===")
    find_brace_mismatch(file_path)
    print("\n=== Method 2: Track depth in styles section ===")
    find_extra_close_in_styles(file_path)
