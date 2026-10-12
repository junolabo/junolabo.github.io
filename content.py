# Site text in three languages. Edit here, then run `python3 build.py`.
# L(en, ko, ja) holds one sentence in each language. Technical terms stay in English.


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

# Status labels. The key decides the style ("op" is shown in bold).
STATUS = {
    "op": L("In operation", "운영", "運用中"),
    "op_inhouse": L("In operation (in-house)", "운영 (사내)", "運用中（社内）"),
    "test": L("Real-robot testing", "실로봇 테스트", "実機テスト"),
    "sim": L("Simulation", "시뮬레이션", "シミュレーション"),
    "sim_eval": L("Simulation (evaluation)", "시뮬레이션 (평가)", "シミュレーション（評価）"),
    "past": L("Previously in operation", "과거 운영", "過去に運用"),
    "ongoing": L("Ongoing", "진행 중", "進行中"),
}

NAME = L("Junho Kim", "김준호", "Junho Kim（キム・ジュノ）")
TITLE = "Physical AI / Robot Intelligence Systems Engineer"
LOCATION = L("Seoul, Korea", "Seoul, Korea", "Seoul, Korea")

META_DESCRIPTION = L(
    "Junho Kim — Robot Intelligence engineer. Robot perception, LLM-based task planning, and learning-based manipulation built as one connected system.",
    "김준호 — Robot Intelligence 엔지니어. 로봇의 perception, LLM 기반 task planning, 학습 기반 manipulation을 하나로 이어지는 시스템으로 설계하고 구현합니다.",
    "Junho Kim — Robot Intelligenceエンジニア。ロボットのperception、LLMによるtask planning、学習ベースのmanipulationを、ひとつにつながるシステムとして設計・実装しています。",
)

NAV = [
    ("system", "System"),
    ("work", "Work"),
    ("scenarios", "Scenarios"),
    ("experience", "Experience"),
    ("skills", "Skills"),
    ("contact", "Contact"),
]

SUMMARY = [
    L(
        "Robot Intelligence engineer. I design and build robot perception, LLM-based task planning, and learning-based manipulation as one connected system.",
        "로봇의 perception, LLM 기반 task planning, 학습 기반 manipulation을 하나로 이어지는 시스템으로 직접 설계하고 구현해 온 Robot Intelligence 엔지니어입니다.",
        "ロボットのperception、LLMによるtask planning、学習ベースのmanipulationを、ひとつにつながるシステムとして自ら設計・実装してきたRobot Intelligenceエンジニアです。",
    ),
    L(
        "I built the perception runtime that runs in 40+ stores and the deployment and model-update system behind it (OTA, MLOps). On top of that I added an LLM agent system that ties several kinds of robots together, and manipulation policies learned from teleoperation.",
        "매장 40여 곳에서 동작하는 perception runtime과 그 배포·모델 갱신 체계(OTA, MLOps)를 만들었고, 그 위에 여러 종류의 로봇을 묶는 LLM agent 시스템과 teleoperation 기반 manipulation policy를 더했습니다.",
        "40以上の店舗で動くperception runtimeと、そのデプロイ・モデル更新の仕組み（OTA、MLOps）を作りました。その上に、複数種類のロボットをまとめるLLM agentシステムと、teleoperationに基づくmanipulation policyを加えました。",
    ),
    L(
        "Perception and the single-arm manipulation policy are in operation in stores. The agent system is in operation in-house.",
        "perception과 single-arm manipulation policy는 매장에서, agent 시스템은 사내에서 운영하고 있습니다.",
        "perceptionとsingle-arm manipulation policyは店舗で、agentシステムは社内で運用しています。",
    ),
]

LANGUAGES_LABEL = L("Languages", "Languages", "Languages")
LANGUAGES = L(
    "Korean (native), English (conversational), Japanese (conversational)",
    "한국어 (모국어), 영어 (일상 대화), 일본어 (일상 대화)",
    "韓国語（母語）、英語（日常会話）、日本語（日常会話）",
)

# ---------------------------------------------------------------- System

SYSTEM_INTRO = L(
    "The three projects below are layers of one system. In operation: running in stores. In operation (in-house): serving employees inside the company building. Real-robot testing: before live service.",
    "아래 세 프로젝트는 한 시스템의 계층입니다. 운영: 매장에서 동작. 운영 (사내): 회사 건물 안 직원 대상. 실로봇 테스트: 실서비스 전.",
    "以下の3つのプロジェクトは、ひとつのシステムの階層です。運用中：店舗で稼働。運用中（社内）：社屋内の社員向け。実機テスト：実サービス前。",
)

SYSTEM_MAP_HEAD = ("Layer", "Role", "Status")
SYSTEM_MAP = [
    ("Orchestrator Agent",
     L("Distributes work across robots", "로봇 간 작업 배분", "ロボット間の作業配分"),
     ["op_inhouse", "test"]),
    ("Task Planning Agent",
     L("Per-robot LLM task planning, validation, replanning",
       "로봇별 LLM task planning, validation, replanning",
       "ロボットごとのLLM task planning、validation、replanning"),
     ["op_inhouse", "test"]),
    ("Execution",
     L("skill, manipulation policy", "skill, manipulation policy", "skill、manipulation policy"),
     ["op", "test"]),
    ("Perception",
     L("depth · detection · tracking, VLM anomaly detection",
       "depth · detection · tracking, VLM anomaly detection",
       "depth · detection · tracking、VLM anomaly detection"),
     ["op"]),
    ("Cross-cutting: Data · Evaluation · Deployment",
     L("MLOps, evaluation, OTA", "MLOps, 평가, OTA", "MLOps、評価、OTA"),
     ["op", "sim_eval"]),
]

