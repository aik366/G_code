def main():
    freza, fr_eza = "Tfreza M6\nG43 H1 Z50\nG54\nS18000 M3\n\n", ""
    with open('f.txt', 'r') as f:
        file = [i.strip().split("\n") for i in [num for num in f.read().split("@ ROUT, 0 : ")[1:]]]
        for fr in file:
            fr_eza += freza.replace("freza", fr[0][1:4], 1)

            start_point = fr[1].replace(",", "").split()
            x0, y0, z0 = start_point[-3], start_point[-2], start_point[-1]
            fr_eza += f"G0 X({x0}) Y({y0}) Z1\n"

            for n, i in enumerate(fr[2:-1]):
                line_ep = i.replace(",", "").split()
                x1, y1, z1, z2 = line_ep[4], line_ep[5], line_ep[6], line_ep[7]
                if n == 0 and z2 != "0":
                    fr_eza += f"G1 X({x1}) Y({y1}) Z-{z2}\n"
                elif n == 0 and z1 != "0":
                    fr_eza += f"G1 X({x0}) Y({y0}) Z-{z1}\n"
                    fr_eza += f"G1 X({x1}) Y({y1})\n"
                else:
                    fr_eza += f"G1 X({x1}) Y({y1})\n"
            fr_eza += "\n"
    print(fr_eza)
    with open('code.txt', 'w', encoding="utf-8") as f:
        f.write(fr_eza)


if __name__ == '__main__':
    main()
