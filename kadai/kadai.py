import streamlit as st
import numpy as np
import pandas as pd

st.title("はんたいことば")
images = {
 "おおきい(大きい)": "ookii.png",
 "ちいさい(小さい)": "chiisai.png",
 "ながい(長い)": "nagai.png",
 "みじかい(短い)":"mijikai.png",
 "たかい(高い)": "takai.png",
 "ひくい(低い)":"hikui.png",
 "おもい(重い)":"omoi.png", 
 "かるい(軽い)":"karui.png",
 "ふとい(太い)":"futoi.png", 
 "ほそい(細い)":"hosoi.png",
 "あつい(厚い)":"atsui.png", 
 "うすい(薄い)":"usui.png",
 "あさい(浅い)": "asai.png",
 "ふかい(深い)":"fukai.png",
 "あかるい(明るい)":"akarui.png",
 "くらい(暗い)":"kurai.png",
 "ちかい(近い)": "chikai.png",
 "とおい(遠い)":"tooi.png",
 "ひろい(広い)": "hiroi.png",
 "せまい(狭い)":"semai.png",
 "つよい(強い)": "tsuyoi.png",
 "よわい(弱い)":"yowai.png",
 "あたらしい(新しい)":"atarashii.png",
 "ふるい(古い)":"furui.png",
 "はやい(速い)":"hayai.png",
 "おそい(遅い)":"osoi.png",
 "おおい(多い)":"ooi.png",
 "すくない(少ない)":"sukunai.png",
 "うえ(上)": "ue.png",
 "した(下)":"shita.png",
 "まえ(前)": "mae.png",
 "うしろ(後ろ)":"ushiro.png",
 "おもて(表)": "omote.png",
 "うら(裏)":"ura.png",
 "なか(中)": "naka.png",
 "そと(外)":"soto.png",
 "ひだり(左)": "hidari.png",
 "みぎ(右)":"migi.png",
 "あがる(上がる)": "agaru.png",
 "さがる(下がる)":"sagaru.png",
 "さむい(寒い)": "samui.png",
 "あつい(暑い)":"hot.png",
 "やわらかい(柔らかい)": "yawarakai.png",
 "かたい(硬い)":"katai.png",
 "いりぐち(いりぐち)":"iriguchi.png",
 "でぐち(出口)":"deguchi.png",
 "のぼる(上る)": "noboru.png",
 "くだる(下る)":"kudaru.png",
 "おとこ(男)": "otoko.png",
 "おんな(女)":"onna.png",
 "おす(押す)": "osu.png",
 "ひく(引く)":"hiku.png",
 "ぬぐ(脱ぐ)": "nugu.png",
 "きる(着る)":"kiru.png",
 "あける(開ける)": "akeru.png",
 "しめる(閉める)":"shimeru.png",
 "いく(行く)": "iku.png",
 "かえる(帰る)":"kaeru.png",
 "うく(浮く)": "uku.png",
 "しずむ(沈む)":"shizumu.png",
 "おとす(落とす)":"otosu.png",
 "ひろう(拾う)":"hirou.png",
 "いれる(入れる)":"ireru.png",
 "だす(出す)":"dasu.png",
 "おきる(起きる)":"okiru.png",
 "ねる(寝る)":"neru.png"
 }

biginner_word_pairs = {
    "おおきい(大きい)": "ちいさい(小さい)",
    "ながい(長い)": "みじかい(短い)",
    "たかい(高い)": "ひくい(低い)",
    "おもい(重い)": "かるい(軽い)",
    "ふとい(太い)": "ほそい(細い)",
    "あつい(厚い)": "うすい(薄い)",
    "あさい(浅い)": "ふかい(深い)",
    "あかるい(明るい)": "くらい(暗い)",
    "ちかい(近い)": "とおい(遠い)",
    "ひろい(広い)": "せまい(狭い)",
    "つよい(強い)": "よわい(弱い)"
}
intermediate_words_pairs = {
    "あたらしい(新しい)": "ふるい(古い)",
    "はやい(速い)": "おそい(遅い)",
    "おおい(多い)": "すくない(少ない)",
    "うえ(上)": "した(下)",
    "まえ(前)": "うしろ(後ろ)",
    "おもて(表)": "うら(裏)",
    "なか(中)": "そと(外)",
    "ひだり(左)": "みぎ(右)",
    "あがる(上がる)": "さがる(下がる)",
    "さむい(寒い)": "あつい(暑い)",
    "やわらかい(柔らかい)": "かたい(硬い)"
}
advanced_words_pairs = {
    "いりぐち(いりぐち)": "でぐち(出口)",
    "のぼる(上る)": "くだる(下る)",
    "おとこ(男)": "おんな(女)",
    "おす(押す)": "ひく(引く)",
    "ぬぐ(脱ぐ)": "きる(着る)",
    "あける(開ける)": "しめる(閉める)",
    "いく(行く)": "かえる(帰る)",
    "うく(浮く)": "しずむ(沈む)",
    "おとす(落とす)":"ひろう(拾う)",
    "いれる(入れる)":"だす(出す)",
    "おきる(起きる)":"ねる(寝る)"
    }

hantaikotoba_data_set = {
  "★": biginner_word_pairs,
  "★★": intermediate_words_pairs,
  "★★★": advanced_words_pairs
}
level = st.sidebar.radio("レベルを選択", ["★","★★","★★★"])
word_pairs = hantaikotoba_data_set[level]
if st.button("出題"):
  index = np.random.randint(0,10)
  english_word = list(word_pairs.keys())[index]
  st.markdown(f"## {english_word}")
  image = images[english_word]
  st.image(image)

  with st.expander("解答を見る"):
    japanese_word = word_pairs[english_word]
    st.write(f"## {japanese_word}")
    image2 = images[japanese_word]
    st.image(image2)

if st.button("次の問題へ"):
  placeholder = st.empty()
  placeholder.empty()






  