STRUCTURE = {
    "caption": L("System structure", "시스템 구조", "システム構成"),
    "top": ("Orchestrator Agent",
            L("Splits a natural-language request into tasks and distributes them",
              "자연어 요청을 작업으로 나눠 배분",
              "自然言語の依頼を作業に分けて配分")),
    "link": "MCP tool",
    "children": [
        ("Task Planning Agent", L("beverage-making robot", "음료 제조 로봇", "ドリンク製造ロボット")),
        ("Task Planning Agent", L("semi-humanoid robot", "세미 휴머노이드 로봇", "セミヒューマノイドロボット")),
        (L("Delivery robot · Cleaning robot", "배송 로봇 · 청소 로봇", "配送ロボット · 清掃ロボット"),
         L("robot API wrapped as an MCP tool", "MCP tool로 감싼 로봇 API", "MCP toolで包んだロボットAPI")),
        ("Perception", L("depth, detection, tracking, VLM", "depth, detection, tracking, VLM", "depth、detection、tracking、VLM")),
    ],
    "inside_label": L("Inside every agent", "모든 agent의 내부", "すべてのagentの内部"),
    "inside": ["Context Manager", "Task Planner (LLM)", "Plan Validator", "Executor"],
    "note": L(
        "The LLM is used only in the planner. The VLM is used only for recognition.",
        "LLM은 planner에서만 씁니다. VLM은 인식에만 씁니다.",
        "LLMはplannerでのみ使います。VLMは認識にのみ使います。",
    ),
}

# ---------------------------------------------------------------- Work

WORK_INTRO = L(
    "XYZ Inc · Robot Intelligence Team · 2023.10 – present",
    "XYZ Inc · Robot Intelligence Team · 2023.10 - 현재",
    "XYZ Inc · Robot Intelligence Team · 2023.10 - 現在",
)

