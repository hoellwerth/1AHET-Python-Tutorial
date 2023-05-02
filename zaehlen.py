untergrenze = int(input("Gib untergrenze ein: "))
obergrenze = int(input("Gib obergrenze ein: "))

def zaehlen_while(untergrenze, obergrenze):
  count = untergrenze

  while count <= obergrenze:
    print(count)
    count += 1

def zaehlen_for(untergrenze, obergrenze):
  for count in range(untergrenze, obergrenze):
    print(count)

zaehlen_while(untergrenze, obergrenze)
zaehlen_for(untergrenze, obergrenze)
