from menu import fomenu
from helyszin import spawnpoint

def main():
    helyszin = spawnpoint()
    print(f'Kezdőpontod:{helyszin}')
    fomenu()
main()