PROJECTS = [
    {
        "id": "perception",
        "title": "Store Perception Runtime & Multi-Store Deployment",
        "role": L("Sole developer", "단독 개발", "単独開発"),
        "period": L("2023.10 – present", "2023.10 - 현재", "2023.10 - 現在"),
        "scale": L("In operation at 40+ stores", "40여 개 매장 운영", "40以上の店舗で運用中"),
        "scale_op": True,
        "video": None,  # set to a file path under assets/ to show the demo video
        "context": L(
            "In a store with no staff, cameras have to decide which slot of the pickup shelf is empty, whether a drink came out correctly, and whether the customer took it. Clearing abandoned drinks and checking anomalies, which a manager used to travel to the store for, were also handed to the robot. As the number of stores grew, deployment and model updates moved to remote operation.",
            "직원이 없는 매장에서는 픽업 선반의 어느 칸(slot)이 비었는지, 음료가 제대로 나왔는지, 고객이 가져갔는지를 camera로 판단해야 했습니다. 관리자가 매장에 나가 하던 방치 음료 정리와 이상 확인도 로봇에 넘겼고, 매장이 늘면서 배포와 모델 갱신을 원격으로 옮겼습니다.",
            "スタッフのいない店舗では、ピックアップ棚のどの区画（slot）が空いているか、ドリンクが正しく出たか、お客様が受け取ったかをcameraで判断する必要がありました。管理者が店舗に出向いて行っていた放置ドリンクの片付けと異常確認もロボットに任せました。店舗が増えるにつれ、デプロイとモデル更新を遠隔に移しました。",
        ),
        "groups": [
            ("Perception", [
                ("Occupancy detection", None, L(
                    "Decides from depth whether each slot of the pickup shelf holds a cup. Depth from a trained stereo model and RealSense's own depth are transformed into shelf-plane coordinates to measure the height of objects on each slot. When depth drops out or goes stale, the slot is not treated as empty and no new drink is placed there.",
                    "픽업 선반의 각 칸에 컵이 있는지를 depth로 판단. 학습한 stereo 모델의 depth와 RealSense 자체 depth를 선반 면 기준 좌표로 옮겨 칸 위 물체의 높이를 측정. depth가 끊기거나 오래되면 비었다고 보지 않고 그 칸에 새 음료를 놓지 않음.",
                    "ピックアップ棚の各区画にカップがあるかをdepthで判断します。学習したstereoモデルのdepthとRealSense自体のdepthを棚面基準の座標に変換し、区画上の物体の高さを測ります。depthが途切れたり古くなったりした場合は空きとは見なさず、その区画に新しいドリンクを置きません。",
                )),
                ("Cup lifecycle tracking", None, L(
                    "Tracks each cup from making to customer pickup. The gripper camera checks that the cup is held correctly and checks the drink level. When a cup disappears from the shelf, it is matched against the robot's motion at that moment to tell customer pickup from robot removal. State is restored from SQLite after a restart. Detection and tracking are implemented in C++ and TensorRT.",
                    "컵 한 잔을 제조부터 고객 수령까지 추적. gripper camera로 컵을 제대로 잡았는지와 음료량을 확인. 선반에서 컵이 사라지면 그때의 로봇 동작과 대조해 고객 수령과 로봇 회수를 구분. 재시작 뒤에도 SQLite로 상태를 복구. detection과 tracking은 C++와 TensorRT로 구현.",
                    "カップ1杯を製造からお客様の受け取りまで追跡します。gripper cameraでカップを正しく把持できたかとドリンク量を確認します。棚からカップが消えたときは、その時点のロボットの動作と照合して、お客様の受け取りとロボットによる回収を区別します。再起動後もSQLiteから状態を復元します。detectionとtrackingはC++とTensorRTで実装しました。",
                )),
                ("Disposal flow", None, L(
                    "The robot picks up and disposes of drinks that customers did not take. Depth is used to check that the cup can be approached without touching neighboring cups. A cup found by the ceiling camera is identified again by the gripper camera before it is grasped. Because the same arm also makes drinks, control ownership is managed so that the two jobs do not overlap.",
                    "고객이 가져가지 않은 음료를 로봇이 집어 폐기. 주변 컵에 닿지 않고 접근할 수 있는지 depth로 확인하고, 천장 camera로 찾은 컵을 gripper camera로 다시 식별한 뒤 집음. 제조와 같은 로봇팔을 쓰므로 두 작업이 겹치지 않게 제어권을 관리.",
                    "お客様が受け取らなかったドリンクをロボットが把持して廃棄します。周囲のカップに触れずに接近できるかをdepthで確認し、天井cameraで見つけたカップをgripper cameraで再度識別してから把持します。製造と同じロボットアームを使うため、2つの作業が重ならないように制御権を管理します。",
                )),
                ("Stereo depth", None, L(
                    "A large stereo model (FoundationStereo) serves as the teacher. Its output is corrected against the measured shelf plane to make pseudo-labels, and a real-time model (RT-IGEV) is further trained on store images. Inference runs on Jetson Orin with TensorRT FP16.",
                    "큰 stereo 모델(FoundationStereo)을 teacher로 삼고 그 출력을 실측한 선반 평면에 맞춰 보정해 pseudo-label을 만든 뒤, 실시간 모델(RT-IGEV)을 매장 image로 추가 학습. Jetson Orin에서 TensorRT FP16으로 추론.",
                    "大きなstereoモデル（FoundationStereo）をteacherとし、その出力を実測した棚の平面に合わせて補正してpseudo-labelを作り、リアルタイムモデル（RT-IGEV）を店舗のimageで追加学習しました。Jetson Orin上でTensorRT FP16で推論します。",
                )),
                ("VLM anomaly detection", None, L(
                    "Camera images and robot and equipment state are bundled every 2 seconds and given to a VLM. The VLM, fine-tuned with QLoRA, classifies 12+ situations such as a fallen cup, contamination, and equipment failure. A predefined recovery action runs according to the result, and an alert is sent when a person is needed. In operation at company-run stores.",
                    "camera image와 로봇·장비 상태를 2초마다 묶어 VLM에 입력. QLoRA로 fine-tuning한 VLM이 컵 쓰러짐, 오염, 고장 등 12종 이상의 상황을 분류. 결과에 따라 정해 둔 복구 동작을 실행하고, 사람이 필요하면 알림. 직영 매장에서 운영.",
                    "camera imageとロボット・機器の状態を2秒ごとにまとめてVLMに入力します。QLoRAでfine-tuningしたVLMが、カップの転倒、汚れ、故障など12種類以上の状況を分類します。結果に応じてあらかじめ決めた復旧動作を実行し、人が必要な場合は通知します。直営店舗で運用しています。",
                )),
            ]),
            ("Deployment", [
                ("OTA", None, L(
                    "The whole runtime is deployed from a central server to store devices with Tailscale and Ansible. A new version first runs as a dry-run, and its errors, its communication with other devices, and its decisions are compared with the previous version before the swap. Store logs are collected in real time, and anomalies raise alerts.",
                    "중앙 서버에서 Tailscale과 Ansible로 전체 runtime을 매장 장치에 배포. 새 버전을 먼저 dry-run으로 돌려 오류, 다른 장치와의 통신, 판단 결과를 이전 버전과 비교한 뒤 교체. 매장 로그를 실시간 수집해 이상 시 알림.",
                    "中央サーバーからTailscaleとAnsibleでruntime全体を店舗の機器にデプロイします。新しいバージョンをまずdry-runで動かし、エラー、他の機器との通信、判断結果を以前のバージョンと比較してから切り替えます。店舗のログをリアルタイムで収集し、異常時に通知します。",
                )),
                ("MLOps pipeline", None, L(
                    "From store data, segments where the model's decision changed or its confidence was low are selected automatically, labeled automatically, and then reviewed by a person. A new model is evaluated separately on the target store and on all stores, and it is deployed only when both pass the threshold. Applied to three models: stereo, detection, and VLM.",
                    "매장 데이터에서 모델의 판단이 바뀌거나 신뢰도가 낮은 구간을 자동으로 골라 자동 라벨링한 뒤 사람이 검토. 새 모델은 해당 매장 성능과 전체 매장 성능을 따로 평가해 둘 다 기준을 넘어야 배포. stereo, detection, VLM 3종에 적용.",
                    "店舗データから、モデルの判断が変わった区間や信頼度が低い区間を自動で選び、自動ラベリングした後に人が確認します。新しいモデルは、対象店舗での性能と全店舗での性能を別々に評価し、両方が基準を超えた場合のみデプロイします。stereo、detection、VLMの3種類に適用しています。",
                )),
                ("Commissioning", None, L(
                    "Differences between stores, such as shelf size, robot configuration, and camera type, are handled by configuration and not by code branches. A new store is installed in the order pre-check → camera calibration → result verification → start of operation. Calibration results are versioned and can be rolled back.",
                    "매장마다 다른 선반 크기, 로봇 구성, camera 종류를 code 분기 없이 설정으로 처리. 신규 매장은 사전 점검 → camera calibration → 결과 검증 → 운영 시작의 순서로 설치하고, calibration 결과를 버전으로 관리해 이전 버전으로 되돌릴 수 있음.",
                    "店舗ごとに異なる棚のサイズ、ロボット構成、cameraの種類を、codeの分岐ではなく設定で扱います。新規店舗は、事前点検 → camera calibration → 結果検証 → 運用開始の順で設置します。calibrationの結果をバージョン管理し、以前のバージョンに戻せます。",
                )),
            ]),
        ],
        "diagram": {
            "caption": L("MLOps pipeline: from store data to deployment",
                         "MLOps pipeline: 매장 데이터에서 배포까지",
                         "MLOps pipeline：店舗データからデプロイまで"),
            "steps": [
                (L("Store data", "매장 데이터", "店舗データ"),
                 L("collected on the central server", "중앙 서버로 수집", "中央サーバーに収集")),
                (L("Automatic selection", "자동 선별", "自動選別"),
                 L("decision changed, or confidence low", "판단이 바뀌거나 신뢰도가 낮은 구간", "判断が変わった区間、信頼度が低い区間")),
                (L("Automatic labeling", "자동 라벨링", "自動ラベリング"), None),
                (L("Human review", "사람 검토", "人による確認"), None),
                (L("Training", "학습", "学習"),
                 L("stereo, detection, VLM", "stereo, detection, VLM", "stereo、detection、VLM")),
                (L("Evaluation", "평가", "評価"),
                 L("target store and all stores, both must pass", "해당 매장과 전체 매장, 둘 다 기준 통과", "対象店舗と全店舗、両方が基準を通過")),
                (L("TensorRT conversion", "TensorRT 변환", "TensorRT変換"), None),
                (L("OTA deployment", "OTA 배포", "OTAデプロイ"),
                 L("dry-run, then swap", "dry-run 뒤 교체", "dry-runの後に切り替え")),
            ],
        },
    },
    {
        "id": "agent",
        "title": "Heterogeneous Multi-Robot Agent System",
        "role": "Project Lead",
        "period": L("2025.10 – present", "2025.10 - 현재", "2025.10 - 現在"),
        "scale": L("4 robot types · 3 agents", "로봇 4종 · agent 3개", "ロボット4種 · agent 3つ"),
        "scale_op": False,
        "video": None,
        "context": L(
            "A fixed making sequence could not handle off-menu requests or problems that came up during execution, so a person stepped in each time. To respond as flexibly as a staffed store, and to take on delivery and cleaning inside the company building, each robot got an agent in which an LLM plans and code validates, and an Orchestrator ties the agents together.",
            "고정된 제조 순서로는 메뉴에 없는 요청이나 실행 중에 생긴 문제를 처리할 수 없어 그때마다 사람이 개입했습니다. 유인 매장처럼 유연하게 응대하고 회사 건물 안 배송과 청소까지 맡기려고, LLM이 계획하고 code가 검증하는 agent를 로봇마다 두고 Orchestrator로 묶었습니다.",
            "固定された製造手順では、メニューにない要望や実行中に起きた問題を処理できず、そのたびに人が介入していました。有人店舗のように柔軟に対応し、社屋内の配送と清掃まで任せるために、LLMが計画しcodeが検証するagentをロボットごとに置き、Orchestratorでまとめました。",
        ),
        "groups": [
            ("Agents", [
                ("Orchestrator Agent", ["op_inhouse", "test"], L(
                    "Splits a natural-language request into tasks and distributes them to agents and robots connected as MCP tools. For “two Americanos to the meeting room”, making and loading go to the beverage-making agent, and the delivery robot is instructed in order: move, ride the elevator, hand over. When the VLM detects contamination, the cleaning robot is dispatched. Distribution to the semi-humanoid agent is in real-robot testing.",
                    "자연어 요청을 작업으로 나눠, MCP tool로 연결한 agent와 로봇에 배분. \"아메리카노 2잔을 회의실로\" 요청이면 제조와 적재는 음료 제조 agent에 맡기고, 배송 로봇에는 이동, 엘리베이터 탑승, 전달을 순서대로 지시. VLM이 오염을 감지하면 청소 로봇을 보냄. 세미 휴머노이드 agent로의 배분은 실로봇 테스트.",
                    "自然言語の依頼を作業に分け、MCP toolとして接続したagentとロボットに配分します。「アメリカーノ2杯を会議室へ」という依頼であれば、製造と積み込みはドリンク製造agentに任せ、配送ロボットには移動、エレベーター乗車、受け渡しを順に指示します。VLMが汚れを検知すると清掃ロボットを向かわせます。セミヒューマノイドagentへの配分は実機テスト段階です。",
                )),
                (L("Task Planning Agent (beverage-making robot)", "Task Planning Agent (음료 제조 로봇)", "Task Planning Agent（ドリンク製造ロボット）"),
                 ["op_inhouse", "test"], L(
                    "The LLM composes skills (cup, ice, and beverage dispensing, arm motion, loading) into a making sequence. {{b}}In operation (in-house):{{/b}} making in-house delivery orders and loading them onto the delivery robot. On failure, the remaining plan is rebuilt. {{b}}Real-robot testing:{{/b}} off-menu requests (ice water), custom drinks (extra shot), and deciding the order of responses to anomalies detected by the VLM. Not yet offered to store customers.",
                    "컵·얼음·음료 추출, 로봇팔 이동, 적재 skill을 LLM이 조합해 제조 순서를 계획. {{b}}운영 (사내):{{/b}} 사내 배송 주문의 제조와 배송 로봇 적재. 실패하면 남은 계획을 다시 만듦. {{b}}실로봇 테스트:{{/b}} 메뉴에 없는 요청(얼음물), 커스텀 음료(샷 추가), VLM이 감지한 이상 상황의 대응 순서 판단. 매장 고객에게는 아직 제공 전.",
                    "カップ・氷・ドリンクの抽出、ロボットアームの移動、積み込みのskillをLLMが組み合わせて製造手順を計画します。{{b}}運用中（社内）：{{/b}}社内配送注文の製造と配送ロボットへの積み込み。失敗した場合は残りの計画を作り直します。{{b}}実機テスト：{{/b}}メニューにない要望（氷水）、カスタムドリンク（ショット追加）、VLMが検知した異常への対応順序の判断。店舗のお客様にはまだ提供していません。",
                )),
                (L("Task Planning Agent (semi-humanoid robot)", "Task Planning Agent (세미 휴머노이드 로봇)", "Task Planning Agent（セミヒューマノイドロボット）"),
                 ["test"], L(
                    "Plans an order such as “bag two salt breads” as a repetition of find the product by camera → select the target → pick-and-place. It retries on a failed grasp, searches again after a drop, and when stock runs out it replans the remaining order or calls a person. Right before each bagging it checks that the target is still in the remaining order, so a product different from the order is not bagged.",
                    "\"소금빵 2개 담아줘\" 주문을 camera로 상품 찾기 → 대상 선택 → pick-and-place의 반복으로 계획. 잡기에 실패하면 재시도, 놓치면 다시 검색, 재고가 없으면 남은 주문을 재계획하거나 사람을 호출. 담기 직전마다 대상이 남은 주문에 있는지 확인해 주문과 다른 상품을 담지 않음.",
                    "「塩パンを2個入れて」という注文を、cameraで商品を探す → 対象を選ぶ → pick-and-place の繰り返しとして計画します。把持に失敗すれば再試行し、落とせば再検索し、在庫がなければ残りの注文を再計画するか人を呼びます。袋に入れる直前ごとに対象が残りの注文にあるかを確認し、注文と異なる商品を入れません。",
                )),
            ]),
            (L("Components shared by every agent", "Agent 공통 구성요소", "agent共通の構成要素"), [
                ("Context Manager", ["op_inhouse"], L(
                    "Keeps the current state, such as robot position, held object, and equipment stock, as world state and a scene graph, and builds the LLM input from only the part a request needs. Completion is confirmed by observation, not by the robot's success response.",
                    "로봇 위치, 들고 있는 물체, 장비 재고 같은 현재 상태를 world state와 scene graph로 유지하고, 요청에 필요한 부분만 LLM 입력으로 구성. 완료는 로봇의 성공 응답이 아니라 observation으로 확인.",
                    "ロボットの位置、持っている物体、機器の在庫などの現在の状態をworld stateとscene graphとして保持し、依頼に必要な部分だけをLLMの入力として構成します。完了は、ロボットの成功応答ではなくobservationで確認します。",
                )),
                ("Plan Validator", ["op_inhouse"], L(
                    "Before a plan made by the LLM is sent to the robot, it is executed step by step in advance on the current world state. The validator checks that each step is a skill of that robot, that the order is right, and that the step is feasible given position, load capacity, and equipment state. It also checks that hallucination has not inserted work different from the request. A plan that fails (for example, over the load limit) is sent back for replanning with the reason attached.",
                    "LLM이 만든 plan을 로봇에 보내기 전에 현재 world state 위에서 한 단계씩 미리 실행. 그 로봇의 skill인지, 순서가 맞는지, 위치·적재 용량·장비 상태로 수행 가능한지 검사하고, hallucination으로 요청과 다른 작업이 들어가지 않았는지 확인. 통과하지 못하면(예: 적재 한도 초과) 이유를 붙여 재계획을 요청.",
                    "LLMが作ったplanをロボットに送る前に、現在のworld state上で1ステップずつ事前に実行します。そのロボットのskillであるか、順序が正しいか、位置・積載容量・機器の状態から実行可能かを検査し、hallucinationによって依頼と異なる作業が入っていないかを確認します。通過しない場合（例：積載上限の超過）は、理由を付けて再計画を求めます。",
                )),
                ("Planning evaluation", ["sim"], L(
                    "For each request, required conditions are defined (for example, delivery only after making is finished, and the load limit respected), and the plan and the execution result are scored separately. Evaluation runs through the same code path as real operation, and the answer conditions are not given to the planner. (Co-developed with a teammate.)",
                    "요청마다 필수 조건(예: 제조가 끝난 뒤 배송, 적재 한도 준수)을 정해 plan과 실행 결과를 따로 채점. 평가도 실제 운영과 같은 code 경로로 실행하고, 정답 조건은 planner에 주지 않음. (팀원과 공동 개발)",
                    "依頼ごとに必須条件（例：製造が終わってから配送、積載上限の順守）を定め、planと実行結果を別々に採点します。評価も実際の運用と同じcode経路で実行し、正解条件はplannerに与えません。（チームメンバーと共同開発）",
                )),
            ]),
        ],
        "diagram": {
            "caption": L("From a request to execution: the LLM plans, code validates",
                         "요청에서 실행까지: LLM이 계획하고 code가 검증",
                         "依頼から実行まで：LLMが計画し、codeが検証"),
            "steps": [
                (L("Request", "요청", "依頼"),
                 L("natural language", "자연어", "自然言語")),
                ("Context Manager",
                 L("world state and scene graph → LLM input", "world state, scene graph → LLM 입력", "world state、scene graph → LLMの入力")),
                ("Task Planner (LLM)",
                 L("composes skills into a plan", "skill을 조합해 plan 작성", "skillを組み合わせてplanを作成")),
                ("Plan Validator",
                 L("runs the plan step by step on the world state", "world state 위에서 한 단계씩 미리 실행", "world state上で1ステップずつ事前に実行")),
                ("Executor",
                 L("skill, manipulation policy", "skill, manipulation policy", "skill、manipulation policy")),
                ("Observation",
                 L("completion is confirmed, world state is updated", "완료를 확인하고 world state를 갱신", "完了を確認し、world stateを更新")),
            ],
            "note": L(
                "When validation fails, the plan goes back to the Task Planner with the reason attached. When execution fails, the remaining plan is rebuilt.",
                "검증을 통과하지 못하면 이유를 붙여 Task Planner로 되돌립니다. 실행이 실패하면 남은 계획을 다시 만듭니다.",
                "検証を通過しない場合は、理由を付けてTask Plannerに戻します。実行が失敗した場合は、残りの計画を作り直します。",
            ),
        },
    },
    {
        "id": "manipulation",
        "title": "Teleoperation & Manipulation Learning",
        "role": L("Teleoperation code and policy training", "teleoperation code·policy 학습 담당", "teleoperationのcodeとpolicyの学習を担当"),
        "period": L("2024.11 – present", "2024.11 - 현재", "2024.11 - 現在"),
        "scale": None,
        "scale_op": False,
        "video": None,
        "context": L(
            "Clearing trash, bagging bread, and pouring water for drip coffee involve objects without a fixed shape or need both arms together, so predefined motions were not enough. Data of a person directly operating the robot was collected, and the motions were learned from it.",
            "쓰레기 치우기, 빵 담기, 드립 커피의 물 붓기는 대상의 모양이 일정하지 않거나 양팔을 함께 써야 해서 정해진 동작으로는 하기 어려웠습니다. 사람이 로봇을 직접 조작한 데이터를 모아 그 동작을 학습시켰습니다.",
            "ゴミの片付け、パンの袋詰め、ドリップコーヒーの湯注ぎは、対象の形が一定でなかったり、両腕を同時に使う必要があったりして、決まった動作では困難でした。人がロボットを直接操作したデータを集め、その動作を学習させました。",
        ),
        "groups": [
            (None, [
                ("Manipulation policy (single-arm)", ["op"], L(
                    "The beverage-making robot clears trash from the pickup shelf. Unlike cups, trash has no fixed shape, so it is hard to grasp with rules. The arm approaches the position found by the ceiling camera, and then a policy I trained picks the object up and drops it at the disposal position. The policy input is the live gripper-camera image. In operation at company-run stores.",
                    "음료 제조 로봇이 픽업 선반 위의 쓰레기를 치움. 컵과 달리 모양이 정해지지 않아 규칙으로는 집기 어려움. 천장 camera로 찾은 위치 근처까지 로봇팔이 접근한 뒤, 직접 학습한 policy가 집어서 폐기 위치에 버림. policy 입력은 실시간 gripper camera image. 직영 매장에서 운영.",
                    "ドリンク製造ロボットがピックアップ棚の上のゴミを片付けます。カップと違って形が決まっていないため、ルールでは把持が困難です。天井cameraで見つけた位置の近くまでロボットアームが接近した後、自ら学習したpolicyが把持して廃棄位置に捨てます。policyの入力はリアルタイムのgripper camera imageです。直営店舗で運用しています。",
                )),
                ("Manipulation policy (bimanual)", ["test"], L(
                    "The semi-humanoid robot picks up packaged bread with both arms and puts it in a bag. I trained a policy of the Diffusion Policy family. I connected the Task Planning Agent so that it calls this policy, and a VLA trained by a teammate, with an instruction text and an image in which everything except the target is masked.",
                    "세미 휴머노이드 로봇이 포장된 빵을 양팔로 집어 봉투에 담음. Diffusion Policy 계열 policy를 직접 학습. Task Planning Agent가 대상 외 영역을 가린 image와 지시문으로 이 policy와 팀원이 학습한 VLA를 호출하도록 연결.",
                    "セミヒューマノイドロボットが包装されたパンを両腕で把持して袋に入れます。Diffusion Policy系のpolicyを自ら学習しました。Task Planning Agentが、対象以外の領域を隠したimageと指示文で、このpolicyとチームメンバーが学習したVLAを呼び出すように接続しました。",
                )),
                ("Teleoperation", ["ongoing"], L(
                    "I implemented the control code (joint mapping, control loop) and the demonstration-collection code for single-arm and bimanual leader-follower teleoperation. Camera images, robot state, and actions are time-aligned and stored as an episode dataset (HDF5) that is used for policy training.",
                    "single-arm과 bimanual leader-follower teleoperation의 제어 code(joint mapping, 제어 loop)와 데모 수집 code를 구현. camera image와 로봇 state, action을 시간 정렬한 episode dataset(HDF5)으로 저장해 policy 학습에 사용.",
                    "single-armとbimanualのleader-follower teleoperationの制御code（joint mapping、制御loop）とデモ収集codeを実装しました。camera image、ロボットのstate、actionを時刻同期し、episode単位のdataset（HDF5）として保存してpolicyの学習に使います。",
                )),
                ("Drip coffee", ["past"], L(
                    "Sole developer. Drip-coffee making was split into segments: grasping the kettle and placing the filter were learned with Diffusion Policy (IL), and pouring water with PPO (RL). PPO was trained in simulation (MuJoCo) and then tuned on the real robot. After real-robot evaluation it was used in the store service.",
                    "단독 개발. 드립 커피 제조를 구간으로 나눠 주전자 잡기와 필터 놓기는 Diffusion Policy(IL), 물 붓기는 PPO(RL)로 학습. PPO는 simulation(MuJoCo)에서 학습한 뒤 실로봇에서 조정. 실로봇 평가 뒤 매장 서비스에 사용.",
                    "単独で開発しました。ドリップコーヒーの製造を区間に分け、ケトルの把持とフィルターの設置はDiffusion Policy（IL）、湯注ぎはPPO（RL）で学習しました。PPOはsimulation（MuJoCo）で学習した後、実機で調整しました。実機評価の後、店舗サービスで使用されました。",
                )),
            ]),
        ],
        "diagram": {
            "caption": L("From demonstrations to a policy in operation",
                         "데모 수집에서 policy 운영까지",
                         "デモ収集からpolicyの運用まで"),
            "steps": [
                ("Teleoperation",
                 L("leader-follower, single-arm and bimanual", "leader-follower, single-arm과 bimanual", "leader-follower、single-armとbimanual")),
                (L("Demonstration collection", "데모 수집", "デモ収集"),
                 L("image, state, action, time-aligned", "image, state, action을 시간 정렬", "image、state、actionを時刻同期")),
                (L("Episode dataset", "Episode dataset", "Episode dataset"), "HDF5"),
                (L("Policy training", "Policy 학습", "Policyの学習"),
                 L("Diffusion Policy family", "Diffusion Policy 계열", "Diffusion Policy系")),
                (L("Real-robot testing", "실로봇 테스트", "実機テスト"), None),
                (L("Operation", "운영", "運用"),
                 L("single-arm policy, in stores", "single-arm policy, 매장", "single-arm policy、店舗")),
            ],
        },
    },
]

