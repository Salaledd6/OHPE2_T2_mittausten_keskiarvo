def laske_keskiarvo(numerot):
    return sum(numerot) / len(numerot)


luvut = []

while True:
    syote = int(input("Anna luku: (negatiivinen lopettaa) "))

    if syote <0:
        break

    luvut.append(syote)

keskiarvo = laske_keskiarvo(luvut)
print(f"Lukujen keskiarvo on {keskiarvo:.2f}")