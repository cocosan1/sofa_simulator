import streamlit as st
import pandas as pd
import os
from PIL import Image
from io import BytesIO
import base64
from st_clickable_images import clickable_images

# pip install streamlit pandas pillow openpyxl st-clickable-images

st.set_page_config('sofa simulator', layout='wide')
st.markdown('# sofa simulator')

# ソファ画像のディレクトリ
image_dir = "./img/sofa/"

df = pd.read_excel('./sofa_info.xlsx')

# 全選択オプションを追加
all_option = "全て選択"

## 項目選択

# シリーズ
op_series_list = [all_option] + df["シリーズ"].unique().tolist()
op_series = st.sidebar.selectbox("シリーズ", op_series_list)

if op_series == all_option:
    filtered_df = df
else:
    filtered_df = df[df["シリーズ"] == op_series]

# 色系統/木部
op_woodcolor2_list = [all_option] + filtered_df["色系統/木部"].unique().tolist()
op_woodcolor2 = st.sidebar.selectbox("色系統/木部", op_woodcolor2_list)

if op_woodcolor2 == all_option:
    filtered_df = filtered_df
else:
    filtered_df = filtered_df[filtered_df["色系統/木部"] == op_woodcolor2]

# 色系統/張地
op_fabric2_list = [all_option] + filtered_df["色系統/張地"].unique().tolist()
op_fabric2 = st.sidebar.selectbox("色系統/張地", op_fabric2_list)

if op_fabric2 == all_option:
    filtered_df = filtered_df
else:
    filtered_df = filtered_df[filtered_df["色系統/張地"] == op_fabric2]

# 材質
op_kinds_list = [all_option] + filtered_df["材質"].unique().tolist()
op_kinds = st.sidebar.selectbox("材質", op_kinds_list)

if op_kinds == all_option:
    filtered_df = filtered_df
else:
    filtered_df = filtered_df[filtered_df["材質"] == op_kinds]

# 塗色
op_woodcolor1_list = [all_option] + filtered_df["塗色"].unique().tolist()
op_woodcolor1 = st.sidebar.selectbox("塗色", op_woodcolor1_list)

if op_woodcolor1 == all_option:
    filtered_df = filtered_df
else:
    filtered_df = filtered_df[filtered_df["塗色"] == op_woodcolor1]

# 張地
op_fabric_list = [all_option] + filtered_df["張地"].unique().tolist()
op_fabric = st.sidebar.selectbox("張地", op_fabric_list)

if op_fabric == all_option:
    filtered_df = filtered_df
else:
    filtered_df = filtered_df[filtered_df["張地"] == op_fabric]

# サイズ
op_size_list = [all_option] + filtered_df["サイズ"].unique().tolist()
op_size = st.sidebar.selectbox("サイズ", op_size_list)

if op_size == all_option:
    filtered_df = filtered_df
else:
    filtered_df = filtered_df[filtered_df["サイズ"] == op_size]

col1, col2 = st.columns(2)

# 検索結果の画像を表示
for i in range(len(filtered_df)):
    image_path = os.path.join(image_dir, filtered_df["ファイル名"].iloc[i])
    image = Image.open(image_path)

    series_name = filtered_df["シリーズ"].iloc[i]
    wood_color = filtered_df["塗色"].iloc[i]
    fabric_name = filtered_df["張地"].iloc[i]
    text = f'{series_name} {wood_color} {fabric_name}'

    # 偶数はcol1 奇数はcol2
    if i == 0:
        with col1:
            st.image(image,caption=text)
    elif i % 2 == 0:
        with col1:
            st.image(image,caption=text)
    else:
        with col2:
            st.image(image,caption=text)
    
    # 30枚でstop
    if i == 30:
        break



# opened_imgs = []
# # 検索結果の画像をfilesリストに格納
# for i in range(len(filtered_df)):
#     image_path = os.path.join(image_dir, filtered_df["ファイル名"].iloc[i])
#     image = Image.open(image_path)
#     opened_imgs.append(image)
    
#     images = []
#     for file in opened_imgs:
#         # BytesIOを使用してpngファイルをバイナリーデータに変換
#         # メモリ上でバイナリデータを扱う
#         image_bytes = BytesIO()
#         # メモリ上に保存
#         file.save(image_bytes, format='PNG')
#         #バイナリデータをテキストに変換し扱いやすい文字列に変換
#         encoded = base64.b64encode(image_bytes.getvalue()).decode()
#         #HTMLで表示可能な形式に変換 HTML の img タグの src 属性に相当
#         images.append(f"data:image/png;base64,{encoded}")

#     #returns the index of the last image clicked on
#     clicked = clickable_images(
#         images,
#         titles=[f"Image #{fname}" for fname in images],
#         #cssの設定
#         # 要素をフレックスボックスとして表示 直下の子要素を横並び　子要素を水平方向に中央揃え
#         # コンテナに収まりきらない場合、アイテムを折り返して新しい行に配置
#         div_style={"display": "flex", "justify-content": "center", "flex-wrap": "wrap"},
#         #余白
#         img_style={"margin": "5px", "height": "200px"},
#     )