# ---------------------------------------------------------------- Scenarios

SCENARIOS_INTRO = L(
    "Three cases that show how the layers work together.",
    "계층들이 함께 움직이는 방식을 보여 주는 세 가지 사례입니다.",
    "各階層がどのように連携するかを示す3つの事例です。",
)

SCENARIOS = [
    {
        "title": L("Beverage delivery inside the building", "건물 안 음료 배달", "社屋内のドリンク配送"),
        "status": ["op_inhouse"],
        "request": L("“Two Americanos to the meeting room.”", "\"아메리카노 2잔을 회의실로.\"", "「アメリカーノ2杯を会議室へ」"),
        "steps": [
            ("Orchestrator Agent", L(
                "Splits the natural-language request into tasks.",
                "자연어 요청을 작업으로 나눔.",
                "自然言語の依頼を作業に分けます。")),
            (L("Task Planning Agent (beverage-making robot)", "Task Planning Agent (음료 제조 로봇)", "Task Planning Agent（ドリンク製造ロボット）"), L(
                "Plans the making sequence. The Plan Validator checks the plan before it is sent. The robot makes the drinks and loads them onto the delivery robot.",
                "제조 순서를 계획. Plan Validator가 plan을 보내기 전에 검사. 로봇이 음료를 만들어 배송 로봇에 적재.",
                "製造手順を計画します。Plan Validatorがplanを送る前に検査します。ロボットがドリンクを作り、配送ロボットに積み込みます。")),
            (L("Orchestrator Agent → delivery robot", "Orchestrator Agent → 배송 로봇", "Orchestrator Agent → 配送ロボット"), L(
                "Instructs the delivery robot in order: move, ride the elevator, hand over.",
                "배송 로봇에 이동, 엘리베이터 탑승, 전달을 순서대로 지시.",
                "配送ロボットに移動、エレベーター乗車、受け渡しを順に指示します。")),
            (L("On failure", "실패하면", "失敗した場合"), L(
                "The remaining plan is rebuilt.",
                "남은 계획을 다시 만듦.",
                "残りの計画を作り直します。")),
        ],
    },
    {
        "title": L("Anomaly handling in an unstaffed store", "무인 매장의 이상 상황 대응", "無人店舗での異常対応"),
        "status": ["op"],
        "request": L("A cup falls over in the store.", "매장에서 컵이 쓰러짐.", "店舗でカップが倒れます。"),
        "steps": [
            ("Perception", L(
                "Camera images and robot and equipment state are bundled every 2 seconds.",
                "camera image와 로봇·장비 상태를 2초마다 묶음.",
                "camera imageとロボット・機器の状態を2秒ごとにまとめます。")),
            ("VLM", L(
                "The VLM fine-tuned with QLoRA classifies the situation: a fallen cup, contamination, equipment failure, and others (12+ in total).",
                "QLoRA로 fine-tuning한 VLM이 상황을 분류: 컵 쓰러짐, 오염, 고장 등 12종 이상.",
                "QLoRAでfine-tuningしたVLMが状況を分類します：カップの転倒、汚れ、故障など12種類以上。")),
            (L("Recovery", "복구", "復旧"), L(
                "A predefined recovery action runs according to the result.",
                "결과에 따라 정해 둔 복구 동작을 실행.",
                "結果に応じて、あらかじめ決めた復旧動作を実行します。")),
            (L("Alert", "알림", "通知"), L(
                "A person is notified when one is needed.",
                "사람이 필요하면 알림.",
                "人が必要な場合は通知します。")),
        ],
        "note": L(
            "In operation at company-run stores. Letting the Task Planning Agent decide the order of responses is in real-robot testing.",
            "직영 매장에서 운영. Task Planning Agent가 대응 순서를 판단하는 방식은 실로봇 테스트 단계.",
            "直営店舗で運用しています。Task Planning Agentが対応順序を判断する方式は実機テスト段階です。",
        ),
    },
    {
        "title": L("Bagging bread with two arms", "양팔로 빵 담기", "両腕でのパンの袋詰め"),
        "status": ["test"],
        "request": L("“Bag two salt breads.”", "\"소금빵 2개 담아줘.\"", "「塩パンを2個入れて」"),
        "steps": [
            (L("Task Planning Agent (semi-humanoid robot)", "Task Planning Agent (세미 휴머노이드 로봇)", "Task Planning Agent（セミヒューマノイドロボット）"), L(
                "Plans the order as a repetition of find the product by camera → select the target → pick-and-place.",
                "주문을 camera로 상품 찾기 → 대상 선택 → pick-and-place의 반복으로 계획.",
                "注文を、cameraで商品を探す → 対象を選ぶ → pick-and-place の繰り返しとして計画します。")),
            (L("Check before bagging", "담기 직전 확인", "袋に入れる直前の確認"), L(
                "Confirms that the target is still in the remaining order.",
                "대상이 남은 주문에 있는지 확인.",
                "対象が残りの注文にあるかを確認します。")),
            ("Manipulation policy · VLA", L(
                "Called with an instruction text and an image in which everything except the target is masked. The robot picks up the bread with both arms and puts it in the bag.",
                "대상 외 영역을 가린 image와 지시문으로 호출. 로봇이 빵을 양팔로 집어 봉투에 담음.",
                "対象以外の領域を隠したimageと指示文で呼び出します。ロボットがパンを両腕で把持して袋に入れます。")),
            (L("On failure", "실패하면", "失敗した場合"), L(
                "Failed grasp: retry. Dropped: search again. Out of stock: replan the remaining order or call a person.",
                "잡기 실패: 재시도. 놓침: 다시 검색. 재고 없음: 남은 주문을 재계획하거나 사람을 호출.",
                "把持の失敗：再試行。落下：再検索。在庫なし：残りの注文を再計画するか人を呼びます。")),
        ],
    },
]

