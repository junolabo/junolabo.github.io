# Text shared by every page. Edit here, then run `python3 build.py`.
# L(en, ko, ja) holds one piece of text in each language. Technical terms stay in English.


def L(en, ko, ja):
    return {"en": en, "ko": ko, "ja": ja}


LANGS = [
    ("en", "English", ""),
    ("ko", "한국어", "ko/"),
    ("ja", "日本語", "ja/"),
]

SITE_URL = "https://junolabo.github.io/"
EMAIL = "snowpoet95@gmail.com"
LINKEDIN = "https://www.linkedin.com/in/junho-kim-a3ba8a2aa"
PHOTO = "assets/profile_image_robot.jpeg"

NAME = L("Junho Kim", "김준호", "Junho Kim（キム・ジュノ）")
TITLE = "Physical AI / Robot Intelligence Systems Engineer"

# Status labels. "op" and "op_inhouse" are shown in bold.
STATUS = {
    "op": L("In operation", "운영", "運用中"),
    "op_stores": L("In operation at 40+ stores", "40여 개 매장 운영", "40以上の店舗で運用中"),
    "op_direct": L("In operation at company-run stores", "직영 매장에서 운영", "直営店舗で運用中"),
    "op_inhouse": L("In operation (in-house)", "운영 (사내)", "運用中（社内）"),
    "test": L("Real-robot testing", "실로봇 테스트", "実機テスト"),
    "sim": L("Simulation", "시뮬레이션", "シミュレーション"),
    "sim_eval": L("Simulation (evaluation)", "시뮬레이션 (평가)", "シミュレーション（評価）"),
    "past": L("Previously in operation", "과거 운영", "過去に運用"),
    "ongoing": L("Ongoing", "진행 중", "進行中"),
}
OP_KEYS = {"op", "op_stores", "op_direct", "op_inhouse"}

STATUS_LEGEND = L(
    "In operation: running in stores. In operation (in-house): serving employees inside the company building. Real-robot testing: before live service.",
    "운영: 매장에서 동작. 운영 (사내): 회사 건물 안 직원 대상. 실로봇 테스트: 실서비스 전.",
    "運用中：店舗で稼働。運用中（社内）：社屋内の社員向け。実機テスト：実サービス前。",
)

UI = {
    "all_projects": L("All projects", "전체 프로젝트", "プロジェクト一覧"),
    "project": L("Project", "Project", "Project"),
    "part_of": L("Part {i} of {n}", "{n}개 중 {i}번째 부분", "全{n}パート中 {i}"),
    "role": L("Role", "역할", "役割"),
    "period": L("Period", "기간", "期間"),
    "status": L("Status", "상태", "状態"),
    "scale": L("Scale", "규모", "規模"),
    "prev": L("Previous", "이전", "前へ"),
    "next": L("Next", "다음", "次へ"),
    "read": L("Read", "읽기", "読む"),
    "legend_judge": L("Judgment", "판단", "判断"),
    "legend_fail": L("Failure or return path", "실패 또는 되돌아가는 경로", "失敗または戻る経路"),
    "on_this_page": L("On this page", "이 페이지의 내용", "このページの内容"),
    "request": L("Situation", "상황", "状況"),
}

