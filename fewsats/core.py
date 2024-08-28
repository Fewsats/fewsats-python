# AUTOGENERATED! DO NOT EDIT! File to edit: ../00_core.ipynb.

# %% auto 0
__all__ = ['Fewsats']

# %% ../00_core.ipynb 2
from fastcore.utils import *
import os
import requests
from typing import Dict, Any, List

# %% ../00_core.ipynb 4
class Fewsats:
    def __init__(self, api_key: str = None, base_url: str = "https://hub-5n97k.ondigitalocean.app/"):
        self.api_key = api_key or os.environ.get("HUB_API_TOKEN")
        if not self.api_key:
            raise ValueError("API key not provided and HUB_API_TOKEN environment variable is not set")
        self.base_url = base_url
        self.session = requests.Session()
        self.session.headers.update({"Authorization": f"Token {self.api_key}"})

@patch
def _request(self: Fewsats, method: str, endpoint: str, **kwargs) -> Dict[str, Any]:
    url = f"{self.base_url}/{endpoint}"
    response = self.session.request(method, url, **kwargs)
    response.raise_for_status()
    return response.json()


# %% ../00_core.ipynb 8
@patch
def get_payment_methods(self: Fewsats) -> List[Dict[str, Any]]:
    """Retrieve the user's payment methods.
    
    Returns:
        List[Dict[str, Any]]: A list of payment methods associated with the user's account.
    """
    return self._request("GET", "v0/stripe/payment-methods")


# %% ../00_core.ipynb 11
@patch
def preview_purchase(self: Fewsats, l402_url: str) -> Dict[str, Any]:
    """Preview a purchase for the given L402 URL.
    
    This method will use the default payment method if a charge is needed.
    
    Args:
        l402_url (str): The L402 URL for the purchase.
    
    Returns:
        Dict[str, Any]: The preview details of the purchase.
    """
    return self._request("POST", "v0/l402/preview/purchase", json={"l402_url": l402_url})


# %% ../00_core.ipynb 14
@patch
def purchase(self: Fewsats, l402_url: str) -> Dict[str, Any]:
    """Make a purchase for the given L402 URL.
    
    This method will use the default payment method if a charge is needed.
    
    Args:
        l402_url (str): The L402 URL for the purchase.
    
    Returns:
        Dict[str, Any]: The details of the completed purchase.
    """
    return self._request("POST", "v0/l402/purchases", json={"l402_url": l402_url})