# ---------------------------------------------------------------- Experience

EXPERIENCE = [
    {
        "org": "XYZ Inc",
        "role": "Researcher, Robot Intelligence Team",
        "period": L("2023.10 – present", "2023.10 - 현재", "2023.10 - 現在"),
        "lines": [
            L("A robot service company that operates unmanned robot cafés, where robots make and serve drinks, in 40+ stores.",
              "로봇이 음료를 만들어 제공하는 무인 로봇카페를 40여 개 매장에서 운영하는 로봇 서비스 기업",
              "ロボットがドリンクを作って提供する無人ロボットカフェを、40以上の店舗で運営するロボットサービス企業"),
            L("5-person team. Sole developer of the perception runtime and the deployment system. Project Lead of the agent system: design, task planning, Plan Validator, and Context Manager (MCP connection, robot integration, and evaluation were shared work). For manipulation: teleoperation code and policy training. The navigation system is outside my scope.",
              "5인 팀. perception runtime과 배포 체계는 단독 개발. agent 시스템은 Project Lead로 설계와 task planning, Plan Validator, Context Manager 개발(MCP 연결, 로봇 연동, 평가는 공동). manipulation은 teleoperation code와 policy 학습. 주행 시스템은 담당 밖.",
              "5人チーム。perception runtimeとデプロイの仕組みは単独で開発しました。agentシステムはProject Leadとして、設計とtask planning、Plan Validator、Context Managerを開発しました（MCP接続、ロボット連携、評価は共同）。manipulationではteleoperationのcodeとpolicyの学習を担当しました。走行システムは担当外です。"),
            L("Four robot types: beverage-making robot (rail-mounted manipulator), semi-humanoid mobile dual-arm robot, autonomous delivery robot, autonomous cleaning robot.",
              "대상 로봇 4종: 음료 제조 로봇(레일형 매니퓰레이터), 세미 휴머노이드 모바일 양팔 로봇, 자율주행 배송 로봇, 자율주행 청소 로봇",
              "対象ロボット4種：ドリンク製造ロボット（レール型マニピュレータ）、セミヒューマノイドのモバイル双腕ロボット、自律走行の配送ロボット、自律走行の清掃ロボット"),
        ],
    },
    {
        "org": "POSTECH Artificial Intelligence Institute",
        "role": "Intern Researcher",
        "period": "2023.05 – 2023.06",
        "lines": [
            L("Took part in building an experiment framework that compares combinations of preprocessing (blur, binarization, morphology, denoising) for footprint and tire-mark images.",
              "족적과 타이어 흔적 image의 전처리 조합(blur, binarization, morphology, denoising)을 비교하는 실험 framework 구축에 참여.",
              "足跡とタイヤ痕のimageの前処理の組み合わせ（blur、binarization、morphology、denoising）を比較する実験frameworkの構築に参加しました。"),
        ],
    },
]

