from src.input_handler.Parser import Parser

input_data = Parser("an_example.txt")
input_data.parse()

main_params = input_data.main_params
services = input_data.services
features = input_data.features

print("Done")