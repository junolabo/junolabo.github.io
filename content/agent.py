# Project 2: Heterogeneous Multi-Robot Agent System.
from .common import L, T_DECISION, T_SCOPE, SC_STATUS, SC_MINE, SC_SHARED, SC_TEAM, SC_OUT

TPA_BEV = L("Task Planning Agent (beverage-making robot)", "Task Planning Agent (음료 제조 로봇)", "Task Planning Agent（ドリンク製造ロボット）")
TPA_SEMI = L("Task Planning Agent (semi-humanoid robot)", "Task Planning Agent (세미 휴머노이드 로봇)", "Task Planning Agent（セミヒューマノイドロボット）")
SC_HEAD = [L("Step", "단계", "段階"), L("What happens", "일어나는 일", "起きること")]

PAGE = {
    "slug": "agent-system",
    "project": 2,
    "title": "Heterogeneous Multi-Robot Agent System",
    "claim": L(
        "The LLM plans and code validates. Each robot has its own agent, and an Orchestrator ties four robot types together.",
        "LLM이 계획하고 code가 검증합니다. 로봇마다 agent를 두고, Orchestrator가 로봇 4종을 묶습니다.",
        "LLMが計画し、codeが検証します。ロボットごとにagentを置き、Orchestratorが4種のロボットをまとめます。",
    ),
    "facts": [
        ("role", "Project Lead"),
        ("period", L("2025.10 – present", "2025.10 - 현재", "2025.10 - 現在")),
        ("scale", L("4 robot types · 3 agents", "로봇 4종 · agent 3개", "ロボット4種 · agent 3つ")),
        ("status", ("st", ["op_inhouse", "test"])),
    ],
    "blocks": [
        ("h2", "problem"),
        ("p", L(
            "The beverage-making robot followed a fixed making sequence. A fixed sequence could not handle a request that was not on the menu or a problem that came up during execution, so a person stepped in each time. The goal was to respond as flexibly as a staffed store and to take on delivery and cleaning inside the company building.",
            "음료 제조 로봇은 고정된 제조 순서를 따랐습니다. 고정된 순서로는 메뉴에 없는 요청이나 실행 중에 생긴 문제를 처리할 수 없어, 그때마다 사람이 개입했습니다. 목표는 유인 매장처럼 유연하게 응대하고, 회사 건물 안의 배송과 청소까지 맡기는 것이었습니다.",
            "ドリンク製造ロボットは固定された製造手順に従っていました。固定された手順では、メニューにない要望や実行中に起きた問題を処理できず、そのたびに人が介入していました。目標は、有人店舗のように柔軟に対応し、社屋内の配送と清掃まで任せることでした。")),
        ("points", [
            (L("Situations combine, and rules cannot list the combinations.", "상황은 조합되고, 규칙으로는 그 조합을 다 쓸 수 없습니다.", "状況は組み合わさり、ルールではその組み合わせを書ききれません。"),
             L("An LLM can judge a situation that was not specified in advance. That is the reason an LLM does the planning.",
               "LLM은 미리 정해지지 않은 상황을 판단할 수 있습니다. LLM이 계획을 맡는 이유입니다.",
               "LLMは、あらかじめ決められていない状況を判断できます。LLMが計画を担当する理由です。")),
            (L("A plan from an LLM can be wrong and still look right.", "LLM의 plan은 틀려도 그럴듯해 보입니다.", "LLMのplanは、誤っていてももっともらしく見えます。"),
             L("It can use a skill the robot does not have, put steps in the wrong order, ask for something the current state does not allow, or add work that nobody requested.",
               "그 로봇에 없는 skill을 쓰거나, 순서를 틀리거나, 지금 상태로는 할 수 없는 일을 시키거나, 요청하지 않은 작업을 넣을 수 있습니다.",
               "そのロボットにないskillを使う、順序を誤る、現在の状態ではできないことを指示する、依頼されていない作業を加える、といったことが起こり得ます。")),
            (L("A robot's success response is not the result.", "로봇의 성공 응답이 곧 결과는 아닙니다.", "ロボットの成功応答が、そのまま結果とは限りません。"),
             L("A robot can report that a motion finished even when the intended result did not happen.",
               "로봇이 동작을 끝냈다고 응답해도, 의도한 결과가 실제로 일어나지 않았을 수 있습니다.",
               "ロボットが動作の完了を応答しても、意図した結果が実際には起きていないことがあります。")),
            (L("The robots are different.", "로봇들이 서로 다릅니다.", "ロボットがそれぞれ異なります。"),
             L("A rail-mounted manipulator, a semi-humanoid with two arms, a delivery robot, and a cleaning robot have different skills and different limits.",
               "레일형 매니퓰레이터, 양팔 세미 휴머노이드, 배송 로봇, 청소 로봇은 skill과 제약이 서로 다릅니다.",
               "レール型マニピュレータ、双腕のセミヒューマノイド、配送ロボット、清掃ロボットは、skillと制約がそれぞれ異なります。")),
        ]),

        ("h2", "structure"),
        ("tree", {
            "caption": L("Agents and robots", "Agent와 로봇", "Agentとロボット"),
            "top": ("Orchestrator Agent", L("splits a natural-language request into tasks and distributes them", "자연어 요청을 작업으로 나눠 배분", "自然言語の依頼を作業に分けて配分")),
            "link": "MCP tool",
            "children": [
                ("Task Planning Agent", L("beverage-making robot", "음료 제조 로봇", "ドリンク製造ロボット")),
                ("Task Planning Agent", L("semi-humanoid robot", "세미 휴머노이드 로봇", "セミヒューマノイドロボット")),
                (L("Delivery robot · Cleaning robot", "배송 로봇 · 청소 로봇", "配送ロボット · 清掃ロボット"), L("robot API wrapped as an MCP tool", "MCP tool로 감싼 로봇 API", "MCP toolで包んだロボットAPI")),
                ("Perception", L("depth, detection, tracking, VLM", "depth, detection, tracking, VLM", "depth、detection、tracking、VLM")),
            ],
            "note": L(
                "To the Orchestrator Agent, another agent is also a tool. The delivery and cleaning robots have no agent of their own.",
                "Orchestrator Agent 입장에서는 다른 agent도 하나의 도구입니다. 배송 로봇과 청소 로봇에는 따로 agent가 없습니다.",
                "Orchestrator Agentから見ると、ほかのagentもひとつのツールです。配送ロボットと清掃ロボットには専用のagentがありません。"),
        }),
        ("flow", L("Inside every agent: one turn of a plan", "모든 agent의 내부: plan의 한 바퀴", "すべてのagentの内部：planの1サイクル"), [
            (L("Request", "요청", "依頼"), L("natural language", "자연어", "自然言語"), None),
            ("Context Manager", L("current state → LLM input", "현재 상태 → LLM 입력", "現在の状態 → LLMの入力"), None),
            ("Task Planner (LLM)", L("composes skills into a plan", "skill을 조합해 plan 작성", "skillを組み合わせてplanを作成"), None),
            ("Plan Validator", L("runs the plan in advance on the world state", "world state 위에서 plan을 미리 실행", "world state上でplanを事前に実行"), "judge"),
            ("Executor", L("skill, manipulation policy", "skill, manipulation policy", "skill、manipulation policy"), None),
            ("Observation", L("confirms the result, updates the state", "결과를 확인하고 상태를 갱신", "結果を確認し、状態を更新"), "judge"),
        ], L(
            "Validation fails: the plan returns to the Task Planner with the reason. Execution fails: the remaining plan is rebuilt. The LLM is used only in the planner.",
            "검증 실패: 이유를 붙여 Task Planner로 되돌립니다. 실행 실패: 남은 계획을 다시 만듭니다. LLM은 planner에서만 씁니다.",
            "検証の失敗：理由を付けてTask Plannerに戻します。実行の失敗：残りの計画を作り直します。LLMはplannerでのみ使います。")),

        ("h2", "how"),
        ("h3", "Orchestrator Agent", ["op_inhouse", "test"]),
        ("p", L(
            "It splits a natural-language request into tasks and distributes them to the agents and robots connected as MCP tools. For “two Americanos to the meeting room”, making and loading go to the beverage-making agent, and the delivery robot is instructed in order: move, ride the elevator, hand over. When the VLM detects contamination, the cleaning robot is dispatched. Distribution to the semi-humanoid agent is in real-robot testing.",
            "자연어 요청을 작업으로 나눠, MCP tool로 연결한 agent와 로봇에 배분합니다. “아메리카노 2잔을 회의실로” 요청이면 제조와 적재는 음료 제조 agent에 맡기고, 배송 로봇에는 이동, 엘리베이터 탑승, 전달을 순서대로 지시합니다. VLM이 오염을 감지하면 청소 로봇을 보냅니다. 세미 휴머노이드 agent로의 배분은 실로봇 테스트 단계입니다.",
            "自然言語の依頼を作業に分け、MCP toolとして接続したagentとロボットに配分します。「アメリカーノ2杯を会議室へ」という依頼であれば、製造と積み込みはドリンク製造agentに任せ、配送ロボットには移動、エレベーター乗車、受け渡しを順に指示します。VLMが汚れを検知すると清掃ロボットを向かわせます。セミヒューマノイドagentへの配分は実機テスト段階です。")),

        ("h3", TPA_BEV, ["op_inhouse", "test"]),
        ("p", L(
            "The LLM composes skills (cup, ice, and beverage dispensing, arm motion, loading) into a making sequence. The sequence is not fixed. Rules are given as constraints, not as a sequence: an iced drink needs cup, then ice, then beverage, and the planner decides the rest within that.",
            "컵·얼음·음료 추출, 로봇팔 이동, 적재 skill을 LLM이 조합해 제조 순서를 계획합니다. 순서를 고정하지 않습니다. 규칙은 순서가 아니라 제약으로 줍니다. ICE 음료는 컵, 얼음, 음료의 순서여야 하고, 그 안에서 나머지는 planner가 정합니다.",
            "カップ・氷・ドリンクの抽出、ロボットアームの移動、積み込みのskillをLLMが組み合わせて製造手順を計画します。手順は固定しません。ルールは手順ではなく制約として与えます。アイスドリンクはカップ、氷、ドリンクの順である必要があり、その中で残りはplannerが決めます。")),
        ("p", L(
            "The state of dispenser channels (kind, state, stock), the robot, cups, and slots is kept as a graph and updated during execution. When the same channel fails repeatedly, it is marked unavailable and another channel is used. The agent keeps a short-term memory of the current order and a long-term memory of how past incidents were handled.",
            "디스펜서 채널의 종류·상태·재고, 로봇, 컵, 칸의 상태를 graph로 두고 실행 중에 갱신합니다. 같은 채널이 반복해서 실패하면 사용 불가로 표시하고 다른 채널을 씁니다. 현재 주문에 대한 단기 메모리와 과거 대응 사례에 대한 장기 메모리를 둡니다.",
            "ディスペンサーのチャンネルの種類・状態・在庫、ロボット、カップ、区画の状態をgraphとして持ち、実行中に更新します。同じチャンネルが繰り返し失敗した場合は使用不可とし、別のチャンネルを使います。現在の注文に関する短期メモリと、過去の対応事例に関する長期メモリを持ちます。")),
        ("table",
         [L("Status", "상태", "状態"), L("What the agent does", "agent가 하는 일", "agentが行うこと")],
         [
             [("st", ["op_inhouse"]),
              L("Making in-house delivery orders and loading them onto the delivery robot. On failure, the remaining plan is rebuilt.",
                "사내 배송 주문의 제조와 배송 로봇 적재. 실패하면 남은 계획을 다시 만듦",
                "社内配送注文の製造と配送ロボットへの積み込み。失敗した場合は残りの計画を作り直す")],
             [("st", ["test"]),
              L("Requests that are not on the menu (ice water), custom drinks (extra shot), and deciding the order of responses to anomalies detected by the VLM. Not yet offered to store customers.",
                "메뉴에 없는 요청(얼음물), 커스텀 음료(샷 추가), VLM이 감지한 이상 상황의 대응 순서 판단. 매장 고객에게는 아직 제공 전",
                "メニューにない要望（氷水）、カスタムドリンク（ショット追加）、VLMが検知した異常への対応順序の判断。店舗のお客様にはまだ提供していない")],
         ], {}),

        ("h3", TPA_SEMI, ["test"]),
        ("p", L(
            "It plans an order such as “bag two salt breads” as a repetition of find the product by camera → select the target → pick-and-place. Right before each bagging it checks that the target is still in the remaining order, so a product different from the order is not bagged. The task is complete only when what is in the bag matches the order exactly.",
            "“소금빵 2개 담아줘” 같은 주문을 camera로 상품 찾기 → 대상 선택 → pick-and-place의 반복으로 계획합니다. 담기 직전마다 대상이 남은 주문에 있는지 확인해, 주문과 다른 상품을 담지 않습니다. 봉투에 담긴 내용이 주문과 정확히 일치해야 작업이 끝난 것으로 봅니다.",
            "「塩パンを2個入れて」のような注文を、cameraで商品を探す → 対象を選ぶ → pick-and-place の繰り返しとして計画します。袋に入れる直前ごとに対象が残りの注文にあるかを確認し、注文と異なる商品を入れません。袋の中身が注文と正確に一致して初めて、作業の完了とします。")),
        ("p", L(
            "Failure is handled in four levels: a correction by rule, a fix by the LLM, replanning, and a request to a person. A failed grasp is retried, a dropped item is searched for again, and when stock runs out the remaining order is replanned or a person is called. The connection to the robot is reduced to two contracts, execute and observe, so a mock, a simulator, and the real robot can be swapped.",
            "실패는 네 단계로 복구합니다. 규칙에 의한 보정, LLM의 수정, 재계획, 사람에게 요청의 순서입니다. 잡기에 실패하면 재시도하고, 놓치면 다시 검색하고, 재고가 없으면 남은 주문을 재계획하거나 사람을 호출합니다. 로봇과의 연결은 execute와 observe 두 가지 계약으로 줄여, mock, simulator, 실로봇을 바꿔 끼울 수 있습니다.",
            "失敗は4段階で復旧します。ルールによる補正、LLMによる修正、再計画、人への依頼の順です。把持に失敗すれば再試行し、落とせば再検索し、在庫がなければ残りの注文を再計画するか人を呼びます。ロボットとの接続はexecuteとobserveの2つの契約に絞り、mock、simulator、実機を差し替えられます。")),

        ("h3", "Context Manager", ["op_inhouse"]),
        ("p", L(
            "It keeps the current state, such as robot position, held object, and equipment stock, as world state and a scene graph, and builds the LLM input from only the part that a request needs. The state is not overwritten. Observations are accumulated with their time and source, and the current state is computed from them, so an old observation is not mistaken for the present. Completion is confirmed by observation, not by the robot's success response.",
            "로봇 위치, 들고 있는 물체, 장비 재고 같은 현재 상태를 world state와 scene graph로 유지하고, 요청에 필요한 부분만 LLM 입력으로 구성합니다. 상태를 덮어쓰지 않습니다. 관측을 시간, 출처와 함께 쌓고 거기서 현재 상태를 계산하므로, 오래된 관측을 현재로 착각하지 않습니다. 완료는 로봇의 성공 응답이 아니라 observation으로 확인합니다.",
            "ロボットの位置、持っている物体、機器の在庫などの現在の状態をworld stateとscene graphとして保持し、依頼に必要な部分だけをLLMの入力として構成します。状態は上書きしません。観測を時刻と出所とともに蓄積し、そこから現在の状態を計算するため、古い観測を現在と取り違えません。完了は、ロボットの成功応答ではなくobservationで確認します。")),

        ("h3", "Plan Validator", ["op_inhouse"]),
        ("p", L(
            "Before a plan made by the LLM is sent to the robot, it is executed step by step in advance on the current world state. The planner itself works in two steps: it first writes the plan in natural language and then converts it into a structured form while keeping the meaning. The validator checks the structured plan.",
            "LLM이 만든 plan을 로봇에 보내기 전에 현재 world state 위에서 한 단계씩 미리 실행합니다. planner는 두 단계로 동작합니다. 먼저 자연어로 계획을 쓰고, 그 뜻을 유지한 채 구조화된 형태로 바꿉니다. validator는 구조화된 plan을 검사합니다.",
            "LLMが作ったplanをロボットに送る前に、現在のworld state上で1ステップずつ事前に実行します。plannerは2段階で動きます。まず自然言語で計画を書き、その意味を保ったまま構造化された形に変換します。validatorは構造化されたplanを検査します。")),
        ("table",
         [L("What is checked", "검사하는 것", "検査すること"), L("Example of a plan that is stopped", "막히는 plan의 예", "止められるplanの例")],
         [
             [L("Is each step a skill of that robot?", "각 단계가 그 로봇의 skill인가", "各ステップがそのロボットのskillか"),
              L("A step that uses a skill the robot does not have", "그 로봇에 없는 skill을 쓰는 단계", "そのロボットにないskillを使うステップ")],
             [L("Is the order right?", "순서가 맞는가", "順序が正しいか"),
              L("Delivery before making is finished", "제조가 끝나기 전의 배송", "製造が終わる前の配送")],
             [L("Is it feasible given position, load capacity, and equipment state?", "위치·적재 용량·장비 상태로 수행 가능한가", "位置・積載容量・機器の状態から実行可能か"),
              L("More drinks than the load limit", "적재 한도를 넘는 음료 수", "積載上限を超えるドリンク数")],
             [L("Was it requested?", "요청한 작업인가", "依頼された作業か"),
              L("Work that hallucination added and the request did not ask for", "hallucination으로 들어간, 요청하지 않은 작업", "hallucinationによって加わった、依頼されていない作業")],
         ], {}),
        ("p", L(
            "The result is one of four: valid, conditional, violation, or undecidable. A plan that does not pass returns to the planner with the reason. If the world state changes after validation, the plan is not sent as it is. It is validated again.",
            "결과는 valid, conditional, violation, undecidable의 네 가지 중 하나입니다. 통과하지 못한 plan은 이유를 붙여 planner로 되돌립니다. 검증한 뒤에 world state가 바뀌면 plan을 그대로 보내지 않고 다시 검증합니다.",
            "結果は、valid、conditional、violation、undecidableの4つのいずれかです。通過しなかったplanは、理由を付けてplannerに戻します。検証の後にworld stateが変わった場合は、planをそのまま送らず、もう一度検証します。")),

        ("h3", "Planning evaluation", ["sim"]),
        ("p", L(
            "For each request, required conditions are defined (for example, delivery only after making is finished, and the load limit respected). The plan and the execution result are scored separately. Evaluation runs through the same code path as real operation, and the answer conditions are not given to the planner. A case that is blocked at the generation step stays in the denominator. This part was co-developed with a teammate.",
            "요청마다 필수 조건(예: 제조가 끝난 뒤 배송, 적재 한도 준수)을 정합니다. plan과 실행 결과를 따로 채점합니다. 평가도 실제 운영과 같은 code 경로로 실행하고, 정답 조건은 planner에 주지 않습니다. 생성 단계에서 막힌 사례도 분모에서 빼지 않습니다. 이 부분은 팀원과 공동으로 개발했습니다.",
            "依頼ごとに必須条件（例：製造が終わってから配送、積載上限の順守）を定めます。planと実行結果を別々に採点します。評価も実際の運用と同じcode経路で実行し、正解条件はplannerに与えません。生成の段階で止まった事例も分母から外しません。この部分はチームメンバーと共同で開発しました。")),

        ("h3", L("Where rules stop", "규칙이 끝나는 지점", "ルールが及ばなくなる地点"), None),
        ("table",
         [L("Class", "분류", "分類"), L("Situations", "상황", "状況"), L("Example", "예", "例")],
         [
             [L("1. Normal operation", "1. 일반 운영", "1. 通常運用"),
              L("A menu item, something not on the menu, something that may be given for free", "있는 메뉴, 없는 메뉴, 무료로 줄 수 있는 것", "メニューにあるもの、ないもの、無料で提供できるもの"),
              L("Ice water", "얼음물", "氷水")],
             [L("2. A single anomaly", "2. 이상 상황 단독", "2. 単独の異常"),
              L("Failed grip, failed dispensing, a spill while serving, a person approaching, a drink left on the shelf", "컵 그립 실패, 음료 추출 실패, 서빙 중 쏟아짐, 사람 접근, 방치 음료", "把持の失敗、抽出の失敗、提供中のこぼれ、人の接近、放置されたドリンク"),
              L("Failed grip → the cup is dispensed again", "그립 실패 → 컵을 다시 추출", "把持の失敗 → カップを再度抽出")],
             [L("3. Composite situations", "3. 복합 상황", "3. 複合的な状況"),
              L("Custom drinks, priority between handling an incident and continuing operation, several problems at once", "커스텀 메뉴, 사고 처리와 운영 사이의 우선순위, 여러 문제의 동시 발생", "カスタムメニュー、事故対応と運用の優先順位、複数の問題の同時発生"),
              L("After a spill: remake first or clean first? It depends on how many slots are free and whether orders are waiting.", "쏟아진 뒤 재제조가 먼저인가 청소가 먼저인가. 빈 칸의 수와 대기 주문의 유무에 따라 달라짐", "こぼれた後、再製造が先か清掃が先か。空いている区画の数と待ち注文の有無によって変わる")],
         ], {"first_bold": True}),
        ("p", L(
            "Classes 1 and 2 can be written as rules. Class 3 is the reason the agent exists: as the combinations grow, they can no longer be written as rules.",
            "1번과 2번은 규칙으로 쓸 수 있습니다. 3번이 agent가 있는 이유입니다. 조합이 늘면 규칙으로 쓸 수 없습니다.",
            "1と2はルールとして書けます。3がagentの存在理由です。組み合わせが増えると、ルールでは書けなくなります。")),

        ("h2", "decisions"),
        ("table", T_DECISION, [
            [L("The LLM only plans. Code validates and executes.", "LLM은 계획만 함. 검증과 실행은 code가 함", "LLMは計画のみ。検証と実行はcodeが行う"),
             L("An LLM can judge unspecified situations, and it can also be wrong.", "LLM은 정해지지 않은 상황을 판단할 수 있고, 틀릴 수도 있음", "LLMは決められていない状況を判断できるが、誤ることもある"),
             L("A wrong plan reaching the robot.", "틀린 plan이 로봇에 도달하는 것", "誤ったplanがロボットに届くこと")],
            [L("A plan is run in advance on the world state before it is sent.", "plan을 보내기 전에 world state 위에서 미리 실행", "planを送る前に、world state上で事前に実行する"),
             L("Feasibility depends on the current state, not on the text of the plan.", "수행 가능 여부는 plan의 글이 아니라 현재 상태에 달려 있음", "実行可能かどうかは、planの文面ではなく現在の状態で決まる"),
             L("A plan that reads well and cannot be carried out.", "글로는 맞지만 수행할 수 없는 plan", "文面は正しいが実行できないplan")],
            [L("Completion is confirmed by observation.", "완료를 observation으로 확인", "完了をobservationで確認する"),
             L("A success response describes the motion, not the outcome.", "성공 응답은 동작에 대한 것이고 결과에 대한 것이 아님", "成功応答は動作についてのものであり、結果についてのものではない"),
             L("Continuing a plan on a step that did not actually succeed.", "실제로는 성공하지 않은 단계 위에서 plan을 이어 가는 것", "実際には成功していないステップの上で、planを続けること")],
            [L("Rules are given as constraints, not as a fixed sequence.", "규칙을 고정된 순서가 아니라 제약으로 줌", "ルールを固定の手順ではなく制約として与える"),
             L("A fixed sequence cannot cover requests outside the menu.", "고정된 순서로는 메뉴 밖의 요청을 다룰 수 없음", "固定の手順では、メニュー外の要望を扱えない"),
             L("Rewriting the sequence for every new request.", "새 요청마다 순서를 다시 쓰는 것", "新しい要望のたびに手順を書き直すこと")],
            [L("Every robot is reached as a tool, with or without its own agent.", "agent가 있든 없든 모든 로봇을 tool로 연결", "agentの有無にかかわらず、すべてのロボットをtoolとして接続する"),
             L("The robots differ in skills and limits.", "로봇마다 skill과 제약이 다름", "ロボットごとにskillと制約が異なる"),
             L("A separate integration method for each robot.", "로봇마다 다른 연결 방식", "ロボットごとに別々の接続方式")],
        ], {}),

        ("h2", "case"),
        ("scenario", {
            "title": L("Beverage delivery inside the building", "건물 안 음료 배달", "社屋内のドリンク配送"),
            "status": ["op_inhouse"],
            "request": L("“Two Americanos to the meeting room.”", "“아메리카노 2잔을 회의실로.”", "「アメリカーノ2杯を会議室へ」"),
            "strip": [
                (L("Request", "요청", "依頼"), None, None),
                ("Orchestrator Agent", L("splits into tasks", "작업으로 나눔", "作業に分ける"), None),
                (L("Beverage-making agent", "음료 제조 agent", "ドリンク製造agent"), L("plan, validate, make, load", "계획, 검증, 제조, 적재", "計画、検証、製造、積み込み"), "judge"),
                (L("Delivery robot", "배송 로봇", "配送ロボット"), L("move, elevator, hand over", "이동, 엘리베이터, 전달", "移動、エレベーター、受け渡し"), None),
            ],
            "head": SC_HEAD,
            "rows": [
                ("Orchestrator Agent", L("Splits the request into making, loading, and delivery.", "요청을 제조, 적재, 배송으로 나눔", "依頼を製造、積み込み、配送に分ける")),
                (TPA_BEV, L("Plans the making sequence for two drinks. The Plan Validator runs the plan on the world state, including the load limit of the delivery robot.", "두 잔의 제조 순서를 계획. Plan Validator가 배송 로봇의 적재 한도를 포함해 world state 위에서 plan을 미리 실행", "2杯の製造手順を計画。Plan Validatorが、配送ロボットの積載上限を含めて、world state上でplanを事前に実行")),
                (L("Execution and observation", "실행과 observation", "実行とobservation"), L("The robot makes the drinks and loads them onto the delivery robot. Each step is confirmed by observation.", "로봇이 음료를 만들어 배송 로봇에 적재. 단계마다 observation으로 확인", "ロボットがドリンクを作り、配送ロボットに積み込む。ステップごとにobservationで確認")),
                (L("Orchestrator Agent → delivery robot", "Orchestrator Agent → 배송 로봇", "Orchestrator Agent → 配送ロボット"), L("Instructs the delivery robot in order: move, ride the elevator, hand over.", "배송 로봇에 이동, 엘리베이터 탑승, 전달을 순서대로 지시", "配送ロボットに移動、エレベーター乗車、受け渡しを順に指示")),
            ],
            "note": None,
        }),
        ("scenario", {
            "title": L("A step fails during making", "제조 중에 한 단계가 실패", "製造中に1つのステップが失敗"),
            "status": ["op_inhouse"],
            "request": L("A cup is dispensed, and the gripper camera shows that the cup is not held.", "컵을 추출했는데, gripper camera에서 컵이 잡히지 않은 것으로 보임", "カップを抽出したが、gripper cameraではカップが把持されていない"),
            "strip": [
                (L("Cup dispensing", "컵 추출", "カップの抽出"), None, None),
                (L("Grip check fails", "그립 확인 실패", "把持確認の失敗"), None, "fail"),
                (L("Replanning", "재계획", "再計画"), L("from cup dispensing", "컵 추출부터", "カップの抽出から"), "judge"),
                (L("Cup dispensed again", "컵 재추출", "カップを再度抽出"), None, None),
                (L("Making continues", "제조 계속", "製造を続行"), None, None),
            ],
            "head": SC_HEAD,
            "rows": [
                (L("Failure", "실패", "失敗"), L("The observation after the skill shows that the cup is not held, although the skill itself was executed.", "skill은 실행됐지만, 그 뒤의 observation에서 컵이 잡히지 않은 것으로 확인됨", "skill自体は実行されたが、その後のobservationでカップが把持されていないと確認される")),
                (L("Replanning", "재계획", "再計画"), L("The Task Planner rebuilds the remaining plan, starting again from cup dispensing.", "Task Planner가 컵 추출부터 남은 계획을 다시 만듦", "Task Plannerが、カップの抽出から残りの計画を作り直す")),
                (L("Repeated failure", "반복 실패", "繰り返しの失敗"), L("When the same channel keeps failing, it is marked unavailable and another channel is used.", "같은 채널이 계속 실패하면 사용 불가로 표시하고 다른 채널을 사용", "同じチャンネルが失敗し続ける場合は使用不可とし、別のチャンネルを使う")),
            ],
            "note": None,
        }),
        ("scenario", {
            "title": L("A request that is not on the menu", "메뉴에 없는 요청", "メニューにない要望"),
            "status": ["test"],
            "request": L("One request is for ice water. Another is for a drink with an extra shot.", "한 요청은 얼음물이고, 다른 요청은 샷을 추가한 음료임", "ある依頼は氷水、別の依頼はショットを追加したドリンク"),
            "strip": [
                (L("Request", "요청", "依頼"), None, None),
                (L("Judgment", "판단", "判断"), L("may this be provided?", "제공해도 되는가", "提供してよいか"), "judge"),
                ("Task Planner (LLM)", L("composes existing skills", "기존 skill을 조합", "既存のskillを組み合わせる"), None),
                ("Plan Validator", None, "judge"),
                (L("Making", "제조", "製造"), None, None),
            ],
            "head": SC_HEAD,
            "rows": [
                (L("Judgment", "판단", "判断"), L("Ice water is not a menu item, and it may be given. A free drink may not.", "얼음물은 판매 메뉴가 아니지만 제공할 수 있음. 무료 음료는 제공하지 않음", "氷水は販売メニューではないが提供できる。無料のドリンクは提供しない")),
                (L("Planning", "계획", "計画"), L("A fixed making sequence does not cover these requests. The planner composes the existing skills within the constraints.", "고정된 제조 순서로는 이 요청을 다룰 수 없음. planner가 제약 안에서 기존 skill을 조합", "固定の製造手順ではこれらの要望を扱えない。plannerが制約の中で既存のskillを組み合わせる")),
                (L("Validation and execution", "검증과 실행", "検証と実行"), L("The plan passes the same validation as any other plan before it is executed.", "다른 plan과 같은 검증을 통과한 뒤 실행", "ほかのplanと同じ検証を通過してから実行")),
            ],
            "note": None,
        }),
        ("scenario", {
            "title": L("Bagging bread with two arms", "양팔로 빵 담기", "両腕でのパンの袋詰め"),
            "status": ["test"],
            "request": L("“Bag two salt breads.”", "“소금빵 2개 담아줘.”", "「塩パンを2個入れて」"),
            "strip": [
                (L("Order", "주문", "注文"), None, None),
                (L("Find and select", "찾기와 선택", "探索と選択"), L("camera", "camera", "camera"), None),
                (L("Check", "확인", "確認"), L("still in the remaining order?", "남은 주문에 있는가", "残りの注文にあるか"), "judge"),
                (L("Policy · VLA", "Policy · VLA", "Policy · VLA"), L("pick with both arms, bag", "양팔로 집어 담기", "両腕で把持して袋に入れる"), None),
                (L("Repeat", "반복", "繰り返し"), L("until the bag matches the order", "봉투가 주문과 일치할 때까지", "袋の中身が注文と一致するまで"), None),
            ],
            "head": SC_HEAD,
            "rows": [
                (TPA_SEMI, L("Plans the order as a repetition of find the product by camera → select the target → pick-and-place.", "주문을 camera로 상품 찾기 → 대상 선택 → pick-and-place의 반복으로 계획", "注文を、cameraで商品を探す → 対象を選ぶ → pick-and-place の繰り返しとして計画")),
                ("Manipulation policy · VLA", L("Called with an instruction text and an image in which everything except the target is masked.", "대상 외 영역을 가린 image와 지시문으로 호출", "対象以外の領域を隠したimageと指示文で呼び出す")),
                (L("On failure", "실패하면", "失敗した場合"), L("Failed grasp: retry. Dropped: search again. Out of stock: replan the remaining order or call a person.", "잡기 실패: 재시도. 놓침: 다시 검색. 재고 없음: 남은 주문을 재계획하거나 사람을 호출", "把持の失敗：再試行。落下：再検索。在庫なし：残りの注文を再計画するか人を呼ぶ")),
            ],
            "note": None,
        }),

        ("h2", "scope"),
        ("table", T_SCOPE, [
            [SC_STATUS, L("In operation (in-house): delivery and cleaning through the Orchestrator Agent, making and loading of in-house delivery orders, Context Manager, Plan Validator. Real-robot testing: off-menu requests, custom drinks, response to anomalies, the semi-humanoid agent. Simulation: planning evaluation.",
                          "운영 (사내): Orchestrator Agent를 통한 배송과 청소, 사내 배송 주문의 제조와 적재, Context Manager, Plan Validator. 실로봇 테스트: 메뉴에 없는 요청, 커스텀 음료, 이상 상황 대응, 세미 휴머노이드 agent. 시뮬레이션: planning evaluation.",
                          "運用中（社内）：Orchestrator Agentを通じた配送と清掃、社内配送注文の製造と積み込み、Context Manager、Plan Validator。実機テスト：メニューにない要望、カスタムドリンク、異常への対応、セミヒューマノイドagent。シミュレーション：planning evaluation。")],
            [SC_MINE, L("System design. The task planning algorithm, the Plan Validator, and the Context Manager structure of all three agents: design and development.",
                        "시스템 설계. agent 3개 모두의 task planning 알고리즘, Plan Validator, Context Manager 구조의 설계와 개발.",
                        "システム設計。3つのagentすべてのtask planningアルゴリズム、Plan Validator、Context Managerの構造の設計と開発。")],
            [SC_SHARED, L("Connecting agents and robots through MCP, executing plans as robot motion (Executor, robot integration), and planning evaluation.",
                          "MCP로 agent와 로봇을 연결하는 부분, plan을 로봇 동작으로 실행하는 부분(Executor, 로봇 연동), planning evaluation.",
                          "MCPによるagentとロボットの接続、planをロボットの動作として実行する部分（Executor、ロボット連携）、planning evaluation。")],
            [SC_TEAM, L("Specifications such as the definition of robot skills.",
                        "로봇 skill 정의 등의 명세.",
                        "ロボットのskill定義などの仕様。")],
            [SC_OUT, L("The navigation system of the delivery and cleaning robots. Here they are only targets of commands.",
                       "배송 로봇과 청소 로봇의 주행 시스템. 여기서는 명령의 대상일 뿐입니다.",
                       "配送ロボットと清掃ロボットの走行システム。ここでは指示の対象にとどまります。")],
        ], {"first_bold": True}),

        ("h2", "links"),
        ("links", [
            ("anomaly-detection", L("The VLM's result is the trigger for dispatching the cleaning robot and, in testing, for the agent's judgment of response order.",
                                    "VLM의 결과가 청소 로봇을 보내는 계기가 되고, 테스트 단계에서는 agent가 대응 순서를 판단하는 계기가 됩니다.",
                                    "VLMの結果が、清掃ロボットを向かわせるきっかけとなり、テスト段階ではagentが対応順序を判断するきっかけになります。")),
            ("manipulation-learning", L("The manipulation policy and the VLA that the semi-humanoid agent calls.",
                                        "세미 휴머노이드 agent가 호출하는 manipulation policy와 VLA.",
                                        "セミヒューマノイドagentが呼び出すmanipulation policyとVLA。")),
            ("perception-runtime", L("Perception is connected to the Orchestrator Agent as a tool.",
                                     "Perception은 Orchestrator Agent에 tool로 연결됩니다.",
                                     "PerceptionはOrchestrator Agentにtoolとして接続されています。")),
        ]),
    ],
}
