# Poker Now AutoVenmo

Poker Now AutoVenmo is a simple Python script designed to seamlessly handle financial settlements for Poker Now games using Venmo. It enables game hosts to automatically request payments from players with a negative balance and pay out winnings to those with a positive balance.

## Features

- **Automatic Payment Requests**: Send requests via Venmo to players who owe money from the game.
- **Automatic Payouts**: Send winnings via Venmo to players who have a positive balance at the end of the game.
- **Interactive CLI**: Simple command-line interface to input game details and choose between collecting debts or distributing winnings.

## Requirements

- Python 3.6 or higher
- `requests` library
- `venmo-api` library

## Installation

1. **Clone the Repository**:
   ```
   git clone https://github.com/vishalvinjapuri/pokernow-autovenmo.git
   ```
2. **Navigate to the directory**:
   ```
   cd pokernow-autovenmo
   ```
3. **Install dependencies**:
   ```
   pip install -r requirements.txt
   ```

## Usage

1. **Set up your Venmo API credentials**:
   - Obtain your Venmo developer access token and set it securely.
   - Replace the `access_token` in the script with your actual Venmo access token.
   - Instructions on how to acquire the token can be found here - https://github.com/mmohades/Venmo


2. **Run the script**:
   ```
   python main.py
   ```

3. **Follow the interactive prompts**:
   - Enter the URL of your PokerNow game session.
   - Choose whether to 'request' money from losers or 'pay' winners.

## Configuration

- **Venmo Handles**: Add Venmo handles to the `venmo_handles` dictionary in the script, mapping each player's name to their Venmo username.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue for any bugs, features, or improvements.

## License

Distributed under the MIT License.