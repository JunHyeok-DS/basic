import requests

def get_github_user_info(username):
    """
    주어진 GitHub 사용자 이름으로 GitHub API에서 사용자 정보를 가져옵니다.
    """
    url = f"https://api.github.com/users/{username}"
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()  # 성공적으로 데이터를 가져오면 JSON 반환
    else:
        return {"error": f"사용자를 찾을 수 없습니다. (HTTP 상태 코드: {response.status_code})"}

# 테스트 코드
def test_github_user_info():
    # 정상적인 GitHub 사용자 테스트
    valid_username = "torvalds"  # 예제: 리눅스 창시자 계정
    valid_result = get_github_user_info(valid_username)
    assert "login" in valid_result, f"실패: 정상 계정 {valid_username}을 찾지 못함"

    # 존재하지 않는 사용자 테스트
    invalid_username = "this_user_does_not_exist_12345"
    invalid_result = get_github_user_info(invalid_username)
    assert "error" in invalid_result, f"실패: 존재하지 않는 계정 {invalid_username}을 잘못 처리함"

    print("모든 테스트 통과!")

# 함수 실행
if __name__ == "__main__":
    test_github_user_info() 