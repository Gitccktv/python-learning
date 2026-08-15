import ssl
import httpx
import truststore

def create_client() -> httpx.Client:
    ssl_context = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)

    return httpx.Client(
        verify=ssl_context,
        timeout=10.0,
    )

def get_repository(owner: str, repo: str) -> dict:
    with create_client() as client:
        response = client.get(
            f"https://api.github.com/repos/{owner}/{repo}"
        )
        response.raise_for_status()
        return response.json()

if __name__ == "__main__":
    try:
        data=get_repository("Gitccktv","python-learning")
        print(f"仓库名称：{data['name']}")
        print(f"仓库star数：{data['stargazers_count']}")
        print(f"仓库fork数：{data['forks_count']}")
        print(f"仓库使用语言：{data['language']}")
        print(f"仓库url：{data['url']}")
    except  httpx.TimeoutException as e:
        print(f"请求超时: {e}")
    except  httpx.RequestError as e:
        print(f"发生网络错误: {e}")
    except httpx.HTTPStatusError as e:
        print(f"HTTP状态错误：{e}")
    except Exception as e:
        print(f"发生意外错误：{e}")