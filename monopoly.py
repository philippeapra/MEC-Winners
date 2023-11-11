import pandas as pd

def parse_game_data(file_path):
    with open(file_path, 'r') as file:
        lines = file.readlines()

    properties = [line.strip().split() for line in lines if line[0].isdigit()]
    players = [line.strip().split() for line in lines if not line[0].isdigit()]

    game_status = pd.DataFrame(properties, columns=['Box number', 'Box name', 'Number of houses', 'Is mortgaged', 'Owner'])
    player_status = pd.DataFrame(players, columns=['Player name', 'Remaining Budget', 'Number of squares occupied'])

    game_status['Box number'] = pd.to_numeric(game_status['Box number'])
    game_status['Number of houses'] = pd.to_numeric(game_status['Number of houses'])
    game_status['Is mortgaged'] = pd.to_numeric(game_status['Is mortgaged'])
    player_status['Remaining Budget'] = pd.to_numeric(player_status['Remaining Budget'])
    player_status['Number of squares occupied'] = pd.to_numeric(player_status['Number of squares occupied'])
    game_status['Owner'] = game_status['Owner'].fillna('')

    return game_status, player_status

def calculate_player_worth(game_status, player_status, property_values, house_costs, hotel_cost):
    player_worth = {}

    for player in player_status['Player name'].unique():
        player_properties = game_status[game_status['Owner'] == player]

        properties_value = player_properties.apply(
            lambda row: property_values[row['Box number']] +
            (house_costs[row['Box number']] * row['Number of houses'] if row['Number of houses'] < 5 else hotel_cost), axis=1
        ).sum()

        mortgage_deductions = player_properties[player_properties['Is mortgaged'] == 1].apply(
            lambda row: property_values[row['Box number']] * 0.5, axis=1
        ).sum()

        cash = player_status[player_status['Player name'] == player]['Remaining Budget'].iloc[0]
        player_worth[player] = cash + properties_value - mortgage_deductions

    return player_worth

def estimate_starting_money(player_worth, player_status):
    estimated_starting_money = {
        player: worth - player_status[player_status['Player name'] == player]['Number of squares occupied'].iloc[0] * 100
        for player, worth in player_worth.items()
    }
    starting_money = min(estimated_starting_money.values())
    return starting_money

def main(file_path):
    # Define property values and house costs
    property_values = {i: 100 for i in range(1, 41)}  # You need to fill in the actual values
    house_costs = {i: 50 for i in range(1, 41)}  # You need to fill in the actual costs
    hotel_cost = 250  # The cost of building a hotel

    # Parse the game data
    game_status, player_status = parse_game_data(file_path)

    # Calculate player worth
    player_worth = calculate_player_worth(game_status, player_status, property_values, house_costs, hotel_cost)

    # Estimate the starting money
    starting_money = estimate_starting_money(player_worth, player_status)

    print(f"Estimated starting money: ${starting_money}")

# Replace 'file_path.csv' with the actual path to the game status file
main('path/to/game_data.txt')
