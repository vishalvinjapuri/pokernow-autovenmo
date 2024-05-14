import requests
from venmo_api import Client, PaymentPrivacy

def fetch_data(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.RequestException as e:
        print(f"Error fetching data: {e}")
        return None

def display_pnl(data):
    """Display each player's P&L and username."""
    players_infos = data.get("playersInfos", {})
    print("\nPlayer P&L Summary:")
    for player_id, player_info in players_infos.items():
        player_name = player_info['names'][0]
        net_pnl = player_info['net']/100
        print(f"{player_name}: ${net_pnl}")
    print()

def handle_pnl_data(data, action, client, venmo_handles):
    """Handle PNL data based on the action (request or pay)."""
    players_infos = data.get("playersInfos", {})

    for player_id, player_info in players_infos.items():
        player_name = player_info['names'][0].strip().lower()
        net_pnl = player_info['net']/100
        venmo_handle = venmo_handles.get(player_name)

        if venmo_handle and client.user.get_user_by_username(venmo_handle):
            user = client.user.get_user_by_username(venmo_handle)
            if action == 'request' and net_pnl < 0:
                client.payment.request_money(-net_pnl, "request", user.id)
                print(f"Requested ${-net_pnl} from {player_info['names'][0]} via Venmo.")
            elif action == 'pay' and net_pnl > 0:
                client.payment.send_money(net_pnl, "payment", user.id)
                print(f"Paid ${net_pnl} to {player_info['names'][0]} via Venmo.")
        else:
            if net_pnl != 0:
                print(f"No Venmo handle found for {player_info['names'][0]} with net PNL: ${net_pnl}")

def main():
    # Replace with your Venmo access token
    access_token = "ACCESSTOKENHERE"
    client = Client(access_token=access_token)  # Initialize Venmo client

    # Mapping player names to their Venmo handles, all keys in lower case
    venmo_handles = {
    'jack': 'jack-venmo',
    'john': 'john-venmo',
    #Add handles here as needed
    }

    game_url = input("Please enter your PokerNow link: ")
    url = game_url + "/players_sessions"
    data = fetch_data(url)

    if data:
        display_pnl(data)
        action = input("Do you want to 'request' or 'pay' players? (type 'request' or 'pay'): ").lower().strip()
        if action in ['request', 'pay']:
            handle_pnl_data(data, action, client, venmo_handles)
        else:
            print("Invalid action specified.")
    else:
        print("Failed to fetch game data.")

if __name__ == "__main__":
    main()
