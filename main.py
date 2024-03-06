"""
WhatsApp Chat Converter

This script converts a WhatsApp chat export text file into both CSV and HTML formats.

Usage:
    python script_name.py [input_file.txt] [output_file_csv.csv] [output_file_html.html]

Options:
    -h, --help      : Show this help message and exit

Requirements:
    - Python 3.x
    - tqdm library (install with `pip install tqdm`)

"""

import csv
import os
import sys
from tqdm import tqdm

def parse_whatsapp_chat(input_file):
    """
    Parse WhatsApp chat export text file and extract timestamp, name, and text.
    
    Args:
        input_file (str): Path to the input text file.
    
    Returns:
        list: Parsed chat data as a list of lists, where each sublist contains
              [timestamp, name, text].
    """
    data = []

    with open(input_file, 'r', encoding='utf-8') as f:
        for line in f:
            # Split each line into timestamp, name, and text
            parts = line.strip().split(' - ')
            if len(parts) > 1:
                timestamp, message = parts[0], ' - '.join(parts[1:])
                if ': ' in message:
                    name, text = message.split(': ', 1)
                    data.append([timestamp, name, text])
                else:
                    data.append([timestamp, 'Unknown', message])

    return data

def convert_to_html(data, output_file):
    """
    Convert chat data to HTML format with appropriate styling.
    
    Args:
        data (list): Parsed chat data as a list of lists, where each sublist contains
                     [timestamp, name, text].
        output_file (str): Path to the output HTML file.
    """
    # HTML content template
    html_content = """
    <!DOCTYPE html>
    <html>
    <head>
    <title>WhatsApp Chat</title>
    <style>
    body {
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        background-color: #121212;
        color: #ffffff;
        margin: 0;
        padding: 0;
    }
    .chat-container {
        width: 100%;
        max-width: 600px;
        margin: 20px auto;
    }
    .message {
        padding: 10px 15px;
        margin: 5px 0;
        border-radius: 10px;
        max-width: 70%;
        word-wrap: break-word;
    }
    .message.me {
        background-color: #303030;
        align-self: flex-end;
        margin-left: auto;
    }
    .message.other {
        background-color: #424242;
        align-self: flex-start;
        margin-right: auto;
    }
    .message-body {
        font-size: 14px;
        line-height: 1.5;
    }
    .message-time {
        font-size: 12px;
        color: #999999;
    }
    </style>
    </head>
    <body>
    <div class="chat-container">
    """

    # Generate HTML content
    with tqdm(total=len(data), desc="Converting to HTML", unit="messages") as pbar:
        for row in data:
            timestamp, name, text = row
            if name == 'Aditya':
                html_content += '<div class="message me">'
                html_content += f'<div class="message-body">{text}</div>'
                html_content += '</div>\n'
            elif name == 'Ronak':
                html_content += '<div class="message other">'
                html_content += f'<div class="message-body">{text}</div>'
                html_content += '</div>\n'
            pbar.update(1)  # Increment progress bar

    # Add closing HTML tags
    html_content += """
    </div>
    </body>
    </html>
    """

    # Create necessary directories in the output file path
    os.makedirs(os.path.dirname(output_file), exist_ok=True)

    # Write HTML content to the output file
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html_content)

def convert_to_csv(input_file, output_file):
    """
    Convert chat data to CSV format.
    
    Args:
        input_file (str): Path to the input text file.
        output_file (str): Path to the output CSV file.
    """
    data = parse_whatsapp_chat(input_file)
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['Timestamp', 'Name', 'Text'])
        writer.writerows(data)

def print_help():
    """
    Print help message.
    """
    print("Usage:")
    print("python script_name.py [input_file.txt] [output_file_csv.csv] [output_file_html.html]")
    print("Options:")
    print("-h, --help      : Show this help message and exit")

if __name__ == "__main__":
    if len(sys.argv) == 2 and (sys.argv[1] == "-h" or sys.argv[1] == "--help"):
        print_help()
        sys.exit(0)

    if len(sys.argv) != 4:
        print("Error: Incorrect number of arguments.")
        print_help()
        sys.exit(1)

    input_file = sys.argv[1]
    output_file_csv = sys.argv[2]
    output_file_html = sys.argv[3]

    try:
        convert_to_csv(input_file, output_file_csv)
        data = parse_whatsapp_chat(input_file)
        convert_to_html(data, output_file_html)
        print("Conversion completed successfully.")
    except Exception as e:
        print(f"Error: {e}")
