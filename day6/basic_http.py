from github_api_client.github_client import GitHubClient
import httpx

if __name__ == "__main__":
    try:
        client = GitHubClient()
        data = client.get_repository(
            "Gitccktv",
            "python-learning",
        )
        print(f"仓库名称：{data['name']}")
        print(f"仓库star数：{data['stargazers_count']}")
        print(f"仓库fork数：{data['forks_count']}")
        print(f"仓库使用语言：{data['language']}")
        print(f"仓库url：{data['html_url']}")
    except  httpx.TimeoutException as e:
        print(f"请求超时: {e}")
    except  httpx.RequestError as e:
        print(f"发生网络错误: {e}")
    except httpx.HTTPStatusError as e:
        print(f"HTTP状态错误：{e}")