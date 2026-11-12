import streamlit as st
import datetime
import html

# ページ設定
st.set_page_config(
    page_title="No.1 人間の理解 練習問題",
    page_icon="📝",
    layout="centered"
)

# 明朝体およびルビ表示用カスタムCSS
st.markdown("""
<style>
  * {
    font-family: "Hiragino Mincho ProN", "Yu Mincho", "MS Mincho", "Source Han Serif", serif !important;
  }
  ruby { ruby-align: center; }
  rt { font-size: 0.55em; font-weight: normal; line-height: 1; }
  .chapter-header {
    background-color: #334155;
    color: white;
    padding: 6px 12px;
    border-radius: 4px;
    font-weight: bold;
    margin: 20px 0 10px 0;
  }
  .section-header {
    color: #475569;
    font-weight: bold;
    border-bottom: 1px dashed #94a3b8;
    padding-bottom: 4px;
    margin: 15px 0 10px 0;
  }
  .q-title {
    font-size: 1.05rem;
    font-weight: bold;
    margin-bottom: 8px;
    color: #1e293b;
  }
  .correct-text {
    color: #166534;
    background-color: #dcfce7;
    padding: 4px 8px;
    border-radius: 4px;
    font-weight: bold;
    display: inline-block;
    margin-top: 6px;
  }
  .incorrect-text {
    color: #991b1b;
    background-color: #fee2e2;
    padding: 4px 8px;
    border-radius: 4px;
    font-weight: bold;
    display: inline-block;
    margin-top: 6px;
  }
</style>
""", unsafe_allow_html=True)

# タイトル表示
st.markdown("""
<h2 style='text-align: center; border-bottom: 2px solid #2c3e50; padding-bottom: 8px;'>
No.1 <ruby>人<rt>にん</rt>間<rt>げん</rt></ruby>の<ruby>理<rt>り</rt>解<rt>かい</rt></ruby> <ruby>練<rt>れん</rt>習<rt>しゅう</rt>問<rt>もん</rt>題<rt>だい</rt></ruby>
</h2>
<p style='text-align: center; font-size: 0.9rem; color: #555;'>
Google Classroom 課題提出対応Webアプリ（全25問・4択式）
</p>
""", unsafe_allow_html=True)

# 学生情報入力カード
st.markdown("### 👤 学生情報の入力")
col1, col2, col3 = st.columns([1, 1, 1.5])
with col1:
    s_class = st.text_input("組（クラス名）", placeholder="例: 1年A組")
with col2:
    s_id = st.text_input("学籍番号", placeholder="例: 20260101")
with col3:
    s_name = st.text_input("氏名", placeholder="例: 山田 太郎")

