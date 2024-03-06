# WhatsApp Chat Converter

This script converts a WhatsApp chat export text file into both CSV and HTML formats.

## Usage


## Options

- `-h, --help`: Show help message and exit.

## Requirements

- Python 3.x
- tqdm library (install with `pip install tqdm`)

## Documentation

The script parses the input WhatsApp chat export text file and extracts timestamp, name, and text data. It then converts this data into CSV and HTML formats.

### Functions

- `parse_whatsapp_chat(input_file)`: Parses WhatsApp chat export text file and extracts data.
- `convert_to_html(data, output_file)`: Converts chat data to HTML format with appropriate styling.
- `convert_to_csv(input_file, output_file)`: Converts chat data to CSV format.
- `print_help()`: Prints help message.

## How to Use

1. Run the script with appropriate command-line arguments:

2. The script will parse the input text file, convert the data into CSV and HTML formats, and save the output files.

3. If needed, install the tqdm library using `pip install tqdm` to display progress bars during conversion.

## Example

This command will convert the chat.txt file into chat.csv and chat.html.

## Author

[Aditya](https://github.com/Aditya331)

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
