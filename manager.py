from application import app
import sys
import traceback


def main():
    app.run()


if __name__ == '__main__':
    try:
        sys.exit(main())
    except Exception as e:
        traceback.print_exc()
