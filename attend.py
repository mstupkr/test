from datetime import datetime
import json
import os

# 출석 데이터가 저장될 파일 이름
DATA_FILE = "attendance.json"


def load_data():
  """저장된 출석 파일을 불러옵니다."""
  if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r", encoding="utf-8") as f:
      return json.load(f)
  return []


def save_data(data):
  """출석 데이터를 파일에 저장합니다."""
  with open(DATA_FILE, "w", encoding="utf-8") as f:
    json.dump(data, f, ensure_ascii=False, indent=4)


def add_attendance():
  """날짜와 이름을 입력받아 출석을 기록합니다."""
  records = load_data()

  # 오늘 날짜를 기본값으로 설정
  today_str = datetime.now().strftime("%Y-%m-%d")
  date_input = (
      input(f"날짜를 입력하세요 (YYYY-MM-DD, 기본값: 오늘({today_str})): ")
      .strip()
  )
  if not date_input:
    date_input = today_str

  name_input = input("이름을 입력하세요: ").strip()
  if not name_input:
    print("❌ 이름은 비워둘 수 없습니다.\n")
    return

  # 기록 추가 후 저장
  records.append({"date": date_input, "name": name_input})
  save_data(records)
  print(f"✅ [{date_input}] {name_input}님의 출석이 정상적으로 기록되었습니다.\n")


def view_attendance():
  """전체 출석 목록을 출력합니다."""
  records = load_data()
  if not records:
    print("📌 아직 저장된 출석 기록이 없습니다.\n")
    return

  print("\n" + "=" * 30)
  print("       [ 전체 출석 목록 ]")
  print("=" * 30)
  for idx, record in enumerate(records, 1):
    print(f"{idx}. 날짜: {record['date']}  |  이름: {record['name']}")
  print("=" * 30 + "\n")


def main():
  while True:
    print("=== 스터디 출석부 프로그램 ===")
    print("1. 출석 체크하기...")
    print("2. 출석 목록 보기000")
    print("3. 프로그램 종료")
    choice = input("원하는 작업의 번호를 입력하세요 (1-3): ").strip()

    if choice == "1":
      add_attendance()
    elif choice == "2":
      view_attendance()
    elif choice == "3":
      print("프로그램을 종료합니다. 수고하셨습니다!")
      break
    else:
      print("❌ 잘못된 입력입니다. 1에서 3 사이의 숫자를 입력해주세요.\n")


if __name__ == "__main__":
  main()