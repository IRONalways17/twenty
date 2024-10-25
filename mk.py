import time
import sys

# Function to print the smile in ASCII art
def display_smile():
    smile = [
        "   *****     *****   ",
        " *       * *       * ",
        "*         *         *",
        "*                   *",
        "*    *       *      *",
        "*    *       *      *",
        "*                   *",
        " *                 * ",
        "  *     *****     *  ",
        "   *             *   ",
        "    *           *    ",
        "      *       *      ",
        "        *****        ",
    ]

    for line in smile:
        sys.stdout.write(f"\033[93m{line}\033[0m\n")
        time.sleep(0.2)

# Run the display_smile function to show the smile
display_smile()