EDUCATION = {
    "org": L("Hanyang University", "Hanyang University", "Hanyang University（漢陽大学校）"),
    "role": "B.S. in Electrical Engineering",
    "period": L("2014 – 2022 (including military service)", "2014 - 2022 (군 복무 포함)", "2014 - 2022（兵役を含む）"),
}

# ---------------------------------------------------------------- Skills

SKILLS = [
    ("Robot Agent / LLM",
     L("LLM task planning, plan validation, replanning, MCP, scene graph",
       "LLM task planning, plan validation, replanning, MCP, scene graph",
       "LLM task planning、plan validation、replanning、MCP、scene graph")),
    ("Perception / Edge AI",
     L("stereo depth, object detection/tracking, VLM fine-tuning (QLoRA), PyTorch, TensorRT, Jetson",
       "stereo depth, object detection/tracking, VLM fine-tuning (QLoRA), PyTorch, TensorRT, Jetson",
       "stereo depth、object detection/tracking、VLM fine-tuning（QLoRA）、PyTorch、TensorRT、Jetson")),
    ("Robot Learning",
     L("teleoperation, imitation learning (Diffusion Policy), VLA integration, reinforcement learning (PPO), MuJoCo",
       "teleoperation, imitation learning (Diffusion Policy), VLA 연동, reinforcement learning (PPO), MuJoCo",
       "teleoperation、imitation learning（Diffusion Policy）、VLA連携、reinforcement learning（PPO）、MuJoCo")),
    ("Robotics / Deployment",
     L("ROS 2, C++, Python, OTA (Ansible), MLOps, camera calibration, systemd",
       "ROS 2, C++, Python, OTA (Ansible), MLOps, camera calibration, systemd",
       "ROS 2、C++、Python、OTA（Ansible）、MLOps、camera calibration、systemd")),
]

# ---------------------------------------------------------------- Contact

CONTACT_INTRO = L(
    "Email is the fastest way to reach me.",
    "이메일로 연락 주시면 가장 빠릅니다.",
    "メールでのご連絡が最も早いです。",
)

FOOTER = L("Junho Kim", "김준호", "Junho Kim")
