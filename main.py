from menu import DesktopMenu


def main():

    role = "admin"
    menu = DesktopMenu(role)
    menu.execute()


if __name__ == "__main__":
    main()
