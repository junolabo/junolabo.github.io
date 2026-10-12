# Project 1, part 3: Deployment & Model Update.
from .common import L, T_DECISION, T_SCOPE, SC_STATUS, SC_MINE, SC_EXISTING

PAGE = {
    "slug": "deployment",
    "project": 1,
    "title": "Deployment & Model Update",
    "claim": L(
        "The runtime and the models of 40+ stores are updated remotely. A new version or a new model reaches a store only after it passes a check.",
        "40여 개 매장의 runtime과 모델을 원격으로 갱신합니다. 새 버전과 새 모델은 검사를 통과한 뒤에만 매장에 들어갑니다.",
        "40店舗以上のruntimeとモデルを遠隔で更新します。新しいバージョンと新しいモデルは、検査を通過した後にのみ店舗に配布されます。",
    ),
    "facts": [
        ("role", L("Sole developer", "단독 개발", "単独開発")),
        ("period", L("Part of Project 1 (2023.10 – present)", "Project 1의 일부 (2023.10 - 현재)", "Project 1の一部（2023.10 - 現在）")),
        ("status", ("st", ["op_stores"])),
    ],
    "blocks": [
        ("h2", "problem"),
        ("p", L(
            "Before this work, a developer deployed software and updated models by hand. That stopped being workable as the number of stores grew.",
            "이 작업 전에는 개발자가 수동으로 소프트웨어를 배포하고 모델을 갱신했습니다. 매장이 늘면서 그 방식으로는 감당할 수 없게 됐습니다.",
            "この作業の前は、開発者が手作業でソフトウェアをデプロイし、モデルを更新していました。店舗が増えるにつれ、その方式では対応できなくなりました。")),
        ("points", [
            (L("Stores are not the same.", "매장은 서로 같지 않습니다.", "店舗は互いに同じではありません。"),
             L("Shelf size, robot configuration, and camera type differ from store to store.",
               "선반 크기, 로봇 구성, camera 종류가 매장마다 다릅니다.",
               "棚のサイズ、ロボット構成、cameraの種類が店舗ごとに異なります。")),
            (L("A model that improves at one store can get worse at another.", "한 매장에서 좋아진 모델이 다른 매장에서 나빠질 수 있습니다.", "ある店舗で良くなったモデルが、別の店舗で悪くなることがあります。"),
             L("Training on data from one store pulls the model toward that store.",
               "한 매장의 데이터로 학습하면 모델이 그 매장 쪽으로 치우칩니다.",
               "ひとつの店舗のデータで学習すると、モデルがその店舗に偏ります。")),
            (L("A bad deployment stops a store, and nobody is there.", "잘못된 배포는 매장을 멈추고, 현장에는 사람이 없습니다.", "誤ったデプロイは店舗を止め、現場には人がいません。"),
             L("A problem has to be found before the running service is replaced, not after.",
               "문제는 운영 중인 서비스를 교체한 뒤가 아니라 교체하기 전에 찾아야 합니다.",
               "問題は、運用中のサービスを切り替えた後ではなく、切り替える前に見つける必要があります。")),
        ]),

        ("h2", "structure"),
        ("p", L(
            "Three parts cover the life of a store: commissioning brings a new store into operation, OTA delivers the runtime, and the MLOps pipeline keeps the models current.",
            "세 부분이 매장의 전 과정을 맡습니다. commissioning은 신규 매장을 운영 상태로 만들고, OTA는 runtime을 전달하고, MLOps pipeline은 모델을 최신으로 유지합니다.",
            "3つの部分が店舗の全過程を担当します。commissioningは新規店舗を運用状態にし、OTAはruntimeを届け、MLOps pipelineはモデルを最新に保ちます。")),
        ("io", {
            "caption": L("Central server and stores", "중앙 서버와 매장", "中央サーバーと店舗"),
            "inputs": [
                (L("Store data", "매장 데이터", "店舗データ"), L("collected on the central server", "중앙 서버로 수집", "中央サーバーに収集")),
                (L("Store logs", "매장 로그", "店舗のログ"), L("collected in real time", "실시간 수집", "リアルタイムで収集")),
                (L("New store", "신규 매장", "新規店舗"), L("shelf, robot, cameras", "선반, 로봇, camera", "棚、ロボット、camera")),
            ],
            "core_title": L("Deployment system", "배포 체계", "デプロイの仕組み"),
            "nodes": [
                ("MLOps pipeline", L("select, label, review, train, evaluate", "선별, 라벨링, 검토, 학습, 평가", "選別、ラベリング、確認、学習、評価"), None),
                ("OTA", L("dry-run, compare, swap", "dry-run, 비교, 교체", "dry-run、比較、切り替え"), None),
                ("Commissioning", L("pre-check, calibration, verification", "사전 점검, calibration, 검증", "事前点検、calibration、検証"), None),
            ],
            "shared": (L("Per-store configuration and versioned calibration", "매장별 설정과 버전으로 관리하는 calibration", "店舗ごとの設定と、バージョン管理されたcalibration"),
                       L("store differences are data, not code branches", "매장의 차이는 code 분기가 아니라 데이터", "店舗の違いはcodeの分岐ではなくデータ")),
            "base": None,
            "outputs": [
                (L("Store devices", "매장 장치", "店舗の機器"), L("runtime and models, over Tailscale and Ansible", "runtime과 모델, Tailscale과 Ansible로 전달", "runtimeとモデル、TailscaleとAnsibleで配布")),
                (L("Alert", "알림", "通知"), L("when a store log shows an anomaly", "매장 로그에 이상이 있을 때", "店舗のログに異常があるとき")),
            ],
            "note": None,
        }),

        ("h2", "how"),
        ("h3", "MLOps pipeline", ["op"]),
        ("p", L(
            "The pipeline is applied to three models: stereo, detection, and VLM. People do not look at all the data. The pipeline selects the segments where the model's decision changed or where its confidence was low, labels them automatically, and a person reviews and corrects the labels.",
            "stereo, detection, VLM 세 모델에 적용합니다. 사람이 모든 데이터를 보지 않습니다. 모델의 판단이 바뀌거나 신뢰도가 낮은 구간을 pipeline이 고르고 자동으로 라벨링하면, 사람이 라벨을 검토하고 고칩니다.",
            "stereo、detection、VLMの3つのモデルに適用しています。人がすべてのデータを見ることはありません。モデルの判断が変わった区間や信頼度が低い区間をpipelineが選び、自動でラベリングし、人がラベルを確認して修正します。")),
        ("flow", L("One model update", "모델 갱신 1회", "モデル更新1回"), [
            (L("Store data", "매장 데이터", "店舗データ"), L("central server", "중앙 서버", "中央サーバー"), None),
            (L("Automatic selection", "자동 선별", "自動選別"), L("decision changed, or confidence low", "판단이 바뀌거나 신뢰도가 낮은 구간", "判断が変わった区間、信頼度が低い区間"), None),
            (L("Automatic labeling", "자동 라벨링", "自動ラベリング"), None, None),
            (L("Human review", "사람 검토", "人による確認"), L("labels are checked and corrected", "라벨을 확인하고 고침", "ラベルを確認して修正"), "judge"),
            (L("Training", "학습", "学習"), None, None),
            (L("Evaluation", "평가", "評価"), L("target store and all stores, scored separately", "해당 매장과 전체 매장을 따로 평가", "対象店舗と全店舗を別々に評価"), "judge"),
            (L("TensorRT conversion", "TensorRT 변환", "TensorRT変換"), None, None),
            (L("Deployment", "배포", "デプロイ"), None, None),
        ], L(
            "A new model passes only when it is above the threshold on the target store and on all stores, and better than the model in use. Otherwise it is not deployed.",
            "새 모델은 해당 매장과 전체 매장에서 모두 기준을 넘고, 쓰고 있는 모델보다 좋아야 통과합니다. 그렇지 않으면 배포하지 않습니다.",
            "新しいモデルは、対象店舗と全店舗の両方で基準を超え、使用中のモデルより良い場合にのみ通過します。そうでなければデプロイしません。")),

        ("h3", "OTA", ["op"]),
        ("p", L(
            "The unit of deployment is the whole runtime. A central server reaches the store devices over Tailscale and deploys with Ansible. The new version does not replace the running service at once. It first runs as a dry-run, and its behavior is compared with the previous version.",
            "배포 단위는 전체 runtime입니다. 중앙 서버가 Tailscale로 매장 장치에 접속하고 Ansible로 배포합니다. 새 버전은 운영 중인 서비스를 바로 교체하지 않습니다. 먼저 dry-run으로 돌리고, 이전 버전과 동작을 비교합니다.",
            "デプロイの単位はruntime全体です。中央サーバーがTailscaleで店舗の機器に接続し、Ansibleでデプロイします。新しいバージョンは、運用中のサービスをすぐには置き換えません。まずdry-runとして動かし、以前のバージョンと動作を比較します。")),
        ("flow", L("One deployment", "배포 1회", "デプロイ1回"), [
            (L("New version", "새 버전", "新しいバージョン"), None, None),
            (L("Dry-run", "Dry-run", "Dry-run"), L("before the running service is replaced", "운영 중인 서비스를 교체하기 전에", "運用中のサービスを置き換える前に"), None),
            (L("Comparison", "비교", "比較"), L("errors, communication with other devices, decisions", "오류, 다른 장치와의 통신, 판단 결과", "エラー、他の機器との通信、判断結果"), "judge"),
            (L("Swap", "교체", "切り替え"), L("the service is replaced", "서비스를 교체", "サービスを置き換える"), None),
            (L("Live logs", "실시간 로그", "リアルタイムのログ"), L("an anomaly raises an alert", "이상 시 알림", "異常時に通知"), None),
        ], None),

        ("h3", "Commissioning", ["op"]),
        ("p", L(
            "Differences between stores, such as shelf size, robot configuration, and camera type, are handled by configuration and not by code branches. The same runtime runs in every store. Calibration results are kept as versions, so a store can be returned to an earlier calibration.",
            "매장마다 다른 선반 크기, 로봇 구성, camera 종류를 code 분기 없이 설정으로 처리합니다. 모든 매장에서 같은 runtime이 돌아갑니다. calibration 결과를 버전으로 관리하므로, 매장을 이전 calibration으로 되돌릴 수 있습니다.",
            "店舗ごとに異なる棚のサイズ、ロボット構成、cameraの種類を、codeの分岐ではなく設定で扱います。すべての店舗で同じruntimeが動きます。calibrationの結果をバージョン管理しているため、店舗を以前のcalibrationに戻せます。")),
        ("flow", L("One new store", "신규 매장 1곳", "新規店舗1件"), [
            (L("Pre-check", "사전 점검", "事前点検"), None, None),
            (L("Camera calibration", "Camera calibration", "Camera calibration"), None, None),
            (L("Result verification", "결과 검증", "結果検証"), None, "judge"),
            (L("Start of operation", "운영 시작", "運用開始"), None, None),
        ], None),

        ("h2", "decisions"),
        ("p", L(
            "Each row is a risk and the step that stops it.",
            "각 행은 위험 하나와 그것을 막는 단계입니다.",
            "各行は、ひとつのリスクと、それを止める段階です。")),
        ("table",
         [L("Risk", "위험", "リスク"), L("What stops it", "막는 단계", "止める段階"), L("Part", "부분", "部分")],
         [
             [L("A model improves at one store and gets worse overall.", "모델이 한 매장에서 좋아지고 전체에서는 나빠짐", "モデルがある店舗で良くなり、全体では悪くなる"),
              L("It is evaluated separately on the target store and on all stores. Both must pass.", "해당 매장과 전체 매장을 따로 평가. 둘 다 통과해야 함", "対象店舗と全店舗を別々に評価。両方の通過が必要"),
              "MLOps pipeline"],
             [L("A new model is no better than the one in use.", "새 모델이 쓰고 있는 모델보다 좋지 않음", "新しいモデルが使用中のモデルより良くない"),
              L("It must also be better than the current model.", "쓰고 있는 모델보다도 좋아야 함", "使用中のモデルより良いことも必要"),
              "MLOps pipeline"],
             [L("Automatic labels are wrong.", "자동 라벨이 틀림", "自動ラベルが誤っている"),
              L("A person reviews and corrects them before training.", "학습 전에 사람이 검토하고 고침", "学習の前に人が確認して修正する"),
              "MLOps pipeline"],
             [L("A new version has an error, breaks communication with other devices, or changes decisions.", "새 버전에 오류가 있거나, 다른 장치와의 통신이 깨지거나, 판단 결과가 달라짐", "新しいバージョンにエラーがある、他の機器との通信が壊れる、判断結果が変わる"),
              L("The dry-run is compared with the previous version before the swap.", "교체 전에 dry-run을 이전 버전과 비교", "切り替えの前に、dry-runを以前のバージョンと比較する"),
              "OTA"],
             [L("A store misbehaves after a deployment.", "배포 뒤에 매장이 이상하게 동작", "デプロイ後に店舗の動作がおかしくなる"),
              L("Store logs are collected in real time, and an anomaly raises an alert.", "매장 로그를 실시간 수집하고 이상 시 알림", "店舗のログをリアルタイムで収集し、異常時に通知する"),
              "OTA"],
             [L("A new store has a different shelf, robot, or camera.", "신규 매장의 선반, 로봇, camera가 다름", "新規店舗の棚、ロボット、cameraが異なる"),
              L("The difference is written as configuration. The code is not branched.", "차이를 설정으로 씀. code를 분기하지 않음", "違いを設定として書く。codeは分岐しない"),
              "Commissioning"],
             [L("A calibration turns out to be wrong.", "calibration이 잘못된 것으로 드러남", "calibrationが誤っていたと分かる"),
              L("Calibration results are versioned. The store returns to the earlier version.", "calibration 결과를 버전으로 관리. 이전 버전으로 되돌림", "calibrationの結果をバージョン管理。以前のバージョンに戻す"),
              "Commissioning"],
         ], {"cls": "risk"}),

        ("h2", "scope"),
        ("table", T_SCOPE, [
            [SC_STATUS, ("st", ["op_stores"])],
            [SC_MINE, L("All of it: the OTA procedure, the MLOps pipeline for three models, the configuration structure, and the commissioning procedure.",
                        "전부. OTA 절차, 세 모델의 MLOps pipeline, 설정 구조, commissioning 절차.",
                        "すべて。OTAの手順、3つのモデルのMLOps pipeline、設定の構造、commissioningの手順。")],
            [SC_EXISTING, L("Tailscale, Ansible, and TensorRT are existing tools.",
                            "Tailscale, Ansible, TensorRT는 기존 도구입니다.",
                            "Tailscale、Ansible、TensorRTは既存のツールです。")],
        ], {"first_bold": True}),

        ("h2", "links"),
        ("links", [
            ("perception-runtime", L("The stereo and detection models and the runtime that the system on this page deploys.",
                                     "이 페이지의 체계로 배포하는 stereo 모델, detection 모델, runtime.",
                                     "このページの仕組みでデプロイするstereoモデル、detectionモデル、runtime。")),
            ("anomaly-detection", L("The VLM is the third model updated by the pipeline. Reviewed cases go into its next training data.",
                                    "VLM은 pipeline으로 갱신하는 세 번째 모델입니다. 검토한 사례가 다음 학습 데이터로 들어갑니다.",
                                    "VLMは、pipelineで更新する3つ目のモデルです。確認済みの事例が次の学習データに入ります。")),
        ]),
    ],
}
