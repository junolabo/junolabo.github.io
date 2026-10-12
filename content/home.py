# First page.
from .common import L

META_DESCRIPTION = L(
    "Junho Kim. Robot Intelligence engineer. Robot perception, LLM-based task planning, and learning-based manipulation built as one connected system.",
    "김준호. Robot Intelligence 엔지니어. 로봇의 perception, LLM 기반 task planning, 학습 기반 manipulation을 하나로 이어지는 시스템으로 설계하고 구현합니다.",
    "Junho Kim。Robot Intelligenceエンジニア。ロボットのperception、LLMによるtask planning、学習ベースのmanipulationを、ひとつにつながるシステムとして設計・実装しています。",
)

INTRO = [
    L("I design and build robot perception, LLM-based task planning, and learning-based manipulation as one connected system.",
      "로봇의 perception, LLM 기반 task planning, 학습 기반 manipulation을 하나로 이어지는 시스템으로 직접 설계하고 구현합니다.",
      "ロボットのperception、LLMによるtask planning、学習ベースのmanipulationを、ひとつにつながるシステムとして自ら設計・実装しています。"),
    L("The system runs unmanned robot cafés. Perception and the single-arm manipulation policy are in operation in stores, and the agent system is in operation in-house.",
      "이 시스템은 무인 로봇카페를 운영합니다. perception과 single-arm manipulation policy는 매장에서, agent 시스템은 사내에서 운영하고 있습니다.",
      "このシステムは無人ロボットカフェを運営しています。perceptionとsingle-arm manipulation policyは店舗で、agentシステムは社内で運用しています。"),
]

LOCATION = "Seoul, Korea"
LANGUAGES = L(
    "Korean (native), English (conversational), Japanese (conversational)",
    "한국어 (모국어), 영어 (일상 대화), 일본어 (일상 대화)",
    "韓国語（母語）、英語（日常会話）、日本語（日常会話）",
)

# ---------------------------------------------------------------- purpose

PURPOSE_TITLE = L("Why these projects exist", "이 프로젝트들이 필요했던 이유", "これらのプロジェクトが必要だった理由")
PURPOSE = [
    L("The goal is to run a store with as little human involvement as possible. Two conditions followed from that goal.",
      "목적은 매장을 최대한 자동화로 운영하는 것입니다. 이 목적에서 두 가지 조건이 나왔습니다.",
      "目的は、店舗をできる限り自動で運営することです。この目的から2つの条件が生まれました。"),
    L("First, irregular situations, and situations that used to need a person (a manager sent to the store, or an operator watching remotely), have to be handled by the robot as far as a robot can. Second, the store has to respond as flexibly as a staffed store.",
      "첫째, 비정형 상황과 사람이 필요하던 상황(매장에 출동하던 관리자, 원격으로 지켜보던 운영 인력)을 로봇만으로 가능한 수준까지 대처해야 합니다. 둘째, 유인 매장처럼 유연하게 응대해야 합니다.",
      "第一に、非定型の状況や、これまで人が必要だった状況（店舗に出向く管理者、遠隔で見守るオペレーター）を、ロボットだけで可能な範囲まで処理する必要があります。第二に、有人店舗のように柔軟に対応する必要があります。"),
    L("The scope then grew to delivery and cleaning inside the company building. Every project below was added or improved for these needs. They are layers of one system, not separate projects.",
      "그 뒤 회사 건물 안의 배송과 청소까지 범위를 넓혔습니다. 아래의 모든 프로젝트는 이 필요에 따라 더해지고 개선된 것입니다. 서로 다른 프로젝트가 아니라 한 시스템의 계층입니다.",
      "その後、社屋内の配送と清掃まで範囲を広げました。以下のすべてのプロジェクトは、この必要に応じて追加・改善したものです。別々のプロジェクトではなく、ひとつのシステムの階層です。"),
]

# ---------------------------------------------------------------- system map

SYSTEM_TITLE = L("System map", "System map", "System map")
SYSTEM_INTRO = L(
    "Each layer links to the page that explains it.",
    "각 계층은 그 계층을 설명하는 페이지로 이어집니다.",
    "各階層から、その階層を説明するページに移動できます。",
)
SYSTEM_HEAD = ["Layer", "Role", "Status", L("Explained in", "설명 페이지", "説明ページ")]
# (layer, role, status keys, [(page slug, label)])
SYSTEM_MAP = [
    ("Orchestrator Agent",
     L("Distributes work across robots", "로봇 간 작업 배분", "ロボット間の作業配分"),
     ["op_inhouse", "test"], [("agent-system", "Project 2")]),
    ("Task Planning Agent",
     L("Per-robot LLM task planning, validation, replanning",
       "로봇별 LLM task planning, validation, replanning",
       "ロボットごとのLLM task planning、validation、replanning"),
     ["op_inhouse", "test"], [("agent-system", "Project 2")]),
    ("Execution",
     L("skill, manipulation policy", "skill, manipulation policy", "skill、manipulation policy"),
     ["op", "test"], [("manipulation-learning", "Project 3")]),
    ("Perception",
     L("depth · detection · tracking, VLM anomaly detection",
       "depth · detection · tracking, VLM anomaly detection",
       "depth · detection · tracking、VLM anomaly detection"),
     ["op"], [("perception-runtime", "Project 1-1"), ("anomaly-detection", "Project 1-2")]),
    ("Cross-cutting: Data · Evaluation · Deployment",
     L("MLOps, evaluation, OTA", "MLOps, 평가, OTA", "MLOps、評価、OTA"),
     ["op", "sim_eval"], [("deployment", "Project 1-3")]),
]

