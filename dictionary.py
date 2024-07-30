def print_details(**args):
    for key, value in args.items():
        print(f"{key},{value}")

print_details(name='Success',age=31,address='Prampram',phone=45678903456)