# The three projects use the same numbers, titles, roles and periods as the resume.
# Project 1 is explained in three parts. Projects 2 and 3 have one page each.
PROJECTS = [
    {
        "no": 1,
        "title": "Store Perception Runtime & Multi-Store Deployment",
        "role": L("Sole developer", "단독 개발", "単独開発"),
        "period": L("2023.10 – present", "2023.10 - 현재", "2023.10 - 現在"),
        "scale": ["op_stores"],
        "summary": L(
            "In a store with no staff, cameras judge the pickup shelf and every cup, a VLM handles irregular situations, and the runtime and its models are updated remotely across 40+ stores.",
            "직원이 없는 매장에서 camera가 픽업 선반과 컵 한 잔 한 잔을 판단하고, VLM이 비정형 상황을 맡고, 40여 개 매장의 runtime과 모델을 원격으로 갱신합니다.",
            "スタッフのいない店舗で、cameraがピックアップ棚とカップ1杯ごとを判断し、VLMが非定型の状況を担当し、40以上の店舗のruntimeとモデルを遠隔で更新します。",
        ),
        "pages": [
            ("perception-runtime", "Perception Runtime", L(
                "Which slot is empty, whether the drink is right, whether the customer took it.",
                "어느 칸이 비었는지, 음료가 제대로 나왔는지, 고객이 가져갔는지.",
                "どの区画が空いているか、ドリンクが正しいか、お客様が受け取ったか。")),
            ("anomaly-detection", "VLM Anomaly Detection", L(
                "12+ irregular situations: the robot recovers, or a person is called.",
                "12종 이상의 이상 상황: 로봇이 복구하거나 사람을 부릅니다.",
                "12種類以上の異常：ロボットが復旧するか、人を呼びます。")),
            ("deployment", "Deployment & Model Update", L(
                "OTA, MLOps pipeline, commissioning of a new store.",
                "OTA, MLOps pipeline, 신규 매장의 commissioning.",
                "OTA、MLOps pipeline、新規店舗のcommissioning。")),
        ],
    },
    {
        "no": 2,
        "title": "Heterogeneous Multi-Robot Agent System",
        "role": "Project Lead",
        "period": L("2025.10 – present", "2025.10 - 현재", "2025.10 - 現在"),
        "scale": None,
        "scale_text": L("4 robot types · 3 agents", "로봇 4종 · agent 3개", "ロボット4種 · agent 3つ"),
        "summary": L(
            "The LLM plans and code validates. Each robot has its own agent, and an Orchestrator ties four robot types together.",
            "LLM이 계획하고 code가 검증합니다. 로봇마다 agent를 두고 Orchestrator가 로봇 4종을 묶습니다.",
            "LLMが計画し、codeが検証します。ロボットごとにagentを置き、Orchestratorが4種のロボットをまとめます。",
        ),
        "pages": [("agent-system", "Heterogeneous Multi-Robot Agent System", None)],
    },
    {
        "no": 3,
        "title": "Teleoperation & Manipulation Learning",
        "role": L("Teleoperation code and policy training", "teleoperation code·policy 학습 담당", "teleoperationのcodeとpolicyの学習を担当"),
        "period": L("2024.11 – present", "2024.11 - 현재", "2024.11 - 現在"),
        "scale": None,
        "summary": L(
            "Motions that fixed sequences cannot do are learned from teleoperation data, from demonstration collection to operation in stores.",
            "정해진 동작으로 할 수 없는 일을 teleoperation 데이터로 학습합니다. 데모 수집부터 매장 운영까지 이었습니다.",
            "決まった動作ではできない作業を、teleoperationのデータから学習します。デモ収集から店舗での運用までをつなぎました。",
        ),
        "pages": [("manipulation-learning", "Teleoperation & Manipulation Learning", None)],
    },
]

# Reading order of the detail pages.
PAGE_ORDER = ["perception-runtime", "anomaly-detection", "deployment", "agent-system", "manipulation-learning"]

# Section headings used on the detail pages.
H = {
    "problem": L("The problem", "문제", "課題"),
    "structure": L("Structure", "구조", "構成"),
    "how": L("How it works", "동작", "仕組み"),
    "decisions": L("Design decisions", "설계 판단", "設計上の判断"),
    "case": L("One case, start to end", "한 건을 끝까지 따라가기", "1件を最後まで追う"),
    "scope": L("Scope", "범위", "範囲"),
    "links": L("Connected projects", "연결된 프로젝트", "関連プロジェクト"),
}

T_DECISION = [L("Decision", "판단", "判断"), L("Reason", "이유", "理由"), L("What it prevents", "막는 문제", "防ぐ問題")]
T_CASE = [L("Event", "사건", "出来事"), L("Observation", "관측", "観測"), L("Judgment", "판단", "判断"), L("Result", "결과", "結果")]
T_SCOPE = [L("Item", "항목", "項目"), L("Content", "내용", "内容")]
SC_STATUS = L("Status", "상태", "状態")
SC_MINE = L("Built by me", "직접 한 것", "自分で行ったこと")
SC_SHARED = L("Shared work", "공동으로 한 것", "共同で行ったこと")
SC_TEAM = L("Done by teammates", "팀원이 한 것", "チームメンバーが行ったこと")
SC_EXISTING = L("Existing technology used", "가져다 쓴 기술", "利用した既存技術")
SC_OUT = L("Outside my scope", "담당 밖", "担当外")
