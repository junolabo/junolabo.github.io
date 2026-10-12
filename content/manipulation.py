# Project 3: Teleoperation & Manipulation Learning.
from .common import L, T_DECISION, T_SCOPE, SC_STATUS, SC_MINE, SC_TEAM, SC_EXISTING

PAGE = {
    "slug": "manipulation-learning",
    "project": 3,
    "title": "Teleoperation & Manipulation Learning",
    "claim": L(
        "Only the part that a fixed motion cannot do is learned. The work covers the whole path: teleoperation, demonstration data, policy training, real-robot testing, and operation in stores.",
        "정해진 동작으로 할 수 없는 부분만 학습합니다. teleoperation, 데모 데이터, policy 학습, 실로봇 테스트, 매장 운영까지 전 과정을 다뤘습니다.",
        "決まった動作ではできない部分だけを学習します。teleoperation、デモデータ、policyの学習、実機テスト、店舗での運用まで、全過程を扱いました。",
    ),
    "facts": [
        ("role", L("Teleoperation code and policy training", "teleoperation code·policy 학습 담당", "teleoperationのcodeとpolicyの学習を担当")),
        ("period", L("2024.11 – present", "2024.11 - 현재", "2024.11 - 現在")),
        ("status", ("st", ["op", "test"])),
    ],
    "blocks": [
        ("h2", "problem"),
        ("p", L(
            "Most of what the robots do can be written as fixed motions: move to a dispenser, place a cup on a slot. Three tasks could not.",
            "로봇이 하는 일의 대부분은 정해진 동작으로 쓸 수 있습니다. 디스펜서로 이동하기, 컵을 칸에 놓기 같은 일입니다. 세 가지 작업은 그렇게 할 수 없었습니다.",
            "ロボットが行う作業の大部分は、決まった動作として書けます。ディスペンサーへの移動や、カップを区画に置くことなどです。3つの作業はそうできませんでした。")),
        ("points", [
            (L("Clearing trash: the object has no fixed shape.", "쓰레기 치우기: 대상의 모양이 정해져 있지 않습니다.", "ゴミの片付け：対象に決まった形がありません。"),
             L("A cup always has the same shape, so a rule can grasp it. Trash left on the shelf does not.",
               "컵은 모양이 늘 같아서 규칙으로 집을 수 있습니다. 선반에 남은 쓰레기는 그렇지 않습니다.",
               "カップは形が常に同じなので、ルールで把持できます。棚に残されたゴミはそうではありません。")),
            (L("Bagging bread: two arms have to work together.", "빵 담기: 양팔을 함께 써야 합니다.", "パンの袋詰め：両腕を同時に使う必要があります。"),
             L("Picking up packaged bread and putting it into a bag needs both arms at the same time.",
               "포장된 빵을 집어 봉투에 담으려면 양팔이 동시에 움직여야 합니다.",
               "包装されたパンを把持して袋に入れるには、両腕が同時に動く必要があります。")),
            (L("Pouring water for drip coffee: a much more complex motion.", "드립 커피의 물 붓기: 훨씬 더 복잡한 동작입니다.", "ドリップコーヒーの湯注ぎ：はるかに複雑な動作です。"),
             L("Pouring is far more complex than grasping a kettle or placing a filter.",
               "물 붓기는 주전자를 잡거나 필터를 놓는 것보다 훨씬 복잡합니다.",
               "湯注ぎは、ケトルの把持やフィルターの設置よりはるかに複雑です。")),
        ]),
        ("p", L(
            "For these, data of a person directly operating the robot was collected, and the motion was learned from it.",
            "이 작업들은 사람이 로봇을 직접 조작한 데이터를 모아 그 동작을 학습시켰습니다.",
            "これらの作業では、人がロボットを直接操作したデータを集め、その動作を学習させました。")),

        ("h2", "structure"),
        ("flow", L("From a demonstration to a policy in operation", "데모에서 운영 중인 policy까지", "デモから運用中のpolicyまで"), [
            ("Teleoperation", L("leader-follower, single-arm and bimanual", "leader-follower, single-arm과 bimanual", "leader-follower、single-armとbimanual"), None),
            (L("Demonstration collection", "데모 수집", "デモ収集"), L("image, state, action, time-aligned", "image, state, action을 시간 정렬", "image、state、actionを時刻同期"), None),
            ("Episode dataset", "HDF5", None),
            (L("Policy training", "Policy 학습", "Policyの学習"), L("Diffusion Policy family, PPO", "Diffusion Policy 계열, PPO", "Diffusion Policy系、PPO"), None),
            (L("Real-robot testing", "실로봇 테스트", "実機テスト"), None, "judge"),
            (L("Operation", "운영", "運用"), L("called as a skill", "skill로 호출", "skillとして呼び出す"), None),
        ], L(
            "A learned policy sits in the Execution layer next to the fixed skills.",
            "학습한 policy는 Execution 계층에서 정해진 skill과 나란히 있습니다.",
            "学習したpolicyは、Execution階層で決まったskillと並んでいます。")),
        ("table",
         [L("Task", "작업", "作業"), L("Done by fixed motion", "정해진 동작으로 한 부분", "決まった動作で行う部分"),
          L("Learned", "학습한 부분", "学習した部分"), L("Policy input", "Policy의 입력", "Policyの入力"), L("Status", "상태", "状態")],
         [
             [L("Clearing trash from the shelf", "선반 위 쓰레기 치우기", "棚の上のゴミの片付け"),
              L("Approach to the position found by the ceiling camera. Drop at the disposal position.", "천장 camera로 찾은 위치까지의 접근. 폐기 위치에 버리기", "天井cameraで見つけた位置までの接近。廃棄位置に捨てる"),
              L("The grasp", "집는 동작", "把持"),
              L("Live gripper-camera image", "실시간 gripper camera image", "リアルタイムのgripper camera image"),
              ("st", ["op"])],
             [L("Bagging bread", "빵 담기", "パンの袋詰め"),
              L("Finding the product and choosing the target, planned by the Task Planning Agent", "상품 찾기와 대상 선택. Task Planning Agent가 계획", "商品の探索と対象の選択。Task Planning Agentが計画"),
              L("Picking with both arms and bagging", "양팔로 집어 봉투에 담기", "両腕で把持して袋に入れる"),
              L("An image in which everything except the target is masked, and an instruction text", "대상 외 영역을 가린 image와 지시문", "対象以外の領域を隠したimageと指示文"),
              ("st", ["test"])],
             [L("Drip coffee", "드립 커피", "ドリップコーヒー"),
              L("—", "—", "—"),
              L("Grasping the kettle and placing the filter (IL). Pouring water (RL)", "주전자 잡기와 필터 놓기(IL). 물 붓기(RL)", "ケトルの把持とフィルターの設置（IL）。湯注ぎ（RL）"),
              L("—", "—", "—"),
              ("st", ["past"])],
         ], {"first_bold": True}),

        ("h2", "how"),
        ("h3", "Teleoperation", ["ongoing"]),
        ("p", L(
            "I implemented the control code and the demonstration-collection code for single-arm and bimanual leader-follower teleoperation. The leader and the follower have the same 6-DOF joint configuration, so the leader's joint values are mapped to the follower's joint commands (joint mapping) inside a control loop.",
            "single-arm과 bimanual leader-follower teleoperation의 제어 code와 데모 수집 code를 구현했습니다. leader와 follower의 관절 구성이 6-DOF로 같아서, 제어 loop 안에서 leader의 joint 값을 follower의 joint 명령으로 옮깁니다(joint mapping).",
            "single-armとbimanualのleader-follower teleoperationの制御codeとデモ収集codeを実装しました。leaderとfollowerの関節構成が同じ6-DOFのため、制御loopの中でleaderのjoint値をfollowerのjoint指令に写します（joint mapping）。")),
        ("p", L(
            "During a demonstration, camera images, robot state, and actions are recorded and aligned in time, and each demonstration is stored as one episode in HDF5. The dataset is used for policy training.",
            "데모 중에 camera image, 로봇 state, action을 기록하고 시간을 맞춥니다. 데모 하나를 HDF5의 episode 하나로 저장합니다. 이 dataset을 policy 학습에 씁니다.",
            "デモの間、camera image、ロボットのstate、actionを記録し、時刻を合わせます。デモ1件をHDF5のepisode 1件として保存します。このdatasetをpolicyの学習に使います。")),

        ("h3", "Manipulation policy (single-arm)", ["op"]),
        ("p", L(
            "The beverage-making robot clears trash from the pickup shelf. Only the grasp is learned. The arm first approaches the position found by the ceiling camera. From there, a policy that I trained takes the live gripper-camera image and picks the object up. Dropping it at the disposal position is a fixed motion again. In operation at company-run stores.",
            "음료 제조 로봇이 픽업 선반 위의 쓰레기를 치웁니다. 집는 동작만 학습했습니다. 로봇팔은 먼저 천장 camera로 찾은 위치 근처까지 접근합니다. 거기서부터는 직접 학습한 policy가 실시간 gripper camera image를 받아 물체를 집습니다. 폐기 위치에 버리는 동작은 다시 정해진 동작입니다. 직영 매장에서 운영하고 있습니다.",
            "ドリンク製造ロボットがピックアップ棚の上のゴミを片付けます。学習したのは把持だけです。ロボットアームはまず、天井cameraで見つけた位置の近くまで接近します。そこからは、自ら学習したpolicyがリアルタイムのgripper camera imageを受け取り、物体を把持します。廃棄位置に捨てる動作は、再び決まった動作です。直営店舗で運用しています。")),
        ("flow", L("Clearing one piece of trash", "쓰레기 하나 치우기", "ゴミ1つの片付け"), [
            (L("Ceiling camera", "천장 camera", "天井camera"), L("finds the position", "위치를 찾음", "位置を見つける"), None),
            (L("Approach", "접근", "接近"), L("fixed motion, to near that position", "정해진 동작, 그 위치 근처까지", "決まった動作、その位置の近くまで"), None),
            (L("Grasp", "집기", "把持"), L("learned policy, live gripper-camera image", "학습한 policy, 실시간 gripper camera image", "学習したpolicy、リアルタイムのgripper camera image"), "judge"),
            (L("Dispose", "폐기", "廃棄"), L("fixed motion, to the disposal position", "정해진 동작, 폐기 위치로", "決まった動作、廃棄位置へ"), None),
        ], None),

        ("h3", "Manipulation policy (bimanual)", ["test"]),
        ("p", L(
            "The semi-humanoid robot picks up packaged bread with both arms and puts it in a bag. I trained a policy of the Diffusion Policy family. A teammate trained a VLA for the same task. I connected the Task Planning Agent so that it calls this policy and the VLA with an instruction text and an image in which everything except the target is masked.",
            "세미 휴머노이드 로봇이 포장된 빵을 양팔로 집어 봉투에 담습니다. Diffusion Policy 계열 policy를 직접 학습했습니다. 같은 작업에 대해 팀원이 VLA를 학습했습니다. Task Planning Agent가 대상 외 영역을 가린 image와 지시문으로 이 policy와 VLA를 호출하도록 연결했습니다.",
            "セミヒューマノイドロボットが包装されたパンを両腕で把持して袋に入れます。Diffusion Policy系のpolicyを自ら学習しました。同じ作業について、チームメンバーがVLAを学習しました。Task Planning Agentが、対象以外の領域を隠したimageと指示文で、このpolicyとVLAを呼び出すように接続しました。")),

        ("h3", "Drip coffee", ["past"]),
        ("p", L(
            "I developed this alone. Drip-coffee making was split into segments, and the learning method was chosen for each segment. Pouring water was a much more complex task than the other two, so it was learned with reinforcement learning.",
            "혼자 개발했습니다. 드립 커피 제조를 구간으로 나누고, 구간마다 학습 방법을 골랐습니다. 물 붓기는 다른 두 구간보다 훨씬 복잡한 작업이어서 강화학습으로 학습했습니다.",
            "単独で開発しました。ドリップコーヒーの製造を区間に分け、区間ごとに学習方法を選びました。湯注ぎはほかの2つの区間よりはるかに複雑な作業だったため、強化学習で学習しました。")),
        ("table",
         [L("Segment", "구간", "区間"), L("Method", "방법", "方法"), L("How", "방식", "進め方")],
         [
             [L("Grasping the kettle", "주전자 잡기", "ケトルの把持"), "Diffusion Policy (IL)",
              L("Learned from teleoperation demonstrations", "teleoperation 데모로 학습", "teleoperationのデモから学習")],
             [L("Placing the filter", "필터 놓기", "フィルターの設置"), "Diffusion Policy (IL)",
              L("Learned from teleoperation demonstrations", "teleoperation 데모로 학습", "teleoperationのデモから学習")],
             [L("Pouring water", "물 붓기", "湯注ぎ"), "PPO (RL)",
              L("Trained in simulation (MuJoCo), then tuned on the real robot", "simulation(MuJoCo)에서 학습한 뒤 실로봇에서 조정", "simulation（MuJoCo）で学習した後、実機で調整")],
         ], {"first_bold": True}),
        ("p", L(
            "The reward for pouring included posture alignment, smoothness of motion, avoidance of joint limits, and early termination when there was a risk of spilling. On the robot, policy actions at 30 Hz were interpolated and executed as 100 Hz pose commands. After real-robot evaluation, the policies were used in a store service. That service is no longer offered.",
            "물 붓기의 보상에는 자세 정렬, 동작의 부드러움, 관절 한계 회피를 넣었고, 유출 위험이 있으면 일찍 종료하게 했습니다. 로봇에서는 30 Hz의 policy action을 보간해 100 Hz의 pose 명령으로 실행했습니다. 실로봇 평가 뒤 매장 서비스에 사용했습니다. 지금은 그 서비스를 하지 않습니다.",
            "湯注ぎの報酬には、姿勢の整列、動作の滑らかさ、関節限界の回避を含め、こぼれる危険がある場合は早期に終了するようにしました。ロボット上では、30 Hzのpolicy actionを補間し、100 Hzのpose指令として実行しました。実機評価の後、店舗サービスで使用しました。現在、そのサービスは提供していません。")),

        ("h2", "decisions"),
        ("table", T_DECISION, [
            [L("Only the part that a fixed motion cannot do is learned.", "정해진 동작으로 안 되는 부분만 학습", "決まった動作ではできない部分だけを学習する"),
             L("Approach and disposal go to known positions. Only the grasp depends on the shape of the object.", "접근과 폐기는 정해진 위치로 감. 집는 동작만 물체의 모양에 좌우됨", "接近と廃棄は決まった位置に向かう。把持だけが物体の形に左右される"),
             L("Learning a whole task when one part needs it.", "한 부분만 필요한데 작업 전체를 학습하는 것", "一部だけが必要なのに、作業全体を学習すること")],
            [L("A task is split into segments, and each segment gets its own method.", "작업을 구간으로 나누고 구간마다 방법을 고름", "作業を区間に分け、区間ごとに方法を選ぶ"),
             L("Pouring is much more complex than grasping and placing.", "물 붓기는 잡기와 놓기보다 훨씬 복잡함", "湯注ぎは把持や設置よりはるかに複雑"),
             L("Forcing one method on every segment.", "모든 구간에 한 가지 방법을 쓰는 것", "すべての区間にひとつの方法を当てはめること")],
            [L("Image, state, and action are aligned in time when they are recorded.", "image, state, action을 기록할 때 시간을 맞춤", "image、state、actionを記録するときに時刻を合わせる"),
             L("A policy learns which action goes with which observation.", "policy는 어떤 관측에 어떤 action이 대응하는지를 학습함", "policyは、どの観測にどのactionが対応するかを学習する"),
             L("Training on pairs that do not belong together.", "서로 맞지 않는 쌍으로 학습하는 것", "対応していない組で学習すること")],
            [L("The planner calls the policy with a masked image and an instruction.", "planner가 가린 image와 지시문으로 policy를 호출", "plannerが、隠したimageと指示文でpolicyを呼び出す"),
             L("The planner has already chosen the target.", "대상은 planner가 이미 골랐음", "対象はplannerがすでに選んでいる"),
             L("The policy acting on a different object.", "policy가 다른 물체에 동작하는 것", "policyが別の物体に対して動作すること")],
        ], {}),

        ("h2", "scope"),
        ("table", T_SCOPE, [
            [SC_STATUS, L("In operation at company-run stores: single-arm policy. Real-robot testing: bimanual policy. Previously in operation: drip coffee. Ongoing: teleoperation and data collection.",
                          "직영 매장에서 운영: single-arm policy. 실로봇 테스트: bimanual policy. 과거 운영: 드립 커피. 진행 중: teleoperation과 데이터 수집.",
                          "直営店舗で運用中：single-arm policy。実機テスト：bimanual policy。過去に運用：ドリップコーヒー。進行中：teleoperationとデータ収集。")],
            [SC_MINE, L("Design and implementation of the teleoperation code, the code that builds the dataset, training of the Diffusion Policy family policies (including the trash-clearing policy in operation), connection of the policy and the VLA to the Task Planning Agent, and all of the drip coffee work.",
                        "teleoperation code의 설계와 구현, dataset을 만드는 code, Diffusion Policy 계열 policy의 학습(운영 중인 쓰레기 치우기 policy 포함), policy와 VLA를 Task Planning Agent에 연결, 드립 커피 전체.",
                        "teleoperation codeの設計と実装、datasetを作るcode、Diffusion Policy系のpolicyの学習（運用中のゴミ片付けpolicyを含む）、policyとVLAのTask Planning Agentへの接続、ドリップコーヒーのすべて。")],
            [SC_TEAM, L("Training of the VLA: a teammate. Current data collection: the data team and interns.",
                        "VLA 학습: 팀원. 지금의 데이터 수집: 데이터팀과 인턴.",
                        "VLAの学習：チームメンバー。現在のデータ収集：データチームとインターン。")],
            [SC_EXISTING, L("Diffusion Policy, the VLA, and PPO are public methods and models. I trained them and did not design their architecture.",
                            "Diffusion Policy, VLA, PPO는 공개된 방법과 모델입니다. 학습을 했고 구조를 직접 설계하지는 않았습니다.",
                            "Diffusion Policy、VLA、PPOは公開されている手法とモデルです。学習を行い、構造は自分で設計していません。")],
        ], {"first_bold": True}),

        ("h2", "links"),
        ("links", [
            ("agent-system", L("The semi-humanoid Task Planning Agent plans the order and calls the bimanual policy and the VLA.",
                               "세미 휴머노이드 로봇의 Task Planning Agent가 주문을 계획하고 bimanual policy와 VLA를 호출합니다.",
                               "セミヒューマノイドロボットのTask Planning Agentが注文を計画し、bimanual policyとVLAを呼び出します。")),
            ("perception-runtime", L("The ceiling camera and the gripper camera that the trash-clearing policy relies on.",
                                     "쓰레기 치우기 policy가 쓰는 천장 camera와 gripper camera.",
                                     "ゴミ片付けpolicyが利用する天井cameraとgripper camera。")),
        ]),
    ],
}