# 設問データ（全25問）
questions = [
    {
        "num": 1,
        "chapter": "第1章 人間の尊厳と自立",
        "section": "第1節 人間の尊厳と人権・福祉理念",
        "stem": "1. <ruby>人<rt>にん</rt>間<rt>げん</rt></ruby>を<ruby>理<rt>り</rt>解<rt>かい</rt></ruby>することについての<ruby>記<rt>き</rt>述<rt>じゅつ</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>個<rt>こ</rt>人<rt>じん</rt></ruby>の<ruby>過<rt>か</rt>去<rt>こ</rt></ruby>を<ruby>無<rt>む</rt>視<rt>し</rt></ruby>し、<ruby>現<rt>げん</rt>在<rt>ざい</rt></ruby>の<ruby>状<rt>じょう</rt>態<rt>たい</rt></ruby>のみを<ruby>把<rt>は</rt>握<rt>あく</rt></ruby>すること",
            "2. <ruby>現<rt>げん</rt>実<rt>じつ</rt></ruby>の<ruby>生<rt>せい</rt>活<rt>かつ</rt>状<rt>じょう</rt>況<rt>きょう</rt></ruby>と、これまでの<ruby>生<rt>せい</rt>活<rt>かつ</rt></ruby>から<ruby>未<rt>み</rt>来<rt>らい</rt></ruby>への<ruby>志<rt>し</rt>向<rt>こう</rt>性<rt>せい</rt></ruby>を<ruby>含<rt>ふく</rt></ruby>めた<ruby>生<rt>せい</rt>活<rt>かつ</rt></ruby>の<ruby>営<rt>いとな</rt></ruby>みの<ruby>歴<rt>れき</rt>史<rt>し</rt></ruby>を<ruby>理<rt>り</rt>解<rt>かい</rt></ruby>すること",
            "3. <ruby>病<rt>びょう</rt>気<rt>き</rt></ruby>や<ruby>障<rt>しょう</rt>害<rt>がい</rt></ruby>の<ruby>名<rt>めい</rt>称<rt>しょう</rt></ruby>や<ruby>症<rt>しょう</rt>状<rt>じょう</rt></ruby>だけを<ruby>詳<rt>くわ</rt></ruby>しく<ruby>調<rt>しら</rt></ruby>べること",
            "4. <ruby>介<rt>かい</rt>護<rt>ご</rt>者<rt>しゃ</rt></ruby>の<ruby>価<rt>か</rt>値<rt>ち</rt>観<rt>かん</rt></ruby>に<ruby>基<rt>もと</rt></ruby>づいて<ruby>相<rt>あい</rt>手<rt>て</rt></ruby>を<ruby>評<rt>ひょう</rt>価<rt>か</rt></ruby>すること"
        ],
        "answer": 2,
        "exp": "選択肢 2（生活の営みの歴史）"
    },
    {
        "num": 2,
        "stem": "2. <ruby>障<rt>しょう</rt>害<rt>がい</rt>者<rt>しゃ</rt>基<rt>き</rt>本<rt>ほん</rt>法<rt>ほう</rt>第<rt>だい</rt></ruby>1<ruby>条<rt>じょう</rt></ruby>に<ruby>規<rt>き</rt>定<rt>てい</rt></ruby>されている<ruby>理<rt>り</rt>念<rt>ねん</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>能<rt>のう</rt>力<rt>りょく</rt>主<rt>しゅ</rt>義<rt>ぎ</rt></ruby>の<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>",
            "2. <ruby>個<rt>こ</rt>人<rt>じん</rt></ruby>の<ruby>尊<rt>そん</rt>厳<rt>げん</rt></ruby>の<ruby>尊<rt>そん</rt>重<rt>ちょう</rt></ruby>",
            "3. <ruby>社<rt>しゃ</rt>会<rt>かい</rt>防<rt>ぼう</rt>衛<rt>えい</rt></ruby>の<ruby>優<rt>ゆう</rt>先<rt>せん</rt></ruby>",
            "4. <ruby>救<rt>きゅう</rt>貧<rt>ひん</rt>の<ruby>制<rt>せい</rt>限<rt>げん</rt></ruby>"
        ],
        "answer": 2,
        "exp": "選択肢 2（個人の尊厳の尊重）"
    },
    {
        "num": 3,
        "stem": "3. <ruby>介<rt>かい</rt>護<rt>ご</rt></ruby>において、その<ruby>人<rt>ひと</rt>自<rt>じ</rt>身<rt>しん</rt></ruby>の<ruby>生<rt>せい</rt>活<rt>かつ</rt>設<rt>せっ</rt>計<rt>けい</rt></ruby>を<ruby>利<rt>り</rt>用<rt>よう</rt>者<rt>しゃ</rt></ruby>とともに<ruby>立<rt>た</rt></ruby>てていくときに<ruby>踏<rt>ふ</rt></ruby>まえるべき<ruby>基<rt>き</rt>本<rt>ほん</rt>姿<rt>し</rt>勢<rt>せい</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>介<rt>かい</rt>護<rt>ご</rt>者<rt>しゃ</rt>主<rt>しゅ</rt>導<rt>どう</rt></ruby>",
            "2. <ruby>管<rt>かん</rt>理<rt>り</rt>者<rt>しゃ</rt>都<rt>つ</rt>合<rt>ごう</rt></ruby>",
            "3. <ruby>利<rt>り</rt>用<rt>よう</rt>者<rt>しゃ</rt>主<rt>しゅ</rt>体<rt>たい</rt></ruby>",
            "4. <ruby>家<rt>か</rt>族<rt>ぞく</rt>優<rt>ゆう</rt>先<rt>せん</rt></ruby>"
        ],
        "answer": 3,
        "exp": "選択肢 3（利用者主体）"
    },
    {
        "num": 4,
        "stem": "4. 1980<ruby>年<rt>ねん</rt></ruby>にWHOが<ruby>提<rt>てい</rt>示<rt>じ</rt></ruby>した<ruby>国<rt>こく</rt>際<rt>さい</rt>障<rt>しょう</rt>害<rt>がい</rt>分<rt>ぶん</rt>類<rt>るい</rt></ruby>（ICIDH）における3つのレベルとして、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>機<rt>き</rt>能<rt>のう</rt>障<rt>しょう</rt>害<rt>がい</rt></ruby>・<ruby>能<rt>のう</rt>力<rt>りょく</rt>障<rt>しょう</rt>害<rt>がい</rt></ruby>・<ruby>社<rt>しゃ</rt>会<rt>かい</rt>的<rt>てき</rt>不<rt>ふ</rt>利<rt>り</rt></ruby>",
            "2. <ruby>心<rt>しん</rt>身<rt>しん</rt>機<rt>き</rt>能<rt>のう</rt></ruby>・<ruby>活<rt>かつ</rt>動<rt>どう</rt></ruby>・<ruby>参<rt>さん</rt>加<rt>か</rt></ruby>",
            "3. <ruby>環<rt>かん</rt>境<rt>きょう</rt>因<rt>いん</rt>子<rt>し</rt></ruby>・<ruby>個<rt>こ</rt>人<rt>じん</rt>因<rt>いん</rt>子<rt>し</rt></ruby>・<ruby>健<rt>けん</rt>康<rt>こう</rt>状<rt>じょう</rt>態<rt>たい</rt></ruby>",
            "4. <ruby>肉<rt>にく</rt>体<rt>たい</rt>障<rt>しょう</rt>害<rt>がい</rt></ruby>・<ruby>精<rt>せい</rt>神<rt>しん</rt>障<rt>しょう</rt>害<rt>がい</rt></ruby>・<ruby>感<rt>かん</rt>覚<rt>かく</rt>障<rt>しょう</rt>害<rt>がい</rt></ruby>"
        ],
        "answer": 1,
        "exp": "選択肢 1（機能障害・能力障害・社会的不利）"
    },
    {
        "num": 5,
        "stem": "5. 2001<ruby>年<rt>ねん</rt></ruby>にWHOが<ruby>採<rt>さい</rt>択<rt>たく</rt></ruby>した、<ruby>人<rt>ひと</rt></ruby>が<ruby>生<rt>い</rt></ruby>きることの<ruby>全<rt>ぜん</rt>体<rt>たい</rt>像<rt>ぞう</rt></ruby>をとらえる「ICF」の<ruby>正<rt>しょう</rt>式<rt>しき</rt>名<rt>めい</rt>称<rt>しょう</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>国<rt>こく</rt>際<rt>さい</rt>疾<rt>しっ</rt>病<rt>ぺい</rt>分<rt>ぶん</rt>類<rt>るい</rt></ruby>",
            "2. <ruby>国<rt>こく</rt>際<rt>さい</rt>障<rt>しょう</rt>害<rt>がい</rt>分<rt>ぶん</rt>類<rt>るい</rt></ruby>",
            "3. <ruby>国<rt>こく</rt>際<rt>さい</rt>生<rt>せい</rt>活<rt>かつ</rt>機<rt>き</rt>能<rt>のう</rt>分<rt>ぶん</rt>類<rt>るい</rt></ruby>",
            "4. <ruby>世<rt>せ</rt>界<rt>かい</rt>介<rt>かい</rt>護<rt>ご</rt>基<rt>き</rt>準<rt>じゅん</rt>分<rt>ぶん</rt>類<rt>るい</rt></ruby>"
        ],
        "answer": 3,
        "exp": "選択肢 3（国際生活機能分類）"
    },
    {
        "num": 6,
        "stem": "6. <ruby>障<rt>しょう</rt>害<rt>がい</rt>者<rt>しゃ</rt>権<rt>けん</rt>利<rt>り</rt>条<rt>じょう</rt>約<rt>やく</rt></ruby>の<ruby>策<rt>さく</rt>定<rt>てい</rt></ruby>にあたり、<ruby>当<rt>とう</rt>事<rt>じ</rt>者<rt>しゃ</rt>団<rt>だん</rt>体<rt>たい</rt></ruby>が<ruby>掲<rt>かか</rt></ruby>げたスローガン（Nothing About Us Without Us）の<ruby>日<rt>に</rt>本<rt>ほん</rt>語<rt>ご</rt>訳<rt>やく</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>私<rt>わたし</rt></ruby>たちのためにすべてを<ruby>決<rt>き</rt></ruby>めてほしい",
            "2. <ruby>私<rt>わたし</rt></ruby>たち<ruby>抜<rt>ぬ</rt></ruby>きに<ruby>私<rt>わたし</rt></ruby>たちのことを<ruby>決<rt>き</rt></ruby>めないで",
            "3. <ruby>誰<rt>だれ</rt></ruby>もが<ruby>同<rt>おな</rt></ruby>じように<ruby>暮<rt>く</rt></ruby>らす<ruby>社<rt>しゃ</rt>会<rt>かい</rt></ruby>をつくろう",
            "4. <ruby>私<rt>わたし</rt></ruby>たちに<ruby>特<rt>とく</rt>別<rt>べつ</rt></ruby>な<ruby>保<rt>ほ</rt>護<rt>ご</rt></ruby>を<ruby>与<rt>あた</rt></ruby>えてください"
        ],
        "answer": 2,
        "exp": "選択肢 2（私たち抜きに私たちのことを決めないで）"
    },
    {
        "num": 7,
        "stem": "7. <ruby>日<rt>に</rt>本<rt>ほん</rt>国<rt>こく</rt>憲<rt>けん</rt>法<rt>ぽう</rt>第<rt>だい</rt></ruby>13<ruby>条<rt>じょう</rt>前<rt>ぜん</rt>段<rt>だん</rt></ruby>で「すべて<ruby>国<rt>こく</rt>民<rt>みん</rt></ruby>は、<ruby>何<rt>なに</rt></ruby>として<ruby>尊<rt>そん</rt>重<rt>ちょう</rt></ruby>される」と<ruby>規<rt>き</rt>定<rt>てい</rt></ruby>されているか、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>労<rt>ろう</rt>働<rt>どう</rt>者<rt>しゃ</rt></ruby>",
            "2. <ruby>家<rt>か</rt>族<rt>ぞく</rt></ruby>",
            "3. <ruby>個<rt>こ</rt>人<rt>じん</rt></ruby>",
            "4. <ruby>生<rt>せい</rt>活<rt>かつ</rt>者<rt>しゃ</rt></ruby>"
        ],
        "answer": 3,
        "exp": "選択肢 3（個人）"
    },
    {
        "num": 8,
        "stem": "8. <ruby>日<rt>に</rt>本<rt>ほん</rt>国<rt>こく</rt>憲<rt>けん</rt>法<rt>ぽう</rt>第<rt>だい</rt></ruby>25<ruby>条<rt>じょう</rt>第<rt>だい</rt></ruby>1<ruby>項<rt>こう</rt></ruby>が<ruby>保<rt>ほ</rt>障<rt>しょう</rt></ruby>する<ruby>生<rt>せい</rt>存<rt>ぞん</rt>権<rt>けん</rt></ruby>の<ruby>内<rt>ない</rt>容<rt>よう</rt></ruby>として、「すべて<ruby>国<rt>こく</rt>民<rt>みん</rt></ruby>は、（　）で<ruby>文<rt>ぶん</rt>化<rt>か</rt>的<rt>てき</rt></ruby>な<ruby>最<rt>さい</rt>低<rt>てい</rt>限<rt>げん</rt>度<rt>ど</rt></ruby>の<ruby>生<rt>せい</rt>活<rt>かつ</rt></ruby>を<ruby>営<rt>いとな</rt></ruby>む<ruby>権<rt>けん</rt>利<rt>り</rt></ruby>を<ruby>有<rt>ゆう</rt></ruby>する」の（　）に<ruby>入<rt>はい</rt></ruby>る<ruby>言<rt>こと</rt>葉<rt>ば</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>平<rt>へい</rt>和<rt>わ</rt></ruby>",
            "2. <ruby>健<rt>けん</rt>康<rt>こう</rt></ruby>",
            "3. <ruby>裕<rt>ゆう</rt>福<rt>ふく</rt></ruby>",
            "4. <ruby>安<rt>あん</rt>定<rt>てい</rt></ruby>"
        ],
        "answer": 2,
        "exp": "選択肢 2（健康）"
    },
    {
        "num": 9,
        "stem": "9. <ruby>社<rt>しゃ</rt>会<rt>かい</rt>福<rt>ふく</rt>祉<rt>し</rt>法<rt>ほう</rt>第<rt>だい</rt></ruby>3<ruby>条<rt>じょう</rt></ruby>における、<ruby>福<rt>ふく</rt>祉<rt>し</rt></ruby>サービス<ruby>利<rt>り</rt>用<rt>よう</rt>者<rt>しゃ</rt></ruby>の<ruby>位<rt>い</rt>置<rt>ち</rt></ruby>づけとして、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>保<rt>ほ</rt>護<rt>ご</rt></ruby>を<ruby>受<rt>う</rt></ruby>けるだけの<ruby>存<rt>そん</rt>在<rt>ざい</rt>",
            "2. <ruby>措<rt>そ</rt>置<rt>ち</rt></ruby>の<ruby>対<rt>たい</rt>象<rt>しょう</rt>となる<ruby>客<rt>きゃく</rt>体<rt>たい</rt>",
            "3. <ruby>福<rt>ふく</rt>祉<rt>し</rt></ruby>サービスを<ruby>利<rt>り</rt>用<rt>よう</rt></ruby>する<ruby>主<rt>しゅ</rt>体<rt>たい</rt>",
            "4. <ruby>行<rt>ぎょう</rt>政<rt>せい</rt></ruby>の<ruby>指<rt>し</rt>導<rt>どう</rt></ruby>に<ruby>従<rt>したが</rt></ruby>うべき<ruby>者<rt>もの</rt>"
        ],
        "answer": 3,
        "exp": "選択肢 3（福祉サービスを利用する主体）"
    },
    {
        "num": 10,
        "stem": "10. <ruby>介<rt>かい</rt>護<rt>ご</rt>保<rt>ほ</rt>険<rt>けん</rt>法<rt>ほう</rt>第<rt>だい</rt></ruby>1<ruby>条<rt>じょう</rt></ruby>で<ruby>定<rt>さだ</rt></ruby>められている<ruby>保<rt>ほ</rt>持<rt>じ</rt></ruby>すべきものとして、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>労<rt>ろう</rt>働<rt>どう</rt>能<rt>のう</rt>力<rt>りょく</rt></ruby>",
            "2. <ruby>尊<rt>そん</rt>厳<rt>げん</rt></ruby>",
            "3. <ruby>財<rt>ざい</rt>産<rt>さん</rt>",
            "4. <ruby>身<rt>しん</rt>体<rt>たい</rt>規<rt>き</rt>律<rt>りつ</rt></ruby>"
        ],
        "answer": 2,
        "exp": "選択肢 2（尊厳）"
    },
    {
        "num": 11,
        "stem": "11. 1601<ruby>年<rt>ねん</rt></ruby>にイギリスで<ruby>制<rt>せい</rt>定<rt>てい</rt></ruby>されたエリザベス<ruby>救<rt>きゅう</rt>貧<rt>ひん</rt>法<rt>ほう</rt></ruby>の<ruby>主<rt>おも</rt></ruby>な<ruby>目<rt>もく</rt>的<rt>てき</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>社<rt>しゃ</rt>会<rt>かい</rt>防<rt>ぼう</rt>衛<rt>えい</rt></ruby>と<ruby>労<rt>ろう</rt>働<rt>どう</rt>力<rt>りょく</rt></ruby>の<ruby>確<rt>かく</rt>保<rt>ほ</rt></ruby>",
            "2. <ruby>個<rt>こ</rt>人<rt>じん</rt></ruby>の<ruby>幸<rt>しあわ</rt></ruby>せの<ruby>追<rt>つい</rt>求<rt>きゅう</rt></ruby>",
            "3. ノーマライゼーションの<ruby>実<rt>じつ</rt>現<rt>げん</rt></ruby>",
            "4. <ruby>民<rt>みん</rt>間<rt>かん</rt>ボランティアの<ruby>育<rt>いく</rt>成<rt>せい</rt></ruby>"
        ],
        "answer": 1,
        "exp": "選択肢 1（社会防衛と労働力の確保）"
    },
    {
        "num": 12,
        "stem": "12. 1834<ruby>年<rt>ねん</rt></ruby>のイギリス<ruby>新<rt>しん</rt>救<rt>きゅう</rt>貧<rt>ひん</rt>法<rt>ほう</rt></ruby>において、「<ruby>救<rt>きゅう</rt>済<rt>さい</rt></ruby>の<ruby>水<rt>すい</rt>準<rt>じゅん</rt></ruby>は<ruby>最<rt>さい</rt>下<rt>か</rt>級<rt>きゅう</rt></ruby>の<ruby>独<rt>どく</rt>立<rt>りつ</rt>労<rt>ろう</rt>働<rt>どう</rt>者<rt>しゃ</rt></ruby>の<ruby>生<rt>せい</rt>活<rt>かつ</rt>条<rt>じょう</rt>件<rt>けん</rt>以<rt>い</rt>下<rt>か</rt></ruby>でなければならない」とした<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>均<rt>きん</rt>等<rt>とう</rt>処<rt>しょ</rt>遇<rt>ぐう</rt></ruby>の<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>",
            "2. <ruby>劣<rt>れっ</rt>等<rt>とう</rt>処<rt>しょ</rt>遇<rt>ぐう</rt></ruby>の<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>",
            "3. <ruby>居<rt>きょ</rt>宅<rt>たく</rt>救<rt>きゅう</rt>済<rt>さい</rt></ruby>の<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>",
            "4. <ruby>生<rt>せい</rt>存<rt>ぞん</rt>保<rt>ほ</rt>障<rt>しょう</rt></ruby>の<ruby>原<rt>げん</rt>則<rt>そく</rt></ruby>"
        ],
        "answer": 2,
        "exp": "選択肢 2（劣等処遇の原則）"
    },
    {
        "num": 13,
        "stem": "13. 19<ruby>世<rt>せい</rt>紀<rt>き</rt>後<rt>こう</rt>半<rt>はん</rt>の<ruby>慈<rt>じ</rt>善<rt>ぜん</rt>組<rt>そ</rt>織<rt>しき</rt>協<rt>きょう</rt>会<rt>かい</rt>（COS）が<ruby>友<rt>ゆう</rt>愛<rt>あい</rt>訪<rt>ほう</rt>問<rt>もん</rt>によって<ruby>行<rt>おこな</rt></ruby>ったこととして、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>金<rt>きん</rt>銭<rt>せん</rt></ruby>の<ruby>無<rt>む</rt>制<rt>せい</rt>限<rt>げん</rt></ruby>な<ruby>給<rt>きゅう</rt>付<rt>ふ</rt>",
            "2. <ruby>貧<rt>ひん</rt>困<rt>こん</rt>者<rt>しゃ</rt></ruby>への<ruby>道<rt>どう</rt>徳<rt>とく</rt>的<rt>てき</rt>助<rt>じょ</rt>言<rt>げん</rt></ruby>",
            "3. <ruby>医<rt>い</rt>療<rt>りょう</rt></ruby>の<ruby>無<rt>む</rt>償<rt>しょう</rt>提<rt>てい</rt>供<rt>きょう</rt>",
            "4. <ruby>住<rt>じゅう</rt>宅<rt>たく</rt></ruby>の<ruby>建<rt>けん</rt>設<rt>せつ</rt></ruby>と<ruby>配<rt>はい</rt>分<rt>ぶん</rt>"
        ],
        "answer": 2,
        "exp": "選択肢 2（道徳的助言）"
    },
    {
        "num": 14,
        "stem": "14. 1917<ruby>年<rt>ねん</rt></ruby>に『<ruby>社<rt>しゃ</rt>会<rt>かい</rt>診<rt>しん</rt>断<rt>だん</rt></ruby>』を<ruby>著<rt>あらわ</rt></ruby>し、「ケースワークの<ruby>母<rt>はは</rt></ruby>」と<ruby>呼<rt>よ</rt></ruby>ばれる<ruby>人<rt>じん</rt>物<rt>ぶつ</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. ナイチンゲール",
            "2. メアリー・リッチモンド",
            "3. バンク＝ミケルセン",
            "4. ニィリエ"
        ],
        "answer": 2,
        "exp": "選択肢 2（メアリー・リッチモンド）"
    },
    {
        "num": 15,
        "stem": "15. ナイチンゲールが1859<ruby>年<rt>ねん</rt></ruby>の『<ruby>看<rt>かん</rt>護<rt>ご</rt>覚<rt>おぼ</rt></ruby>え<ruby>書<rt>がき</rt></ruby>』で<ruby>示<rt>しめ</rt></ruby>した<ruby>看<rt>かん</rt>護<rt>ご</rt></ruby>の2<ruby>本<rt>ほん</rt>柱<rt>ばしら</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>手<rt>しゅ</rt>術<rt>じゅつ</rt></ruby>の<ruby>執<rt>しっ</rt>刀<rt>とう</rt></ruby>と<ruby>薬<rt>くすり</rt></ruby>の<ruby>調<rt>ちょう</rt>合<rt>ごう</rt>",
            "2. <ruby>診<rt>しん</rt>療<rt>りょう</rt></ruby>の<ruby>補<rt>ほ</rt>助<rt>じょ</rt></ruby>と<ruby>療<rt>りょう</rt>養<rt>よう</rt>上<rt>じょう</rt></ruby>の<ruby>世<rt>せ</rt>話<rt>わ</rt>",
            "3. <ruby>病<rt>びょう</rt>院<rt>いん</rt>経<rt>けい</rt>営<rt>えい</rt></ruby>と<ruby>施<rt>し</rt>設<rt>せつ</rt>管<rt>かん</rt>理<rt>り</rt>",
            "4. <ruby>患<rt>かん</rt>者<rt>しゃ</rt></ruby>の<ruby>隔<rt>かく</rt>離<rt>り</rt></ruby>と<ruby>監<rt>かん</rt>視<rt>し</rt>"
        ],
        "answer": 2,
        "exp": "選択肢 2（診療の補助と療養上の世話）"
    },
    {
        "num": 16,
        "stem": "16. デンマークの1959<ruby>年<rt>ねん</rt>法<rt>ほう</rt></ruby>においてノーマライゼーションの<ruby>理<rt>り</rt>念<rt>ねん</rt></ruby>を<ruby>盛<rt>も</rt></ruby>り<ruby>込<rt>こ</rt></ruby>んだ「<ruby>生<rt>う</rt></ruby>みの<ruby>親<rt>おや</rt></ruby>」として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. バンク＝ミケルセン",
            "2. ニィリエ",
            "3. ヴォルフェンスベルガー",
            "4. リッチモンド"
        ],
        "answer": 1,
        "exp": "選択肢 1（バンク＝ミケルセン）"
    },
    {
        "num": 17,
        "stem": "17. ノーマライゼーションの「<ruby>育<rt>そだ</rt></ruby>ての<ruby>親<rt>おや</rt></ruby>」と<ruby>呼<rt>よ</rt></ruby>ばれるスウェーデンのニィリエが<ruby>提<rt>てい</rt>唱<rt>しょう</rt></ruby>した<ruby>具<rt>ぐ</rt>体<rt>たい</rt>的<rt>てき</rt>目<rt>もく</rt>標<rt>ひょう</rt></ruby>の<ruby>数<rt>かず</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. 3つ",
            "2. 5つ",
            "3. 8つ",
            "4. 12<ruby>個<rt>こ</rt></ruby>"
        ],
        "answer": 3,
        "exp": "選択肢 3（8つ）"
    },
    {
        "num": 18,
        "stem": "18. すべての<ruby>人<rt>ひと</rt></ruby>を<ruby>社<rt>しゃ</rt>会<rt>かい</rt></ruby>から<ruby>排<rt>はい</rt>除<rt>じょ</rt></ruby>せず、<ruby>社<rt>しゃ</rt>会<rt>かい</rt></ruby>の<ruby>構<rt>こう</rt>成<rt>せい</rt>員<rt>いん</rt></ruby>として<ruby>包<rt>つつ</rt></ruby>み<ruby>支<rt>ささ</rt></ruby>え<ruby>合<rt>あ</rt></ruby>う<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby>を<ruby>表<rt>あらわ</rt></ruby>す<ruby>用<rt>よう</rt>語<rt>ご</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. パターナリズム",
            "2. ソーシャルインクルージョン",
            "3. ネグレクト",
            "4. インスティチューショナリズム"
        ],
        "answer": 2,
        "exp": "選択肢 2（ソーシャルインクルージョン）"
    },
    {
        "num": 19,
        "stem": "19. <ruby>人<rt>じん</rt>生<rt>せい</rt></ruby>の<ruby>最<rt>さい</rt>終<rt>しゅう</rt>段<rt>だん</rt>階<rt>かい</rt></ruby>における<ruby>医<rt>い</rt>療<rt>りょう</rt></ruby>やケアについて、<ruby>本<rt>ほん</rt>人<rt>にん</rt></ruby>・<ruby>家<rt>か</rt>族<rt>ぞく</rt></ruby>・<ruby>医<rt>い</rt>療<rt>りょう</rt>ケアチームが<ruby>前<rt>まえ</rt></ruby>もって<ruby>話<rt>はな</rt></ruby>し<ruby>合<rt>あ</rt></ruby>いを<ruby>重<rt>かさ</rt></ruby>ねるプロセスの<ruby>略<rt>りゃく</rt>称<rt>しょう</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. ACP",
            "2. QOL",
            "3. ADL",
            "4. ICF"
        ],
        "answer": 1,
        "exp": "選択肢 1（ACP）"
    },
    {
        "num": 20,
        "stem": "20. びわこ<ruby>学<rt>がく</rt>園<rt>えん</rt></ruby>を<ruby>創<rt>そう</rt>設<rt>せつ</rt></ruby>し、「この<ruby>子<rt>こ</rt></ruby>らを<ruby>世<rt>よ</rt></ruby>の<ruby>光<rt>ひかり</rt></ruby>に」という<ruby>言<rt>こと</rt>葉<rt>ば</rt></ruby>を<ruby>残<rt>のこ</rt></ruby>した<ruby>日<rt>に</rt>本<rt>ほん</rt></ruby>の<ruby>先<rt>せん</rt>駆<rt>く</rt>者<rt>しゃ</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>渋<rt>しぶ</rt>沢<rt>さわ</rt>栄<rt>えい</rt>一<rt>いち</rt></ruby>",
            "2. <ruby>糸<rt>いと</rt>賀<rt>が</rt>一<rt>かず</rt>雄<rt>お</rt></ruby>",
            "3. <ruby>石<rt>いし</rt>井<rt>い</rt>十<rt>じゅう</rt>次<rt>じ</rt></ruby>",
            "4. <ruby>留<rt>とめ</rt>岡<rt>おか</rt>幸<rt>ゆき</rt>助<rt>すけ</rt></ruby>"
        ],
        "answer": 2,
        "exp": "選択肢 2（糸賀一雄）"
    },
    {
        "num": 21,
        "section": "第2節 自立のあり方",
        "stem": "21. <ruby>自<rt>みずか</rt></ruby>らの<ruby>理<rt>り</rt>性<rt>せい</rt></ruby>や<ruby>規<rt>き</rt>範<rt>はん</rt>に<ruby>基<rt>もと</rt></ruby>づき、<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>の<ruby>行<rt>こう</rt>動<rt>どう</rt></ruby>を<ruby>自<rt>じ</rt>律<rt>りつ</rt>的<rt>てき</rt></ruby>にコントロールして<ruby>行<rt>こう</rt>為<rt>い</rt></ruby>を<ruby>決<rt>き</rt></ruby>める<ruby>概<rt>がい</rt>念<rt>ねん</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>自<rt>じ</rt>律<rt>りつ</rt></ruby>",
            "2. <ruby>孤<rt>こ</rt>立<rt>りつ</rt></ruby>",
            "3. <ruby>放<rt>ほう</rt>任<rt>にん</rt></ruby>",
            "4. <ruby>従<rt>じゅう</rt>属<rt>ぞく</rt></ruby>"
        ],
        "answer": 1,
        "exp": "選択肢 1（自律）"
    },
    {
        "num": 22,
        "stem": "22. <ruby>介<rt>かい</rt>護<rt>ご</rt></ruby>における「<ruby>自<rt>じ</rt>立<rt>りつ</rt></ruby>」についての<ruby>考<rt>かんが</rt></ruby>え<ruby>方<rt>かた</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>他<rt>た</rt>人<rt>にん</rt></ruby>の<ruby>手<rt>て</rt></ruby>をまったく<ruby>借<rt>か</rt></ruby>りずにすべて1<ruby>人<rt>ひとり</rt></ruby>でできること",
            "2. <ruby>必<rt>ひつ</rt>要<rt>よう</rt></ruby>なときに<ruby>他<rt>た</rt>者<rt>しゃ</rt></ruby>に<ruby>支<rt>し</rt>援<rt>えん</rt></ruby>を<ruby>求<rt>もと</rt></ruby>めるなど、<ruby>適<rt>てき</rt>切<rt>せつ</rt></ruby>で<ruby>適<rt>てき</rt>度<rt>ど</rt></ruby>な<ruby>依<rt>い</rt>存<rt>ぞん</rt></ruby>を<ruby>含<rt>ふく</rt></ruby>むこと",
            "3. すべての<ruby>判<rt>はん</rt>断<rt>だん</rt></ruby>を<ruby>家<rt>か</rt>族<rt>ぞく</rt>や<ruby>介<rt>かい</rt>護<rt>ご</rt>者<rt>しゃ</rt>に<ruby>任<rt>まか</rt></ruby>せること",
            "4. <ruby>社<rt>しゃ</rt>会<rt>かい</rt></ruby>との<ruby>関<rt>かか</rt></ruby>わりを<ruby>絶<rt>た</rt></ruby>って<ruby>自<rt>じ</rt>活<rt>かつ</rt>すること"
        ],
        "answer": 2,
        "exp": "選択肢 2（適切で適度な依存を含むこと）"
    },
    {
        "num": 23,
        "stem": "23. <ruby>病<rt>びょう</rt>気<rt>き</rt></ruby>やけがにより<ruby>障<rt>しょう</rt>害<rt>がい</rt></ruby>された<ruby>機<rt>き</rt>能<rt>のう</rt>以<rt>い</rt>外<rt>がい</rt></ruby>の、<ruby>残<rt>のこ</rt></ruby>された<ruby>機<rt>き</rt>能<rt>のう</rt></ruby>を<ruby>表<rt>あらわ</rt></ruby>す<ruby>用<rt>よう</rt>語<rt>ご</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>廃<rt>はい</rt>用<rt>よう</rt>機<rt>き</rt>能<rt>のう</rt></ruby>",
            "2. <ruby>代<rt>だい</rt>償<rt>しょう</rt>機<rt>き</rt>能<rt>のう</rt></ruby>",
            "3. <ruby>残<rt>ざん</rt>存<rt>ぞん</rt>機<rt>き</rt>能<rt>のう</rt></ruby>",
            "4. <ruby>潜<rt>せん</rt>在<rt>ざい</rt>機<rt>き</rt>能<rt>のう</rt></ruby>"
        ],
        "answer": 3,
        "exp": "選択肢 3（残存機能）"
    },
    {
        "num": 24,
        "chapter": "第2章 人間関係とコミュニケーション",
        "section": "第1節 人間と人間関係",
        "stem": "24. <ruby>対<rt>たい</rt>人<rt>じん</rt>援<rt>えん</rt>助<rt>じょ</rt>職<rt>しょく</rt></ruby>が<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>の<ruby>内<rt>ない</rt>面<rt>めん</rt></ruby>や<ruby>価<rt>か</rt>値<rt>ち</rt>観<rt>かん</rt></ruby>、<ruby>言<rt>げん</rt>動<rt>どう</rt></ruby>の<ruby>特<rt>とく</rt>徴<rt>ちょう</rt></ruby>について<ruby>深<rt>ふか</rt></ruby>く<ruby>知<rt>し</rt></ruby>ることを<ruby>表<rt>あらわ</rt></ruby>す<ruby>用<rt>よう</rt>語<rt>ご</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>自<rt>じ</rt>己<rt>こ</rt>覚<rt>かく</rt>知<rt>ち</rt></ruby>",
            "2. <ruby>自<rt>じ</rt>己<rt>こ</rt>防<rt>ぼう</rt>衛<rt>えい</rt></ruby>",
            "3. <ruby>他<rt>た</rt>者<rt>しゃ</rt>評<rt>ひょう</rt>価<rt>か</rt></ruby>",
            "4. <ruby>感<rt>かん</rt>情<rt>じょう</rt>移<rt>い</rt>入<rt>にゅう</rt></ruby>"
        ],
        "answer": 1,
        "exp": "選択肢 1（自己覚知）"
    },
    {
        "num": 25,
        "stem": "25. 「ジョハリの<ruby>窓<rt>まど</rt></ruby>」において、「<ruby>他<rt>た</rt>者<rt>しゃ</rt></ruby>は<ruby>知<rt>し</rt></ruby>っているが、<ruby>自<rt>じ</rt>分<rt>ぶん</rt></ruby>は<ruby>気<rt>き</rt></ruby>づいていない」<ruby>領<rt>りょう</rt>域<rt>いき</rt></ruby>の<ruby>名<rt>めい</rt>称<rt>しょう</rt></ruby>として、<ruby>最<rt>さい</rt>適<rt>てき</rt></ruby>なものを1つ<ruby>選<rt>えら</rt></ruby>びなさい。",
        "options": [
            "1. <ruby>開<rt>かい</rt>放<rt>ほう</rt></ruby>の<ruby>窓<rt>まど</rt></ruby>",
            "2. <ruby>盲<rt>もう</rt>点<rt>てん</rt></ruby>の<ruby>窓<rt>まど</rt></ruby>",
            "3. <ruby>秘<rt>ひ</rt>密<rt>みつ</rt></ruby>の<ruby>窓<rt>まど</rt></ruby>",
            "4. <ruby>未<rt>み</rt>知<rt>ち</rt></ruby>の<ruby>窓<rt>まど</rt></ruby>"
        ],
        "answer": 2,
        "exp": "選択肢 2（盲点の窓）"
    }
]

