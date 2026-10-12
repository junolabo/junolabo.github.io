# Project 1, part 2: VLM Anomaly Detection.
from .common import L, T_DECISION, T_SCOPE, SC_STATUS, SC_MINE, SC_EXISTING

PAGE = {
    "slug": "anomaly-detection",
    "project": 1,
    "title": "VLM Anomaly Detection",
    "claim": L(
        "A fine-tuned VLM classifies 12+ kinds of anomalies from camera images and from robot and equipment state. Where the robot can recover, it recovers. Where it cannot, a person is called.",
        "fine-tuning한 VLM이 camera image와 로봇·장비 상태로 이상 상황을 12종 이상 분류합니다. 로봇이 복구할 수 있으면 로봇이 복구하고, 할 수 없으면 사람을 부릅니다.",
        "fine-tuningしたVLMが、camera imageとロボット・機器の状態から12種類以上の異常を分類します。ロボットが復旧できる場合はロボットが復旧し、できない場合は人を呼びます。",
    ),
    "facts": [
        ("role", L("Sole developer", "단독 개발", "単独開発")),
        ("period", L("Part of Project 1 (2023.10 – present)", "Project 1의 일부 (2023.10 - 현재)", "Project 1の一部（2023.10 - 現在）")),
        ("status", ("st", ["op_direct"])),
    ],
    "blocks": [
        ("h2", "problem"),
        ("p", L(
            "Checking whether something went wrong in a store used to need a person: a manager who went to the store, or an operator who watched remotely. To run without them, the system has to notice the situation and also decide what to do about it.",
            "매장에 문제가 생겼는지 확인하는 일에는 사람이 필요했습니다. 매장에 나가는 관리자나 원격으로 지켜보는 운영 인력이 맡았습니다. 이들 없이 운영하려면, 시스템이 상황을 알아차리고 무엇을 할지까지 정해야 합니다.",
            "店舗で何かが起きていないかを確認する作業には、人が必要でした。店舗に出向く管理者や、遠隔で見守るオペレーターが担当していました。その人たちなしで運営するには、システムが状況に気づき、何をするかまで決める必要があります。")),
        ("points", [
            (L("Anomalies have no fixed shape.", "이상 상황은 모양이 정해져 있지 않습니다.", "異常には決まった形がありません。"),
             L("A fallen cup, contamination, an equipment failure, and many others. Writing a separate rule or detector for every kind does not keep up with the kinds that appear.",
               "컵 쓰러짐, 오염, 장비 고장 등 종류가 많습니다. 종류마다 규칙이나 검출기를 따로 만드는 방식으로는 새로 나타나는 종류를 따라가지 못합니다.",
               "カップの転倒、汚れ、機器の故障など、種類が多くあります。種類ごとにルールや検出器を作る方式では、新しく現れる種類に追いつけません。")),
            (L("The image alone is not enough.", "영상만으로는 부족합니다.", "映像だけでは足りません。"),
             L("An image does not show what the robot and the equipment are doing at that moment. The state has to be read together with the image.",
               "영상에는 그 순간 로봇과 장비가 무엇을 하고 있는지가 나오지 않습니다. 상태를 영상과 함께 읽어야 합니다.",
               "映像には、その瞬間にロボットと機器が何をしているかは映りません。状態を映像とあわせて読む必要があります。")),
            (L("A wrong classification must not turn into a robot action.", "틀린 분류가 로봇 동작이 되면 안 됩니다.", "誤った分類がロボットの動作になってはいけません。"),
             L("A model can be wrong, and its output can be malformed. Something has to stand between the model and the robot.",
               "모델은 틀릴 수 있고, 출력의 형식이 깨질 수도 있습니다. 모델과 로봇 사이에 검사하는 단계가 있어야 합니다.",
               "モデルは誤ることがあり、出力の形式が崩れることもあります。モデルとロボットの間に検査する段階が必要です。")),
            (L("The store was already in operation.", "매장은 이미 운영 중이었습니다.", "店舗はすでに運用中でした。"),
             L("The new function had to be added without changing the interfaces of the running system.",
               "운영 중인 시스템의 인터페이스를 바꾸지 않고 새 기능을 붙여야 했습니다.",
               "運用中のシステムのインターフェースを変えずに、新しい機能を追加する必要がありました。")),
        ]),

        ("h2", "structure"),
        ("flow", L("From observation to response", "관측에서 대응까지", "観測から対応まで"), [
            (L("Input bundle", "입력 묶음", "入力セット"), L("camera images + robot and equipment state, every 2 seconds", "camera image + 로봇·장비 상태, 2초마다", "camera image + ロボット・機器の状態、2秒ごと"), None),
            ("VLM", L("fine-tuned with QLoRA, classifies the situation", "QLoRA로 fine-tuning, 상황을 분류", "QLoRAでfine-tuning、状況を分類"), "judge"),
            (L("Fixed output format", "고정된 출력 형식", "固定の出力形式"), L("the output must follow a schema", "출력이 schema를 따라야 함", "出力はschemaに従う必要がある"), None),
            (L("Rule check", "규칙 검사", "ルールによる検査"), L("code checks the output before it is used", "출력을 쓰기 전에 code가 검사", "出力を使う前にcodeが検査"), "judge"),
            (L("Response", "대응", "対応"), L("a predefined recovery action by the robot, or an alert when a person is needed", "로봇이 정해 둔 복구 동작을 실행하거나, 사람이 필요하면 알림", "ロボットがあらかじめ決めた復旧動作を実行するか、人が必要な場合は通知"), None),
        ], L(
            "The VLM is used only for recognition. It does not control the robot.",
            "VLM은 인식에만 씁니다. 로봇을 제어하지 않습니다.",
            "VLMは認識にのみ使います。ロボットを制御しません。")),

        ("h2", "how"),
        ("h3", "VLM anomaly detection", ["op_direct"]),
        ("p", L(
            "Camera images and robot and equipment state are bundled every 2 seconds and given to the VLM. The VLM is a small model fine-tuned with QLoRA on store situations, and it classifies 12+ kinds of situations such as a fallen cup, contamination, and equipment failure.",
            "camera image와 로봇·장비 상태를 2초마다 묶어 VLM에 넣습니다. VLM은 매장 상황으로 QLoRA fine-tuning한 소형 모델이고, 컵 쓰러짐, 오염, 고장 등 12종 이상의 상황을 분류합니다.",
            "camera imageとロボット・機器の状態を2秒ごとにまとめてVLMに入力します。VLMは店舗の状況でQLoRA fine-tuningした小型モデルで、カップの転倒、汚れ、故障など12種類以上の状況を分類します。")),
        ("p", L(
            "The model's output is forced into a fixed schema, so code can parse it. Before the result is used, rule-based checks written in code look at it: whether the inputs were fresh, whether the nodes that supplied them were healthy, and whether the result is consistent with rules such as a hand entering the area or a spill.",
            "모델의 출력은 고정된 schema로 강제하므로 code가 해석할 수 있습니다. 결과를 쓰기 전에 code로 쓴 규칙이 검사합니다. 입력이 최신이었는지, 입력을 준 node가 정상이었는지, 손 진입이나 쏟아짐 같은 규칙과 결과가 맞는지를 봅니다.",
            "モデルの出力は固定のschemaに強制するため、codeで解析できます。結果を使う前に、codeで書いたルールが検査します。入力が最新だったか、入力を供給したnodeが正常だったか、手の進入やこぼれなどのルールと結果が合っているかを確認します。")),
        ("note", L(
            "Earlier version: an image anomaly detector found spills and heavy contamination and blocked serving on that slot. The VLM replaced it because a VLM fits situations that have no fixed shape better.",
            "이전 방식: 영상 이상 감지 모델이 음료 유출과 심한 오염을 찾아 그 칸의 서빙을 막았습니다. 모양이 정해지지 않은 상황에는 VLM이 더 알맞아서 VLM으로 바꿨습니다.",
            "以前の方式：画像の異常検知モデルがドリンクのこぼれとひどい汚れを見つけ、その区画への提供を止めていました。決まった形のない状況にはVLMの方が適しているため、VLMに置き換えました。")),

        ("h3", L("Response by situation", "상황별 대응", "状況ごとの対応"), None),
        ("p", L(
            "The principle: what the robot can fix, the robot fixes. What needs a person raises an alert.",
            "원칙: 로봇이 풀 수 있는 것은 로봇이 풉니다. 사람이 필요한 것은 알림을 보냅니다.",
            "原則：ロボットが解決できることはロボットが解決します。人が必要なことは通知します。")),
        ("table",
         [L("Situation", "상황", "状況"), L("Response", "대응", "対応"), L("Who acts", "누가 하는가", "誰が行うか")],
         [
             [L("A cup fell over. Nothing spilled.", "컵이 쓰러짐. 음료는 흐르지 않음", "カップが倒れた。ドリンクはこぼれていない"),
              L("The cup is picked up and disposed of.", "컵을 집어 폐기", "カップを把持して廃棄"),
              L("Robot", "로봇", "ロボット")],
             [L("A cup fell over and the drink spilled.", "컵이 쓰러지고 음료가 흐름", "カップが倒れ、ドリンクがこぼれた"),
              L("The manager is called.", "관리자 호출", "管理者を呼ぶ"),
              L("Person", "사람", "人")],
             [L("Contamination inside the building", "건물 안의 오염", "社屋内の汚れ"),
              L("The Orchestrator Agent dispatches the cleaning robot.", "Orchestrator Agent가 청소 로봇을 보냄", "Orchestrator Agentが清掃ロボットを向かわせる"),
              L("Cleaning robot", "청소 로봇", "清掃ロボット")],
             [L("A critical equipment failure", "치명적인 장비 고장", "致命的な機器の故障"),
              L("An alert is sent.", "알림 전송", "通知を送る"),
              L("Person", "사람", "人")],
         ], {"fail_rows": [1, 3]}),

        ("h3", L("Improving the model with reviewed cases", "검토한 사례로 모델 개선", "確認済みの事例によるモデルの改善"), None),
        ("p", L(
            "Cases where a person's review disagreed with the model go into the next training data. The VLM is one of the three models updated by the MLOps pipeline.",
            "사람이 검토한 결과가 모델과 달랐던 사례는 다음 학습 데이터로 들어갑니다. VLM은 MLOps pipeline으로 갱신하는 세 모델 중 하나입니다.",
            "人による確認の結果がモデルと異なった事例は、次の学習データに入ります。VLMは、MLOps pipelineで更新する3つのモデルのひとつです。")),

        ("h2", "decisions"),
        ("table", T_DECISION, [
            [L("The image is bundled with robot and equipment state.", "영상을 로봇·장비 상태와 묶음", "映像をロボット・機器の状態とまとめる"),
             L("An image does not show what the robot is doing.", "영상에는 로봇이 하는 일이 나오지 않음", "映像にはロボットの動作が映らない"),
             L("Judging a situation from the image alone.", "영상만으로 상황을 판단하는 것", "映像だけで状況を判断すること")],
            [L("The output must follow a fixed schema.", "출력이 고정된 schema를 따르게 함", "出力を固定のschemaに従わせる"),
             L("Free text cannot be used to choose a response.", "자유 형식 문장으로는 대응 동작을 고를 수 없음", "自由形式の文章では対応動作を選べない"),
             L("Output that cannot be parsed.", "해석할 수 없는 출력", "解析できない出力")],
            [L("Rule-based checks stand between the VLM and the action.", "VLM과 동작 사이에 규칙 검사를 둠", "VLMと動作の間にルールによる検査を置く"),
             L("The model can be wrong.", "모델은 틀릴 수 있음", "モデルは誤ることがある"),
             L("A wrong result becoming a robot action.", "틀린 결과가 로봇 동작이 되는 것", "誤った結果がロボットの動作になること")],
            [L("It runs as a read-only sidecar next to the running system.", "운영 중인 시스템 옆에 읽기 전용 사이드카로 붙임", "運用中のシステムの横に、読み取り専用のサイドカーとして追加する"),
             L("The store was already in operation.", "매장이 이미 운영 중이었음", "店舗がすでに運用中だった"),
             L("Changing the ROS 2 interfaces of the running system.", "운영 중인 ROS 2 인터페이스를 바꾸는 것", "運用中のROS 2インターフェースを変更すること")],
            [L("The VLM only recognizes. It does not choose or control the robot's motion.", "VLM은 인식만 함. 로봇의 동작을 고르거나 제어하지 않음", "VLMは認識のみ。ロボットの動作を選んだり制御したりしない"),
             L("The response to each kind of situation is defined outside the model.", "상황 종류별 대응은 모델 밖에서 정해 둠", "状況の種類ごとの対応は、モデルの外で決めてある"),
             L("The model's output directly moving the robot.", "모델의 출력이 로봇을 직접 움직이는 것", "モデルの出力がロボットを直接動かすこと")],
        ], {}),

        ("h2", "case"),
        ("scenario", {
            "title": L("A cup falls over in the store", "매장에서 컵이 쓰러짐", "店舗でカップが倒れる"),
            "status": ["op_direct"],
            "request": None,
            "strip": [],
            "rows": [
                (L("Observation", "관측", "観測"), L("Camera images and robot and equipment state are bundled. This happens every 2 seconds.", "camera image와 로봇·장비 상태를 묶음. 2초마다 반복", "camera imageとロボット・機器の状態をまとめる。2秒ごとに繰り返す")),
                (L("Classification", "분류", "分類"), L("The VLM returns the kind of situation in the fixed schema.", "VLM이 상황의 종류를 고정된 schema로 반환", "VLMが状況の種類を固定のschemaで返す")),
                (L("Check", "검사", "検査"), L("Rule-based checks confirm that the inputs were fresh and that the result is consistent with the rules.", "입력이 최신이었는지, 결과가 규칙과 맞는지를 규칙 검사가 확인", "入力が最新だったか、結果がルールと合っているかを、ルールによる検査が確認")),
                (L("Response", "대응", "対応"), L("Nothing spilled: the robot picks up the cup and disposes of it. The drink spilled: the manager is called.", "음료가 흐르지 않았으면 로봇이 컵을 집어 폐기. 흘렀으면 관리자 호출", "こぼれていなければ、ロボットがカップを把持して廃棄。こぼれていれば管理者を呼ぶ")),
            ],
            "note": L(
                "Today a predefined flow carries out the response. Letting the Task Planning Agent decide the order of responses (dispose, remake, clean) is in real-robot testing.",
                "지금은 정해 둔 flow가 대응을 실행합니다. Task Planning Agent가 대응 순서(폐기, 재제조, 청소)를 판단하는 방식은 실로봇 테스트 단계입니다.",
                "現在は、あらかじめ決めたflowが対応を実行します。Task Planning Agentが対応の順序（廃棄、再製造、清掃）を判断する方式は、実機テスト段階です。"),
        }),

        ("h2", "scope"),
        ("table", T_SCOPE, [
            [SC_STATUS, ("st", ["op_direct"])],
            [SC_MINE, L("All of it: the input bundle, fine-tuning, the output format and rule checks, the recovery flow, and integration into the running system.",
                        "전부. 입력 묶음, fine-tuning, 출력 형식과 규칙 검사, 복구 flow, 운영 중인 시스템과의 연결.",
                        "すべて。入力セット、fine-tuning、出力形式とルールによる検査、復旧flow、運用中のシステムとの接続。")],
            [SC_EXISTING, L("The base VLM is a public model. I fine-tuned it and did not design its architecture.",
                            "기반 VLM은 공개된 모델입니다. fine-tuning을 했고 구조를 직접 설계하지는 않았습니다.",
                            "ベースのVLMは公開されているモデルです。fine-tuningを行い、構造は自分で設計していません。")],
        ], {"first_bold": True}),

        ("h2", "links"),
        ("links", [
            ("perception-runtime", L("The camera images come from the same cameras that watch the shelf and the cups.",
                                     "camera image는 선반과 컵을 판단하는 같은 camera에서 옵니다.",
                                     "camera imageは、棚とカップを判断するのと同じcameraから得ます。")),
            ("deployment", L("The VLM is retrained and deployed through the MLOps pipeline.",
                             "VLM은 MLOps pipeline으로 다시 학습하고 배포합니다.",
                             "VLMはMLOps pipelineで再学習し、デプロイします。")),
            ("agent-system", L("The Orchestrator Agent dispatches the cleaning robot on contamination. The agent's decision on response order is in real-robot testing.",
                               "오염을 감지하면 Orchestrator Agent가 청소 로봇을 보냅니다. agent의 대응 순서 판단은 실로봇 테스트 단계입니다.",
                               "汚れを検知すると、Orchestrator Agentが清掃ロボットを向かわせます。agentによる対応順序の判断は実機テスト段階です。")),
        ]),
    ],
}
