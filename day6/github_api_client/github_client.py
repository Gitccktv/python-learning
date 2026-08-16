from .config import BASE_URL,TIMEOUT
import truststore,ssl,httpx

class GitHubClient:
    def __init__(self):
        ssl_context = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        self.client=httpx.Client(
            verify=ssl_context,
            timeout=TIMEOUT,
        )

    def get_repository(self, owner: str, repo: str) -> dict[str,any]:
        response=self.client.get(f"{BASE_URL}/{owner}/{repo}")
        response.raise_for_status()
        return response.json()