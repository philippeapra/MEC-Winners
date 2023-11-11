monopoly_properties = {
    "Go": 0,
    "Mediterraneal_Avenue": 60,
    "Baltic_Avenue": 60,
    "Reading_railroad": 200,
    "Oriental_Avenue": 100,
    "Vermont_Avenue": 100,
    "Connecticut_Avenue": 120,
    #"Jail/Just_Visiting": None,  # Jail doesn't have a monetary value
    "Pennsylvania_Railroad": 200,
    "St.Charle's_Place": 140,
    "Electric_Company": 150,
    "States_Avenue": 140,
    "Virginia_Avenue": 160,
    "St.James_Place": 180,
    "Tennessee_Avenue": 180,
    "New_York_Avenue": 200,
    #"Free_Parking": None,  # Free Parking typically doesn't have a monetary value
    "Kentucky_Avenue": 220,
    "Indiana_Avenue": 220,
    "Illinois_Avenue": 240,
    "BnO_Railroad": 200,
    "Atlantic_Avenue": 260,
    "Ventinor_Avenue": 260,
    "Waterworks": 150,
    "Martin_Gardens": 280,
    #"Go_to_Jail": None,  # "Go to Jail" space typically doesn't have a monetary value
    "Pacific_Avenue": 300,
    "North_Carolina_Avenue": 300,
    "Pennsylvania_Avenue": 320,
    "Short_Line": 200,
    "Park_Place": 350,
    #"Luxury_Tax": None,  # Luxury Tax spaces typically don't have a fixed monetary value
    "Boardwalk": 400
}

def extract_property(property_string):
    # Split the string into values
    values = property_string.split()

    # Extract individual values
    position = int(values[0])
    property_name = values[1].split('_', 1)[-1]  # Remove all characters before and including the first underscore
    houses = int(values[2])
    last_letter = values[-1] if len(values) > 4 else None
    if last_letter != None:
        price = monopoly_properties[property_name]
    else:
        price = 0
    
    return price

def extract_player(player_string):
    # Split the string into values
    values = player_string.split()

    # Handle the "A 1373 9" format
    player = values[0]
    value = int(values[1])
    square_count = int(values[2])
    
    return value

def parse_game(lines):
    # Read each line from the file
    total_price = 0
    for line_number, line in enumerate(lines, start=1):
        if line_number <= 28:
            total_price += extract_property(line)
        else:
            total_price += extract_player(line)

    #print(total_price/4)
    return total_price/4


values = []
# Open the file in read mode
with open("in.txt", "r") as file:
    # Read all lines from the file
    all_lines = file.readlines()

    # Parse every 32 lines with the parse_game function
    for i in range(0, len(all_lines), 32):
        values.append(parse_game(all_lines[i:i+32]))

with open("out.txt", "w") as output_file:
    for value in values:
        output_file.write(str(int(value)) + "\n")