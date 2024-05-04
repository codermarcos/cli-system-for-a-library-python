from cli.menus.main import Main
from database import migrate

try:
    migrate()
    Main()

except KeyboardInterrupt:
    print("\n\nAté mais!")
    exit(0)
