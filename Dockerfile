FROM python:3.14.0a7-bullseye

# DevContainer用のユーザー作成
RUN groupadd -g 20000 devuser \
    && useradd -m -u 20000 -g 20000 devuser
USER devuser

# python実行環境
RUN mkdir -p /home/devuser/app

# Pythonのパッケージインストール(AtCoder利用可能なもの)
RUN pip install sortedcontainers numpy mpmath sympy networkx


WORKDIR /home/devuser/app