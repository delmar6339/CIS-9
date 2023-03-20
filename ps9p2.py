def compute_batting_average(hits, at_bats):
    batting_average = hits / at_bats
    return batting_average
last_name = input("Enter player's last name: ")
hits = int(input("Enter number of hits: "))
at_bats = int(input("Enter number of at-bats: "))
batting_average = compute_batting_average(hits, at_bats)
print(f"{last_name}'s batting average is: {batting_average:.3f}")