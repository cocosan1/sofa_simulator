import streamlit as st
import pandas as pd
import os
from PIL import Image

# pip install streamlit pandas pillow openpyxl

st.set_page_config('sofa 画像抽出app', layout='wide')
st.markdown('# sofa 画像抽出app')

# ソファ画像のディレクトリ
image_dir = "./img/sofa/"

df = pd.read_excel('./sofa_info.xlsx')

# 全選択オプションを追加
all_option = "全て選択"

## 項目選択
# シリーズ
op_series_list1 = [all_option] + df["シリーズ"].unique().tolist()
op_series_list2 = st.sidebar.multiselect(\
    "シリーズ", op_series_list1, default=[all_option]
    )

if op_series_list2 == [all_option]:
    filtered_df = df
else:
    filtered_df = df[df["シリーズ"].isin(op_series_list2)]

# 色系統/木部
op_woodcolor2_list = [all_option] + filtered_df["色系統/木部"].unique().tolist()
op_woodcolor2 = st.sidebar.selectbox("色系統/木部", op_woodcolor2_list)

if op_woodcolor2 == all_option:
    filtered_df = filtered_df
else:
    filtered_df = filtered_df[filtered_df["色系統/木部"] == op_woodcolor2]

# 色系統/張地
op_fabric2_list1 = filtered_df["色系統/張地"].unique().tolist()
op_fabric2_list1 = sorted(op_fabric2_list1)
op_fabric2_list1 = [all_option] + op_fabric2_list1
op_fabric2_list2 = st.sidebar.multiselect(\
    "色系統/張地", op_fabric2_list1, default=[all_option]
    )

if op_fabric2_list2 == [all_option]:
    filtered_df = filtered_df
else:
    filtered_df = filtered_df[filtered_df["色系統/張地"].isin(op_fabric2_list2)]

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
op_fabric_list1 = filtered_df["張地"].unique().tolist()
op_fabric_list1 = sorted(op_fabric_list1)
op_fabric_list1 = [all_option] + op_fabric_list1 
op_fabric_list2 = st.sidebar.multiselect(\
    "張地", op_fabric_list1, default=[all_option]
    )

if op_fabric_list2 == [all_option]:
    filtered_df = filtered_df
else:
    filtered_df = filtered_df[filtered_df["張地"].isin(op_fabric_list2)]

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



