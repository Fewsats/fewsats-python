from fastmcp import FastMCP
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
async def _pay_lightning(invoice: str, amount: int, currency: str = "USD", description: str = "") -> str:
    """Pay a lightning invoice.
    
    invoice: Lightning invoice to pay
    amount: Amount in cents
    currency: Currency code (default: USD)
    description: Optional payment description"""
    return handle_response(Fewsats().pay_lightning(invoice, amount, currency, description))

@mcp.tool()
async def _get_payment_details(payment_request_url: str, offer_id: str, payment_method: str, payment_context_token: str) -> str:
    """Get payment details for a payment request.

    payment_request_url: URL for the payment request
    offer_id: ID of the offer
    payment_method: Payment method to use
    payment_context_token: Payment context token"""
    return handle_response(Fewsats().get_payment_details(payment_request_url, offer_id, payment_method, payment_context_token))

if __name__ == "__main__":
    mcp.run()
