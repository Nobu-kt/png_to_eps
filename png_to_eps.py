import subprocess
import os

# PNGファイルが格納されているディレクトリ
png = "./png"

# EPSファイルを格納するディレクトリ
eps = "./eps"

# EPSファイルを格納するディレクトリが存在しない場合は作成する
if not os.path.exists(eps):
    os.makedirs(eps)


# ディレクトリ内の全てのPNGファイルを変換
for filename in os.listdir(png):
    if filename.endswith(".png"):
        # PNGファイルのパス
        png_path = os.path.join(png, filename)
        
        # 出力EPSファイルのパス
        basename = os.path.splitext(filename)[0]
        eps_path = os.path.join(eps, f"{basename}.eps")

        subprocess.run(["convert", f"{png_path}", f"{eps_path}"])
        
        print(f"Converted {png_path} to {eps_path}")

print("All PNG files have been converted to EPS format.")

