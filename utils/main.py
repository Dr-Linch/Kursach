import utils

def main():
    data = utils.get_data('..\operations.json')
    filtered_data = utils.get_filtered_data(data)
    sorted_data = utils.get_sorted_data(filtered_data)
    formate_data = utils.get_formate_data(sorted_data)
    print(formate_data)

main()