# 回答入力フォーム
user_answers = {}

st.markdown("---")
st.markdown("### ✍️ 練習問題（各問の選択肢を選んでください）")

for q in questions:
    if "chapter" in q:
        st.markdown(f"<div class='chapter-header'>{q['chapter']}</div>", unsafe_allow_html=True)
    if "section" in q:
        st.markdown(f"<div class='section-header'>{q['section']}</div>", unsafe_allow_html=True)

    st.markdown(f"<div class='q-title'>{q['stem']}</div>", unsafe_allow_html=True)
    
    # ルビ対応のため各選択肢をHTMLでレンダリングしつつラジオボタンで選択
    choice_labels = [f"選択肢 {i+1}" for i in range(len(q['options']))]
    for opt in q['options']:
        st.markdown(f"<div style='margin-left: 20px; font-size:0.95rem; margin-bottom: 4px;'>{opt}</div>", unsafe_allow_html=True)
    
    selected_idx = st.radio(
        label=f"Q{q['num']}の回答を選択:",
        options=[1, 2, 3, 4],  # ← [1, 2, 3, 4] に修正
        index=None,
        horizontal=True,
        key=f"q_{q['num']}",
    )
    user_answers[q['num']] = selected_idx
    st.markdown("<div style='margin-bottom: 15px;'></div>", unsafe_allow_html=True)

