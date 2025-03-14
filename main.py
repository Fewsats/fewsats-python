from mcp.server.fastmcp import FastMCP
from fewsats.core import Fewsats
import os

# Create FastMCP and Fewsats instances
mcp = FastMCP("Fewsats MCP Server")


def handle_response(response):
    try: return response.status_code, response.json()
    except: return response.status_code, response.text


@mcp.tool()
async def _balance() -> str:
    """Retrieve the balance of the user's wallet."""
    return handle_response(Fewsats().balance())

@mcp.tool()
async def _payment_methods() -> str:
    """Retrieve the user's payment methods."""
    return handle_response(Fewsats().payment_methods())

@mcp.tool()
async def _pay_offer(offer_id: str, l402_offer: dict) -> str:
    """Pays an offer_id from the l402_offers.

    The l402_offer parameter must be a dict with this structure:
    {
        'offers': [
            {
                'offer_id': 'test_offer_2',  # String identifier for the offer
                'amount': 1,                 # Numeric cost value
                'currency': 'usd',           # Currency code
                'description': 'Test offer', # Text description
                'title': 'Test Package'      # Title of the package
            }
        ],
        'payment_context_token': '60a8e027-8b8b-4ccf-b2b9-380ed0930283',  # Payment context token
        'payment_request_url': 'https://api.fewsats.com/v0/l402/payment-request',  # Payment URL
        'version': '0.2.2'  # API version
    }

    Returns payment status response"""
    return handle_response(Fewsats().pay_offer(offer_id, l402_offer))

@mcp.tool()
async def _payment_info(pid: str) -> str:
    """Retrieve the details of a payment."""
    return handle_response(Fewsats().payment_info(pid))

def main():
    mcp.run()

if __name__ == "__main__":
    main()
