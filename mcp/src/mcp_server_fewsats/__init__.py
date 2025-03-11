from .server import serve


def main():
    """MCP Fewsats Server - Payment functionality for MCP"""
    # import argparse

    # parser = argparse.ArgumentParser(
    #     description="give a model the ability to make payments"
    # )
    # parser.add_argument("--api-key", type=str, help="Fewsats API key")
    # args = parser.parse_args()

    serve()


if __name__ == "__main__":
    main()