PROJECTS_TITLE = L("Projects", "Projects", "Projects")
PROJECTS_INTRO = L(
    "XYZ Inc · Robot Intelligence Team · 2023.10 – present. The three projects are the same as on my resume. Project 1 is explained in three parts.",
    "XYZ Inc · Robot Intelligence Team · 2023.10 - 현재. 세 프로젝트는 이력서와 같습니다. 1번 프로젝트는 세 부분으로 나눠 설명합니다.",
    "XYZ Inc · Robot Intelligence Team · 2023.10 - 現在。3つのプロジェクトは履歴書と同じです。Project 1は3つのパートに分けて説明します。",
)

# ---------------------------------------------------------------- connections

CONNECT_TITLE = L("What connecting them makes possible", "연결했기 때문에 가능해진 것", "つなげたことで可能になったこと")
CONNECT_INTRO = L(
    "Each row is a result that needs two parts of the system together.",
    "각 행은 시스템의 두 부분이 함께 있어야 나오는 결과입니다.",
    "各行は、システムの2つの部分がそろって初めて得られる結果です。",
)
CONNECT_HEAD = [L("Connected parts", "연결한 것", "つなげたもの"), L("Result", "결과", "結果"), L("Status", "상태", "状態")]
CONNECTIONS = [
    (L("Camera observation + the robot's work state",
       "camera 관측 + 로봇의 작업 상태",
       "cameraの観測 + ロボットの作業状態"),
     L("When a cup disappears from the shelf, customer pickup and robot removal are told apart.",
       "선반에서 컵이 사라졌을 때 고객 수령과 로봇 회수를 구분합니다.",
       "棚からカップが消えたとき、お客様の受け取りとロボットによる回収を区別します。"),
     ["op"]),
    (L("Ceiling-camera position + learned single-arm policy",
       "천장 camera의 위치 + 학습한 single-arm policy",
       "天井cameraの位置 + 学習したsingle-arm policy"),
     L("The arm approaches by position, and the policy does only the grasp of trash that has no fixed shape.",
       "로봇팔은 위치로 접근하고, 모양이 정해지지 않은 쓰레기를 집는 동작만 policy가 맡습니다.",
       "ロボットアームは位置で接近し、形の決まっていないゴミを把持する動作だけをpolicyが担当します。"),
     ["op"]),
    (L("Store data + MLOps pipeline",
       "매장 데이터 + MLOps pipeline",
       "店舗データ + MLOps pipeline"),
     L("The stereo, detection, and VLM models are updated from the stores' own data, and a new model is deployed only after it passes on the target store and on all stores.",
       "stereo, detection, VLM 모델을 매장의 데이터로 갱신합니다. 새 모델은 해당 매장과 전체 매장에서 모두 통과해야 배포됩니다.",
       "stereo、detection、VLMのモデルを店舗自身のデータで更新します。新しいモデルは、対象店舗と全店舗の両方で通過した場合のみデプロイされます。"),
     ["op"]),
    (L("VLM anomaly detection + Orchestrator Agent",
       "VLM anomaly detection + Orchestrator Agent",
       "VLM anomaly detection + Orchestrator Agent"),
     L("When contamination is detected, the cleaning robot is dispatched.",
       "오염을 감지하면 청소 로봇을 보냅니다.",
       "汚れを検知すると、清掃ロボットを向かわせます。"),
     ["op_inhouse"]),
    (L("Orchestrator Agent + Task Planning Agent + delivery robot",
       "Orchestrator Agent + Task Planning Agent + 배송 로봇",
       "Orchestrator Agent + Task Planning Agent + 配送ロボット"),
     L("One natural-language request becomes making, loading, moving between floors, and handing over.",
       "자연어 요청 하나가 제조, 적재, 층간 이동, 전달로 이어집니다.",
       "ひとつの自然言語の依頼が、製造、積み込み、フロア間の移動、受け渡しにつながります。"),
     ["op_inhouse"]),
    (L("Task Planning Agent + manipulation policy and VLA",
       "Task Planning Agent + manipulation policy와 VLA",
       "Task Planning Agent + manipulation policyとVLA"),
     L("The planner calls a learned policy with an instruction text and an image in which everything except the target is masked.",
       "planner가 대상 외 영역을 가린 image와 지시문으로 학습한 policy를 호출합니다.",
       "plannerが、対象以外の領域を隠したimageと指示文で、学習したpolicyを呼び出します。"),
     ["test"]),
    (L("VLM anomaly detection + Task Planning Agent",
       "VLM anomaly detection + Task Planning Agent",
       "VLM anomaly detection + Task Planning Agent"),
     L("The agent decides the order of responses to an anomaly.",
       "이상 상황의 대응 순서를 agent가 판단합니다.",
       "異常への対応順序をagentが判断します。"),
     ["test"]),
]

# ---------------------------------------------------------------- experience

EXPERIENCE_TITLE = "Experience"
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

EDUCATION_TITLE = "Education"
EDUCATION = {
    "org": L("Hanyang University", "Hanyang University", "Hanyang University（漢陽大学校）"),
    "role": "B.S. in Electrical Engineering",
    "period": L("2014 – 2022 (including military service)", "2014 - 2022 (군 복무 포함)", "2014 - 2022（兵役を含む）"),
}

SKILLS_TITLE = "Skills"
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

CONTACT_TITLE = "Contact"
CONTACT_INTRO = L(
    "Email is the fastest way to reach me.",
    "이메일로 연락 주시면 가장 빠릅니다.",
    "メールでのご連絡が最も早いです。",
)
