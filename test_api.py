import pytest
import requests

# JokeAPI的基础URL
BASE_URL = "https://v2.jokeapi.dev"

def test_get_random_programming_joke():
    """
    测试用例1: 获取一个随机的编程主题笑话
    - 发送请求获取一个类型为 "Programming" 的笑话。
    - 验证响应的状态码是否为 200 (成功)。
    - 验证返回的笑话中 'category' 字段是否确实是 "Programming"。
    """
    # 构造请求URL，指定笑话类别为 "Programming"
    url = f"{BASE_URL}/joke/Programming"
    
    # 发送GET请求
    response = requests.get(url)
    
    # 1. 验证HTTP响应状态码
    assert response.status_code == 200, "API请求失败，状态码不是200"
    
    # 将返回的JSON字符串解析为Python字典
    joke_data = response.json()
    
    # 2. 验证返回的数据中没有错误
    assert joke_data["error"] == False, "API返回了错误信息"
    
    # 3. 验证笑话的类别是否正确
    # assert joke_data["category"] == "Programming", f"笑话类别不正确，预期是 'Programming'，实际是 '{joke_data['category']}'"
    
    print("\n测试1通过: 成功获取了一个编程笑话。")
    # 打印笑话内容，便于查看
    if joke_data["type"] == "single":
        print(f"笑话: {joke_data['joke']}")
    else:
        print(f"问题: {joke_data['setup']}")
        print(f"答案: {joke_data['delivery']}")

def test_search_joke_with_keyword():
    """
    测试用例2: 搜索包含特定关键词的笑话
    - 发送请求搜索包含 "debugging" 关键词的笑话。
    - 验证响应的状态码是否为 200 (成功)。
    - 验证搜索结果不为空，即 'jokes' 列表的长度大于0。
    """
    # 构造请求URL，指定搜索关键词为 "debugging"
    url = f"{BASE_URL}/joke/Any"
    params = {
        "contains": "debugging",
        "amount": 5  # 请求最多5个结果，确保有足够的数据
    }
    
    # 发送GET请求
    response = requests.get(url, params=params)
    
    # 1. 验证HTTP响应状态码
    assert response.status_code == 200, "API请求失败，状态码不是200"
    
    # 将返回的JSON字符串解析为Python字典
    search_result = response.json()
    
    # 2. 验证返回的数据中没有错误
    assert search_result["error"] == False, "API返回了错误信息"
    
    # 3. 验证搜索到的笑话数量大于0
    assert search_result["amount"] > 0, "没有搜索到包含'debugging'的笑话"
    
    print(f"\n测试2通过: 成功搜索到 {search_result['amount']} 个关于 'debugging' 的笑话。")
    # 打印第一个找到的笑话
    first_joke = search_result["jokes"][0]
    if first_joke["type"] == "single":
        print(f"找到的第一个笑话: {first_joke['joke']}")
    else:
        print(f"找到的第一个问题: {first_joke['setup']}")
        print(f"找到的第一个答案: {first_joke['delivery']}")

if __name__ == "__main__":
    # 这部分代码允许你直接运行这个Python文件来查看测试效果
    # 注意：在正式报告中，你应该使用pytest命令来运行测试
    pytest.main(["-s", __file__]) 