# 採点・提出ファイル作成ボタン
st.markdown("---")
if st.button("📊 採点して提出用レポートを作成する", type="primary", use_container_width=True):
    if not s_class.strip() or not s_id.strip() or not s_name.strip():
        st.error("⚠️ 「組（クラス名）」「学籍番号」「氏名」をすべて入力してください。")
    else:
        # 採点
        score = 0
        unanswered = 0
        report_rows = ""
        
        for q in questions:
            u_ans = user_answers[q['num']]
            is_correct = (u_ans == q['answer'])
            if u_ans is None:
                unanswered += 1
                status = "<span style='color:red;'>未回答 ×</span>"
            elif is_correct:
                score += 1
                status = "<span style='color:green;'>正解 ○</span>"
            else:
                status = "<span style='color:red;'>不正解 ×</span>"
            
            report_rows += f"""
            <tr>
              <td style='padding:6px;border:1px solid #ccc;text-align:center;'>第 {q['num']} 問</td>
              <td style='padding:6px;border:1px solid #ccc;text-align:center;'>{u_ans if u_ans else '未回答'}</td>
              <td style='padding:6px;border:1px solid #ccc;text-align:center;'>{q['answer']}</td>
              <td style='padding:6px;border:1px solid #ccc;text-align:center;'>{status}</td>
            </tr>
            """
        
        total = len(questions)
        percent = round((score / total) * 100)
        
        # 画面上にスコア表示
        st.success(f"🎉 採点が完了しました！ 得点: **{score} / {total} 点**（正答率: {percent}%）")
        if unanswered > 0:
            st.warning(f"※ 未回答の問題が {unanswered} 問ありました。")

        # レポートHTMLファイルの構築
        timestamp = datetime.datetime.now().strftime("%Y年%m月%d日 %H:%M:%S")
        auth_raw = f"{s_class}_{s_id}_{s_name}_{score}_{timestamp}"
        auth_code = f"VER-{abs(hash(auth_raw)):X}-{datetime.datetime.now().strftime('%f')}"

        report_html = f"""<!DOCTYPE html>
<html lang="ja">
<head>
<meta charset="UTF-8">
<title>提出用レポート_{html.escape(s_name)}</title>
<style>
  body {{ font-family: "Hiragino Mincho ProN", "Yu Mincho", serif; padding: 25px; line-height: 1.6; color: #222; }}
  .report-box {{ max-width: 650px; margin: 0 auto; border: 2px solid #2c3e50; padding: 20px; border-radius: 6px; }}
  h2 {{ text-align: center; border-bottom: 2px solid #2c3e50; padding-bottom: 8px; margin-top: 0; }}
  .info-table {{ width: 100%; border-collapse: collapse; margin-bottom: 16px; }}
  .info-table td {{ padding: 6px 10px; border: 1px solid #999; }}
  .info-table td.header {{ background: #eee; font-weight: bold; width: 30%; }}
  .score-box {{ text-align: center; background: #eef2ff; border: 1px solid #6366f1; padding: 12px; margin-bottom: 16px; border-radius: 4px; }}
  .score-box span {{ font-size: 1.8rem; font-weight: bold; color: #1e1b4b; }}
  table.results {{ width: 100%; border-collapse: collapse; font-size: 0.9rem; }}
  table.results th {{ background: #f1f5f9; padding: 6px; border: 1px solid #ccc; }}
  .auth-tag {{ font-family: monospace; font-size: 0.8rem; color: #64748b; word-break: break-all; margin-top: 15px; border-top: 1px dashed #ccc; padding-top: 8px; }}
</style>
</head>
<body>
<div class="report-box">
  <h2>課題提出用 成績レポート</h2>
  <table class="info-table">
    <tr><td class="header">教科・課題</td><td>No.1 人間の理解 練習問題（4択）</td></tr>
    <tr><td class="header">組（クラス）</td><td>{html.escape(s_class)}</td></tr>
    <tr><td class="header">学籍番号</td><td>{html.escape(s_id)}</td></tr>
    <tr><td class="header">氏名</td><td>{html.escape(s_name)}</td></tr>
    <tr><td class="header">実施日時</td><td>{timestamp}</td></tr>
  </table>
  <div class="score-box">
    得点：<span>{score} / {total} 点</span>（正答率 {percent}%）
  </div>
  <h3>各設問の回答記録</h3>
  <table class="results">
    <thead>
      <tr><th>設問番号</th><th>あなたの回答</th><th>正解</th><th>判定</th></tr>
    </thead>
    <tbody>
      {report_rows}
    </tbody>
  </table>
  <div class="auth-tag">
    【改ざん防止用 認証コード】<br>{auth_code}
  </div>
</div>
</body>
</html>"""

        # ダウンロードボタン設置
        st.markdown("### 📥 課題提出手順")
        st.info("""
        1. 下の **「提出用レポート（HTML）を保存」** ボタンを押して、成績レポートファイルを保存してください。
        2. Google Classroom の該当課題ページを開きます。
        3. **「あなたの課題」→「追加または作成」→「ファイル」** からダウンロードしたファイルを添付し、**「提出」** を押してください。
        """)

        file_name = f"提出用_人間の理解_{s_id}_{s_name}.html"
        st.download_button(
            label="📥 提出用レポート（HTML）を保存",
            data=report_html,
            file_name=file_name,
            mime="text/html",
            use_container_width=True
        )

        st.markdown("[Google Classroom を開く ↗]([suspicious link removed])", unsafe_allow_html=True)
