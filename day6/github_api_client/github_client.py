from .config import BASE_URL, TIMEOUT
import truststore
import ssl
import httpx
from typing import Any

class GitHubClient:
    def __init__(self):
        ssl_context = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        self.client = httpx.Client(
            verify = ssl_context,
            timeout = TIMEOUT,
        )

    def get_repository(self, owner: str, repo: str) -> dict[str,Any]:
        response = self.client.get(f"{BASE_URL}/repos/{owner}/{repo}")
        response.raise_for_status()
        return response.json()

    def close(self):
        self.client.close()